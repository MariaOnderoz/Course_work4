import pytest
from src.Vacancy import Vacancy


@pytest.fixture
def v():
    v = Vacancy("Ведущий программист 1С (Москва)",
                "Москва",
                460000,
                517000,
                "Полная занятость",
                "https://hh.ru/vacancy/94212812")
    return v


def test__init__(v):
    assert v.name == "Ведущий программист 1С (Москва)"
    assert v.city == "Москва"
    assert v.salary_from == 460000
    assert v.salary_to == 517000
    assert v.emploeyment == "Полная занятость"
    assert v.url == "https://hh.ru/vacancy/94212812"
