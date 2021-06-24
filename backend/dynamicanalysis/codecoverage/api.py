import coverage
import importlib
from .serializers import CodeCoverageSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpResponse
from dynamicanalysis.settings import BASE_DIR, STATIC_FILES
from utils import getFunc
from storage import Storage
import logging
from coverage.report import get_analysis_to_report


def calcCoverage(id, project):
    inputs = project['inputs']
    fileName = project['fileName']
    entry = project['entry']
    cov = coverage.Coverage(omit=(str(BASE_DIR) + '\\dse\\*'))
    cov.start()
    func, mod = getFunc(id, fileName, entry)

    for input in inputs:
        func(*input)

    cov.stop()
    cov.save()
    json = generateCoverageReportJsonObject(cov, mod)
    cov.json_report(
        outfile=(STATIC_FILES / id / (fileName + '_' + entry + '_coverage.json')))
    return json


def generateCoverageReportJsonObject(cov, module):
    _, stmts, excluded, missed, _ = cov.analysis2(
        module)
    executed = list(set(stmts).union(excluded).difference(missed))
    if executed == excluded:
        executed = []
    covered = list(set(stmts).difference(missed))
    total = list(stmts)
    total.sort()
    total_count = len(total)
    coveredLines = len(covered)
    excluded_count = len(excluded)
    missed_count = len(missed)
    try:
        percent_covered = round(float(len(covered))/len(stmts)*100)
    except ZeroDivisionError:
        percent_covered = 100
    return {
        "executed_lines": executed,
        "summary": {
            "covered_lines": coveredLines,
            "num_statements": total_count,
            "percent_covered": percent_covered,
            "missing_lines": missed_count,
            "excluded_lines": excluded_count
        },
        "missing_lines": missed,
        "excluded_lines": excluded
    }


def calcSSE(id, pyFileName, expectedOutputs, entry, inputs):
    func, _ = getFunc(id, pyFileName, entry)

    numOfCorrOutput = 0
    outputs = []
    for idx in range(len(inputs)):
        output = func(*inputs[idx])
        outputs.append(output)
        if expectedOutputs[idx] == output:
            numOfCorrOutput += 1
    return {
        "percent": round((numOfCorrOutput / len(expectedOutputs)) * 100),
        "passed": numOfCorrOutput,
        "all": len(expectedOutputs),
        "inputs": inputs,
        "refOutputs": expectedOutputs,
        "outputs": outputs,
    }


class CodeCoverageAPI(viewsets.GenericViewSet):

    serializers = CodeCoverageSerializer

    def postCoverage(self, request):
        serializer = CodeCoverageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        entry = serializer.validated_data['entry']

        storage = Storage()

        projects = storage.getProjectsByEntry(entry)

        cvgData = {}

        for id in projects:

            project = projects[id]

            try:
                covgJson = calcCoverage(id, project)
                cvgData[id] = covgJson
                storage.setMetric(id, 'cvg', covgJson)
            except AttributeError as e:
                logging.exception(e)
                return HttpResponse({"error": e})

        cvgRes = {"entry": entry, "name": "cvg", "data": cvgData}

        return Response({
            "msg": "Code coverage done successfuly",
            "data": cvgRes
        })

    def postSSE(self, request):
        # serializer = CodeCoverageSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)

        storage = Storage()
        entry = request.data['entry']
        refId = request.data['refId']
        # expectedOutputs = serializer.validated_data['expectedOutputs']
        # pyFileName = serializer.validated_data['pyFileName']
        # entry = serializer.validated_data['entry']

        projects = storage.getProjectsByEntry(entry)
        refProject = storage.getProjectById(refId)

        idToSse = {"entry": entry, "name": "sse"}
        data = {}
        for id in projects:
            project = projects[id]
            if project['isReference']:
                continue

            sse = calcSSE(id, project['fileName'], refProject['outputs'],
                          project['entry'], refProject['inputs'])
            storage.setMetric(id, 'sse', sse)
            data[id] = sse
        idToSse['data'] = data
        return Response({"data": idToSse, "msg": "Single-program Symbolic Execution done successfuly"})
