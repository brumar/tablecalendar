from icsmaker import Ics, AgentEvents
from datetime import date
from pytest import fixture


@fixture(name="cal_ics")
def cal_ics():
    yield Ics.from_csv("./tests/fixture_1.csv")


def test_ft_parsing(cal_ics):

    assert len(cal_ics["CLEMENT"].events) == 2
    assert cal_ics["CLEMENT"][0].day == date(2019, 11, 22)
    assert cal_ics["CLEMENT"][0].txt_shift == "8h-9h30"


def test_ut_get_list_agents(cal_ics):

    assert cal_ics.agents == ("MARIE", "JOE", "CLEMENT")


def test_ut_get_agent(cal_ics):
    assert isinstance(cal_ics["MARIE"], AgentEvents)
