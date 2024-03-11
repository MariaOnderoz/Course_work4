import pytest
from src.Vacancy import Vacancy
from abc import ABC
from src.ABC_classes import GetVacancies
from src.HH_API import HeadHunterAPI


@pytest.fixture
def v():
    v = Vacancy("Ведущий программист 1С (Москва)",
                "Москва",
                460000,
                517000,
                "Полная занятость",
                "https://hh.ru/vacancy/94212812")
    return v


def test_issubclass():
    assert issubclass(GetVacancies, ABC)
    assert issubclass(HeadHunterAPI, GetVacancies)
