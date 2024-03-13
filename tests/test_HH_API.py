import pytest
from src.Vacancy import Vacancy
from abc import ABC
from src.ABC_classes import GetVacancies
from src.HH_API import HeadHunterAPI


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


def test_issubclass():
    assert issubclass(GetVacancies, ABC)
    assert issubclass(HeadHunterAPI, GetVacancies)
