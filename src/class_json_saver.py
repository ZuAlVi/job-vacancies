import json

from src.abstract_classes import Saver


class JSONSaver(Saver):
    """Класс для сохранения информации в файлы формата json"""

    def __init__(self, path='data/vacancies_data.json'):
        self.path = path

    def save_file(self, data: list):
        """Метод сохранения данных в файл"""
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)
