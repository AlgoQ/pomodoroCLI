import json

class JsonHandler:
    def __init__(self, path):
        self.path = path
    
    def jsonReader(self):
        with open(self.path, "r") as jsonFile:
            data = json.load(jsonFile)

        return data
    
    def overwriteJson(self, data):
        with open(self.path, "w") as jsonFile:
            json.dump(data, jsonFile)