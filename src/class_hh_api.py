import copy

from src.abstract_classes import API


class HeadHunterAPI(API):
    """Класс для получения информации из API сайта headhunter.ru """

    __HH_API_URL = 'https://api.hh.ru/vacancies'

    param_default = {
        'per_page': 50,
        'area': 1,
        'date': 7,
        'only_with_salary': True
    }

    def __init__(self):
        self.param = copy.deepcopy(self.param_default)

    def get_vacancies(self):
        pass

    def add_profession(self, value):
        pass

    def format_data(self, data):
        pass