from src.abstract_classes import API


class SuperJobAPI(API):
    """Класс для получения информации из API сайта superjob.ru """

    def __init__(self):
        pass

    def get_vacancies(self):
        pass

    def format_data(self, data: list) -> list:
        pass

    def add_profession(self, value: str) -> None:
        pass
