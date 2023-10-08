class Vacancy:
    """Класс для работы с вакансиями."""

    all_vacancies = []
    request_text = ''

    def __init__(self, vacancy_data: dict):
        self.name = vacancy_data['name']
        self.requirement = vacancy_data['requirement']
        self.responsibility = vacancy_data['responsibility']
        self.salary = vacancy_data['salary']
        self.salary_currency = vacancy_data['salary_currency']
        self.url = vacancy_data['url']
        self.employer = vacancy_data['employer']

        Vacancy.all_vacancies.append(self)

    def get_info(self) -> None:
        """Метод выводит информацию об экземпляре класса в удобном виде."""
        print('~' * 118)
        print(f'Работодатель: {self.employer[:100]}')
        print(f'Профессия - {self.name}')
        if self.requirement is None:
            print('Требования не указаны.')
        else:
            print(f'Требования - {self.requirement[:100]}...')
        if self.responsibility is None:
            print('Сфера деятельности не указана.')
        else:
            print(f'Сфера деятельности - {self.responsibility[:100]}...')
        print(f'Зарплатные ожидания: {self.salary} {self.salary_currency}.')
        print(f'Ссылка на вакансию - {self.url}')
        print('~' * 118)
        print()

    def __len__(self):
        return len(Vacancy.all_vacancies)

    @classmethod
    def clear_vacancies_list(cls) -> None:
        """Метод для очистки атрибута класса 'all_vacancies'."""
        cls.all_vacancies = []

    @classmethod
    def reformat_data(cls) -> list:
        """Метод для переделки атрибута класса 'all_vacancies'
        в список словарей."""
        reformat_data = []
        for vacancy in cls.all_vacancies:
            reformat_data.append(vacancy.__dict__)
        return reformat_data
