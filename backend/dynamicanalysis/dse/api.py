import sys
from io import StringIO
import logging
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import PexSerializer, OptionsSerializer, ProgramPairingSerializer, RandomSampling
from .symbolic.loader import *
from .symbolic.explore import ExplorationEngine
from dynamicanalysis.settings import STATIC_FILES
from graphviz import render
from django.http import HttpResponse, Http404
from .template import combinedProgram
from jinja2 import Template
import numpy as np
from storage import Storage
from utils import getFunc
import asyncio



def generateRandomInput(low, high, size, varSize):
    args = []
    while(varSize > 0):
        args.append(np.random.randint(low, high, size=size, dtype=np.int64))
        varSize -= 1
    return zip(*args)


def calcNumOfAgreedInputs(refId, id, refProject, project, inpAr, entry):
    solutionFunc, _ = getFunc(refId, refProject, entry)
    submissionFunc, _ = getFunc(id, project, entry)
    numOfAgreedInps = 0
    outputs = []
    inputs = []
    for i in inpAr:
        refO = solutionFunc(*i)
        O = submissionFunc(*i)
        inputs.append([int(j) for j in i])
        outputs.append([int(refO) if isinstance(refO, np.int64) else refO,
                        int(O) if isinstance(O, np.int64) else O])
        if solutionFunc(*i) == submissionFunc(*i):
            numOfAgreedInps += 1
    return outputs, inputs, numOfAgreedInps


def concolicTest(id, maxIters, isPse, project):
    fileName = 'paired_program_' + id + '.py'
    entry = 'pairedProgram'

    if not isPse:
        fileName = project['fileName'] + '.py'
        entry = project['entry']

    pyFilePath = os.path.join(STATIC_FILES / id, fileName)
    if fileName[:-3] in sys.modules:
        del(sys.modules[fileName[:-3]])

    app = loaderFactory(pyFilePath, entry)

    if app == None:
        raise ImportError("Please provide a Python file to load")

    generatedInputs = []
    returnVals = []

    try:
        engine = ExplorationEngine(app.createInvocation(), solver="z3")
        generatedInputs, returnVals, path = engine.explore(maxIters)
        # output DOT graph
        if (not isPse):


            file = open(pyFilePath + ".dot", "w")
            file.write(path.toDot())
            file.close()
           
            render(engine='dot', format='png',
                   filepath=STATIC_FILES / id / file.name)              

    except ImportError as e:
        raise

    return [generatedInputs, returnVals]


class PexResult(object):
    def __init__(self, generated_inputs, output):
        self.generated_inputs = generated_inputs
        self.output = output


def pairProgram(refId, projects):
    refProject = projects[refId]
    for id in projects:
        if id == refId:
            continue

        project = projects[id]

        params = {}
        params["referenceId"] = refId
        params["id"] = id
        params["solution"] = refProject['fileName']
        params["submission"] = project['fileName']
        params["entry"] = project['entry']
        params["variables"] = ', '.join(project['params'])
        destionationPy = 'paired_program_' + id + '.py'
        destinationPath = os.path.join(
            STATIC_FILES / id, destionationPy)

        with open(destinationPath, 'w') as destination:
            template = Template(combinedProgram)
            destFileContent = template.render(**params)
            destination.write(destFileContent)


class PexAPI(viewsets.GenericViewSet):
    serializer_class = PexSerializer

    def postPSE(self, request):
        storage = Storage()

        entry = request.data['entry']

        projects = storage.getProjectsByEntry(entry)

        pseRes = {}
        for id in projects:
            project = projects[id]
            if (project['isReference']):
                continue

            inputs, outputs = concolicTest(
                id, request.data['max_iter'], True, project)

            numOfCorrOutput = sum([x for x in outputs if (x == 1 or x)])

            pseData = {
                "percent": round((numOfCorrOutput / len(outputs)) * 100),
                "passed": numOfCorrOutput,
                "all": len(outputs),
                "inputs": inputs,
                "outputs": outputs
            }

            storage.setMetric(id, 'pse', pseData)

            pseRes[id] = pseData

        data = {
            "entry": entry,
            "name": "pse",
            "data": pseRes
        }

        return Response({
            "msg": "PSE cacl done successfully",
            "data": data
        })

    def postDSE(self, request):
        storage = Storage()
        entry = request.data['entry']
        projects = storage.getProjectsByEntry(entry)

        files = []
        for id in projects:
            project = projects[id]
            log_stream = StringIO()
            # logging.basicConfig(stream=log_stream, level=logging.DEBUG)
            # logFile = os.path.join(STATIC_FILES / id, 'logfile.txt')
            logger = logging.getLogger()
            logger.setLevel(logging.DEBUG)
            hdlr = logging.StreamHandler(log_stream)
            logger.addHandler(hdlr)
   
            inputs, outputs = concolicTest(
                id, request.data['max_iter'], False, project)
            logs = log_stream.getvalue()

            storage.setProjectDseRes(id, inputs, outputs, logs)
            # storage.setProjectDseRes(id, inputs, outputs)
            files.append({"id": id, "inputs": inputs,
                          "outputs": outputs, "logs": logs})

        return Response({
            "msg": "Concolic testing done successfully",
            "files": files
        })

    def postProgramPairing(self, request):
        serializer = ProgramPairingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        options = serializer.validated_data

        refId = options['id']

        storage = Storage()
        refProject = storage.getProjectById(refId)
        entry = storage._getEntryById(refId)
        projects = storage.getProjectsByEntry(entry)

        pairProgram(refId, projects)

        return Response({"msg": "Program pairing done successfully"})

    def postRandomSampling(self, request):
        serializer = RandomSampling(data=request.data)
        serializer.is_valid(raise_exception=True)
        options = serializer.validated_data
        low = options['low']
        high = options['high']
        size = options['size']
        entry = options['entry']

        storage = Storage()

        projects = storage.getProjectsByEntry(entry)
        refId = storage.getRefIdByEntry(entry)
        refProject = storage.getProjectById(refId)

        rsRes = {}
        for id in projects:
            project = projects[id]
            if project['isReference']:
                continue
            inpAr = generateRandomInput(
                low, high, size, len(project['params']))
            outputs, inputs, numOfAgreedInps = calcNumOfAgreedInputs(
                refId, id, refProject['fileName'], project['fileName'], inpAr, entry)
            agreedInputRate = numOfAgreedInps / size

            rsData = {
                "percent": round((numOfAgreedInps / size) * 100),
                "passed": numOfAgreedInps,
                "all": size,
                "inputs": inputs,
                "outputs": outputs
            }

            storage.setMetric(id, 'rs', rsData)

            rsRes[id] = rsData

        data = {
            "entry": entry,
            "name": "rs",
            "data": rsRes
        }

        return Response({
            "msg": "RS calc done successfully",
            "data": data
        })

    def postRef(self, request):
        id = request.data['id']
        storage = Storage()
        storage.chooseAsRef(id)

        return Response({
            "msg": "The project is chosen as reference successfully",
            "id": id
        })

    def get(self, request):
        id = request.GET['id']
        storage = Storage()
        project = storage.getProjectById(id)
        fileName = project['fileName']

        file_path = os.path.join(
            STATIC_FILES / id, fileName + '.py.dot.png')
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="image/png")
                response['Content-Disposition'] = 'inline; filename=' + \
                    os.path.basename(file_path)
                return response
        raise Http404
