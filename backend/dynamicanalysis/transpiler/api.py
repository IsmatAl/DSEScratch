from .serializers import FileUploadSerializer, PythonConversionSerializer
from rest_framework import viewsets
from rest_framework.response import Response
import sys
import os
from dynamicanalysis.settings import STATIC_FILES, STORAGE_JSON
from dse.api import pairProgram
from .python.PrintPythonCode import parse
from utils import pathTo, stripExt
from storage import Storage
from shutil import rmtree
import uuid
import json


class TransplileAPI(viewsets.GenericViewSet):

    serializer_class = PythonConversionSerializer

    def postUploadFile(self, request):
        serializer = FileUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        files = serializer.validated_data['files']
        entry = serializer.validated_data['entry']

        fileNames = []
        for file in files:
            id = str(uuid.uuid4())
            fileName = file.name
            handle_uploaded_file(file, id)
            fileNames.append({"id": id, "fileName": stripExt(fileName)})

        files = transpileFiles(fileNames, entry)

        storage = Storage()
        storage.addProjects(entry, files)

        refId = storage.getRefIdByEntry(entry)
        if (refId != None):
            refProject = storage.getProjectById(refId)

            pairProgram(refId, storage.getProjectsByEntry(entry))

        return Response({
            "msg": "File converted successfuly",
            "task": {"entry": entry, "files": files}
        })

    def deleteFile(self, request):
        id = request.GET['id']
        rmtree(str(STATIC_FILES) + '//' + id)

        storage = Storage()
        storage.deleteProject(id)

        return Response({"msg": "File deleted successfully"})

    def getFiles(self, request):
        with open(STORAGE_JSON) as storage:
            
            data = json.load(storage)
            response = Response(data)
            return response

    def postCode(self, request):
        storage = Storage()
        id = request.data['id']
        project = storage.getProjectById(id)
        fileName = project['fileName']
        code = request.data['code']
        convertedFile = os.path.join(
            STATIC_FILES / id,  (fileName + '.py'))

        with open(convertedFile, 'w') as f:
            f.write(code)

        if fileName in sys.modules:
            del(sys.modules[fileName])

        storage.updateProjectCode(id, code)

        return Response({"msg": "File updated successfully"})

    def postActiveFile(self, request):
        storage = Storage()
        id = request.data['id']
        storage.markActive(id)
        return Response({"msg": "File updated successfully"})


def transpileFiles(fileNames, entry):
    files = {}
    for fileNameObj in fileNames:
        id = fileNameObj['id']
        fileName = fileNameObj['fileName']
        _, convPyCode, functionAttributes = convertToPy(id, fileName)
        files[id] = {
            "fileName": fileName,
            "entry": entry,
            "params": functionAttributes,
            "code": convPyCode,
            "metrics": {
                "pse": 0,
                "sse": 0,
                "rs": 0,
                "cvg": 0
            },
            "isReference": False
        }

    return files


def handle_uploaded_file(f, id):
    path = pathTo(f.name, id)
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def convertToPy(id, fileName):
    convertedPyCode, functionAttributes = parse(
        STATIC_FILES / id / (fileName + '.json'))
    convertedFile = os.path.join(
        STATIC_FILES / id,  (fileName + '.py'))

    with open(convertedFile, 'w') as f:
        f.write(convertedPyCode)

    if fileName in sys.modules:
        del(sys.modules[fileName])
    return convertedFile, convertedPyCode, functionAttributes
