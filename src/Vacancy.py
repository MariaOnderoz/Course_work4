
class Vacancy:
    """Класс для работы с вакансиями"""

    def __init__(self, name, url, salary_from, salary_to, employment, city):
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.employment = employment
        self.city = city


    def __str__(self):
        return f"Название вакансии: {self.name}\n" \
               f"Ссылка на вакансию: {self.url}\n" \
               f"Заработная плата от: {self.salary_from}\n" \
               f"Заработная плата до: {self.salary_to}\n" \
               f"Описание вакансии: {self.employment}\n" \
               f"Город: {self.city}\n"


    def to_dict(self):
        """Возвращает вакансию в виде словаря"""

        return {
            'name': self.name,
            'url': self.url,
            'salary_from': self.salary_from,
            'salary_to': self.salary_to,
            'employment': self.employment,
            'city': self.city
        }


    @staticmethod
    def from_dict(vacancy_dict):
        """
        Возвращает вакансию в виде списка
        """
        return Vacancy(
            vacancy_dict['name'],
            vacancy_dict['url'],
            vacancy_dict['city'],
            vacancy_dict['salary_from'],
            vacancy_dict['salary_to'],
            vacancy_dict['employment']
        )

    def __lt__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError('Вакансию можно сравнивать только с вакансией')
        return self.salary_from < other.salary_from


class Vacancies:
    """Обработка списка вакансий"""

    def __init__(self):
        self.__all_vacancies = []

    def add_vacancies(self, new_vacancies):
        self.__all_vacancies += new_vacancies

    def delete_vacancies(self, old_vacancies):
        for i in old_vacancies:
            self.__all_vacancies.remove(i)

    def sort_vacancies_by_salary(self):
        self.__all_vacancies.sort(reverse=True)

    @property
    def all_vacancies(self):
        return self.__all_vacancies

    def to_list_dict(self):
        a = []
        for i in self.__all_vacancies:
            a.append(i.to_dict())
        return a


