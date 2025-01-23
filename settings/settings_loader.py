import json

from settings.models import AppSettings


class SettingsLoader:
    def __init__(self):
        self.file_name = 'app_settings.json'
        self.app_settings = None

        self.load_config()

    @staticmethod
    def load_json(path):
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def load_config(self):
        data = self.load_json(self.file_name)

        self.app_settings = AppSettings(**data)


loader = SettingsLoader()
db_settings = loader.app_settings.db_settings
uvicorn_settings = loader.app_settings.uvicorn_settings
