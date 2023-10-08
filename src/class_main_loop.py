from src.class_hh_api import HeadHunterAPI
from src.class_json_saver import JSONSaver
from src.class_sj_api import SuperJobAPI
from src.class_vacancy import Vacancy


class MainLoop:
    """Этот класс предназначен для взаимодействия
     с пользователем в консоли."""

    def __init__(self):
        self.hh_api = HeadHunterAPI()
        self.sj_api = SuperJobAPI()

    def start_loop(self) -> None:
        """Метод начального меню приложения."""
        while True:
            print('~' * 118)
            print('Добро пожаловать в приложение по поиску вакансий.')
            print('Доступные команды:')
            print('0 - Выход.')
            print('1 - Поиск вакансий на платформе HeadHunter.')
            print('2 - Поиск вакансий на платформе SuperJob.')
            print()
            choice = input('Введите команду: ')
            match choice:
                case '0':
                    print()
                    print('До свидания.')
                    quit()
                case '1':
                    print('~' * 118)
                    hh_choice = 'hh'
                    self.choice_profession(hh_choice)
                case '2':
                    print('~' * 118)
                    sj_choice = 'sj'
                    self.choice_profession(sj_choice)
                case _:
                    print('~' * 118)
                    print('Неизвестная команда.')

    def choice_profession(self, value: str) -> None:
        """Меню выбора профессии для поиска на сайте"""
        while True:
            print('Доступные команды:')
            print('0 - Выход.')
            print('1 - Вернуться в предыдущее меню.')
            user_input = input('Введите профессию для поиска или доступную команду: ').lower().strip()
            match user_input:
                case '0':
                    print('До свидания.')
                    quit()
                case '1':
                    return
                case _:
                    if value == 'hh':
                        self.hh_api.add_profession(user_input)
                        self.average_loop(value)
                    if value == 'sj':
                        self.sj_api.add_profession(user_input)
                        self.average_loop(value)

    def average_loop(self, value: str) -> None:
        """Метод промежуточного меню приложения."""
        while True:
            print('~' * 118)
            print('Доступные команды:')
            print('0 - Выход.')
            print('1 - Показать все вакансии.')
            print('2 - Показать топ 10 вакансий по зарплате.')
            print('3 - Вернуться в предыдущее меню.')
            user_input = input('Введите команду: ')
            match user_input:
                case '0':
                    print('До свидания.')
                    quit()
                case '1':
                    if value == 'hh':
                        print('~' * 118)
                        hh_data = self.hh_api.get_vacancies()
                        if hh_data is None:
                            print('Ошибка получения данных')
                            return
                        hh_work_data = self.hh_api.format_data(hh_data)
                        self.get_all_vacancies(hh_work_data)
                    if value == 'sj':
                        print('~' * 118)
                        sj_data = self.sj_api.get_vacancies()
                        if sj_data is None:
                            print('Ошибка получения данных')
                            return
                        sj_work_data = self.sj_api.format_data(sj_data)
                        self.get_all_vacancies(sj_work_data)
                case '2':
                    if value == 'hh':
                        print('~' * 118)
                        hh_data = self.hh_api.get_vacancies()
                        if hh_data is None:
                            print('Ошибка получения данных')
                            return
                        hh_work_data = self.hh_api.format_data(hh_data)
                        sorted_data = sorted(hh_work_data, key=lambda x: x['salary'], reverse=True)
                        self.get_top_10_by_salary(sorted_data)
                    if value == 'sj':
                        print('~' * 118)
                        sj_data = self.sj_api.get_vacancies()
                        if sj_data is None:
                            print('Ошибка получения данных')
                            return
                        sj_work_data = self.sj_api.format_data(sj_data)
                        sorted_data = sorted(sj_work_data, key=lambda x: x['salary'], reverse=True)
                        self.get_top_10_by_salary(sorted_data)
                case '3':
                    Vacancy.clear_vacancies_list()
                    print('~' * 118)
                    return
                case _:
                    print('~' * 118)
                    print('Неизвестная команда.')

    def get_all_vacancies(self, data):
        """Метод вывода всех найденных вакансий с помощью класса Vacancy"""
        for part in data:
            Vacancy(part)
        work_list = Vacancy.all_vacancies
        for index in range(len(work_list)):
            print(f'Вакансия № {index + 1}.')
            work_list[index].get_info()
        self.last_loop(work_list)

    def get_top_10_by_salary(self, data):
        """Метод вывода топ 10 по зарплате вакансий с помощью класса Vacancy"""
        for part in data[:10]:
            Vacancy(part)
        work_list = Vacancy.all_vacancies
        for index in range(len(work_list)):
            print(f'Вакансия № {index + 1}.')
            work_list[index].get_info()
        self.last_loop(work_list)

    def last_loop(self, data):
        """Метод конечного меню приложения."""
        while True:
            print('~' * 118)
            print(f'Показано {len(data)} вакансий по запросу "{Vacancy.request_text.title()}".')
            print()
            print('Доступные команды:')
            print('0 - выход без сохранения в файл.')
            print('1 - сохранить в файл и выйти.')
            print('2 - начать новый поиск.')
            user_input = input('Введите команду: ')
            match user_input:
                case '0':
                    print('До свидания.')
                    quit()
                case '1':
                    data = Vacancy.reformat_data()
                    saver = JSONSaver()
                    try:
                        saver.save_file(data)
                        print('Данные успешно сохранены.')
                        print()
                        print('До свидания.')
                        quit()
                    except FileNotFoundError:
                        print('Неверный путь к файлу')
                        continue
                case '2':
                    Vacancy.clear_vacancies_list()
                    self.start_loop()
                case _:
                    print('~' * 118)
                    print('Неизвестная команда.')
