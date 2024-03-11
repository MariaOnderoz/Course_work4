import json

def test_add_to_file(self):
    with open('vacancies.json', 'w', encoding='utf-8') as file:
        json.dump(self, file, indent=4, ensure_ascii=False)
    assert file == {
        "name": "Ведущий программист 1С (Москва)",
        "city": "Москва",
        "salary_from": 460000,
        "salary_to": 517000,
        "employment": "Полная занятость",
        "url": "https://hh.ru/vacancy/94212812"
    }
