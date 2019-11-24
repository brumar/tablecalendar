from icsmaker import Ics
from datetime import date


def test_ft_parsing():
    cal_ics = Ics.from_csv("./tests/fixture_1.csv")

    assert len(cal_ics["CLEMENT"].events) == 2
    assert cal_ics["CLEMENT"][0].day == date(2019, 11, 22)
    assert cal_ics["CLEMENT"][0].txt_shift == "8h-9h30"


def test_ut_get_list_agents():
    cal_ics = Ics.from_csv("./tests/fixture_1.csv")

    assert cal_ics.agents == ("MARIE", "JOE", "CLEMENT")
