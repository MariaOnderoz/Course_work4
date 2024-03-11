from abc import ABC, abstractmethod

class GetVacancies(ABC):
    """Абстрактный класс для получения вакансий"""

    @abstractmethod
    def get_vacancies(self, name_job, pages):
        pass


class JSONABCSaver(ABC):
    """Абстрактный класс, который реализует методы для добавления вакансий в файл,
    получения данных из файла по указанным критериям"""

    @abstractmethod
    def add_to_file(self):
        pass

    @abstractmethod
    def get_from_file(self):
        pass

