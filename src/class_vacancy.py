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
