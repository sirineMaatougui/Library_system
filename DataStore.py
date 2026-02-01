import json
import os

class DataStore:
    FILE_NAME = "library_data.json"

    @staticmethod
    def load():
        # AUTOLOAD
        if not os.path.exists(DataStore.FILE_NAME):
            data = {"items": [], "members": []}
            DataStore.save(data)  # crée le fichier direct
            return data

        with open(DataStore.FILE_NAME, "r") as f:
            return json.load(f)

    @staticmethod
    def save(data):
        # AUTOSAVE
        with open(DataStore.FILE_NAME, "w") as f:
            json.dump(data, f, indent=4)
