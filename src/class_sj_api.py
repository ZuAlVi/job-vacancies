import copy
import os

import requests

from src.abstract_classes import API


class SuperJobAPI(API):
    """Класс для получения информации из API сайта superjob.ru """

    __SJ_API_URL = 'https://api.superjob.ru/2.0/vacancies/'
    __SJ_API_KEY = os.getenv('SECRET_KEY')

    param_default = {
        'count': 50,
        'town': 'Москва',
        'period': 7,
    }

    def __init__(self):
        self.param = copy.deepcopy(self.param_default)

    def get_vacancies(self):
        """Получение информации о вакансиях с помощью параметров.
                :return: list или None"""

        headers = {'X-Api-App-Id': self.__SJ_API_KEY}

        response = requests.get(self.__SJ_API_URL, headers=headers, params=self.param)
        if response.status_code == 200:
            return response.json()['objects']
        else:
            return None

    def format_data(self, data: list) -> list:
        pass

    def add_profession(self, value: str) -> None:
        pass
