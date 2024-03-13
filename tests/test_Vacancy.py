import pytest
from src.Vacancy import Vacancy


@pytest.fixture
def v():
    v = Vacancy("Ведущий программист 1С (Москва)",
                "https://hh.ru/vacancy/94212812",
                460000,
                517000,
                "Полная занятость",
                "Москва"
                )
    return v


def test__init__(v):
    assert v.name == "Ведущий программист 1С (Москва)"
    assert v.url == "https://hh.ru/vacancy/94212812"
    assert v.salary_from == 460000
    assert v.salary_to == 517000
    assert v.employment == "Полная занятость"
    assert v.city == "Москва"
