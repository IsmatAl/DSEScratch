import importlib
from dynamicanalysis.settings import STATIC_FILES
import os
from pathlib import Path


def stripExt(fileName):
    return fileName[:fileName.rindex('.')]


def getFunc(id, pyFileName, entry):
    spec = importlib.util.spec_from_file_location(
        "converted", STATIC_FILES / id / (pyFileName + '.py'))
    app = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(app)
    func = getattr(app, entry)
    return func, app


def pathTo(fileName, id=''):
    Path(STATIC_FILES /
         id).mkdir(parents=True, exist_ok=True)
    return os.path.join(STATIC_FILES /
                        id, fileName)
