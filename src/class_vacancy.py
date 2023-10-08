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
