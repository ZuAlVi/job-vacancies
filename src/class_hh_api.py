import copy

import requests

from src.abstract_classes import API
from src.class_vacancy import Vacancy


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
        """Получение информации по API о вакансиях с помощью параметров.
                :return: list или None"""
        response = requests.get(self.__HH_API_URL, params=self.param)
        if response.status_code == 200:
            return response.json()['items']
        else:
            return None

    def add_profession(self, value: str) -> None:
        """Метод для добавления параметра 'text' в param."""
        self.param['text'] = value
        Vacancy.request_text = value

    def format_data(self, data: list) -> list:
        work_data = []
        for item in data:
            match item['salary']['currency']:
                case 'USD':
                    if item['salary']['from'] is None:
                        salary = int(item['salary']['to']) * 100
                        salary_currency = 'руб'
                    else:
                        salary = item['salary']['from'] * 100
                        salary_currency = 'руб'
                case 'EUR':
                    if item['salary']['from'] is None:
                        salary = int(item['salary']['to']) * 107
                        salary_currency = 'руб'
                    else:
                        salary = item['salary']['from'] * 107
                        salary_currency = 'руб'
                case 'RUR':
                    if item['salary']['from'] is None:
                        salary = int(item['salary']['to'])
                        salary_currency = 'руб'
                    else:
                        salary = item['salary']['from']
                        salary_currency = 'руб'

            work_dict = {'name': item['name'],
                         'requirement': item['snippet']['requirement'],
                         'responsibility': item['snippet']['responsibility'],
                         'salary': salary,
                         'salary_currency': salary_currency,
                         'url': item['apply_alternate_url'],
                         'employer': item['employer']['name']
                         # 'date_published': date_published,
                         }
            work_data.append(work_dict)
        return work_data
