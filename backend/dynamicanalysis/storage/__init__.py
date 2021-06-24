from dynamicanalysis.settings import STATIC_FILES, STORAGE_JSON
import json


class Storage(object):
    def __init__(self):
        with open(STORAGE_JSON) as storageJson:
            self.storage = json.load(storageJson)

    def addProjects(self, entry, newProjects):
        if entry in self.storage:
            projects = self.storage.get(entry)
            projects.update(newProjects)
        else:
            self.storage[entry] = newProjects
        self._save()

    def deleteProject(self, id):
        entry = self._getEntryById(id)
        del self.storage[entry][id]
        if not bool(self.storage[entry]):
            del self.storage[entry]
        self._save()

    def chooseAsRef(self, id):
        entry = self._getEntryById(id)

        for idx in self.storage[entry]:
            self.storage[entry][idx]['isReference'] = False

        self.storage[entry][id]['isReference'] = True
        self._save()

    def getProjectById(self, id):
        entry = self._getEntryById(id)
        return self.storage[entry][id]

    def getProjectsByEntry(self, entry):
        return self.storage[entry]

    def getRefIdByEntry(self, entry):
        for id in self.storage[entry]:
            if (self.storage[entry][id]['isReference']):
                return id
        return None

    def setAsReference(self, id):
        entry = self._getEntryById(id)
        self.storage[entry][id]['isReference'] = True
        self._save()

    def setMetric(self, id, type, data):
        entry = self._getEntryById(id)
        self.storage[entry][id]['metrics'][type] = data
        self._save()

    def setProjectDseRes(self, id, inputs, outputs, logs):
        # def setProjectDseRes(self, id, inputs, outputs):
        project = self.getProjectById(id)
        project['inputs'] = inputs
        project['outputs'] = outputs
        project['logs'] = logs
        self._save()

    def updateProjectCode(self, id, code):
        project = self.getProjectById(id)
        project['code'] = code
        project['metrics'] = {"pse": 0, "sse": 0, "rs": 0, "cvg": 0}
        project['isReference'] = False
        self._save()

    def markActive(self, id):

        entry = self._getEntryById(id)
        projects = self.getProjectsByEntry(entry)
        for idx in projects:
            if 'isActive' in projects[idx]:
                projects[idx]['isActive'] = False
            if id == idx:
                projects[idx]['isActive'] = True

        self._save()

    def setProjectPseRes(self, id, inputs, outputs):
        project = self.getProjectById(id)
        project['metrics']['pse'] = {"input": inputs, "output": outputs}
        self._save()

    def _getEntryById(self, id):
        for entry in self.storage:
            if id in self.storage[entry]:
                return entry
        return None

    def _save(self):
        with open(STORAGE_JSON, 'w') as storage:
            json.dump(self.storage, storage)
