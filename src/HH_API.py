import requests
from src.Vacancy import Vacancy
from src.ABC_classes import GetVacancies

class HeadHunterAPI(GetVacancies):
    """ Класс для подключения к hh.ru"""

    def get_vacancies(self, name_job, pages):
        hh_list = []
        for i in range(pages):
            params = {
                'text': name_job,
                'per_page': 99,
                'page': i
            }
            response = requests.get('https://api.hh.ru/vacancies', params=params)
            response_json = response.json()
            for j in response_json['items']:
                hh_name = j['name']
                if not (j['area']) is None:
                    hh_city = j['area']['name']
                else:
                    hh_city = None
                if not ((j['salary'] is None) or j['salary']['from'] is None):
                    salary_from = j['salary']['from']
                    salary_to = j['salary']['to']
                else:
                    salary_from = 0
                    salary_to = 0
                hh_employment = j['employment']['name']
                hh_url = j['alternate_url']
                hh_vacancy = Vacancy(hh_name, hh_url, salary_from, salary_to, hh_employment, hh_city)
                hh_list.append(hh_vacancy)
        return hh_list

