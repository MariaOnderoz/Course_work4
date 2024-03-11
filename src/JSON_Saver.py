from src.Vacancy import Vacancy, Vacancies
from src.ABC_classes import JSONABCSaver
import json

class JSONSaver(Vacancies, JSONABCSaver):
    """Класс для сохранения информации о вакансиях в JSON-файл"""

    def add_to_file(self):
        with open('vacancies.json', 'w', encoding='utf-8') as file:
            json.dump(self.to_list_dict(), file, indent=4, ensure_ascii=False)

    def get_from_file(self):
        with open('vacancies.json', 'r', encoding='utf-8') as file:
            list_dict = json.load(file)
            self.__all_vacancies = []
            for i in list_dict:
                self.all_vacancies.append(Vacancy.from_dict(i))