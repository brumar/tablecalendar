from icsmaker import EventCsvParser, AgentEvents, Event, EventsIcs
from datetime import date
from pytest import fixture
from typing import Iterator
from typing import Union


@fixture(name="cal_ics")
def cal_ics() -> Iterator[Union[Iterator, Iterator[EventCsvParser]]]:
    yield EventCsvParser.from_csv("./tests/fixture_1.csv")


def test_ft_parsing(cal_ics: EventCsvParser) -> None:

    assert len(cal_ics["CLEMENT"].events) == 2
    assert cal_ics["CLEMENT"][0].day == date(2019, 11, 23)
    assert cal_ics["CLEMENT"][0].txt_shift == "9h30-13h30"


def test_ut_get_list_agents(cal_ics: EventCsvParser) -> None:

    assert cal_ics.agents == ("MARIE", "JOE", "CLEMENT", "TOM")


def test_ut_get_agent(cal_ics: EventCsvParser) -> None:
    assert isinstance(cal_ics["MARIE"], AgentEvents)


def test_ut_agent_with_no_event(cal_ics: EventCsvParser) -> None:
    assert cal_ics["TOM"].events == []


def test_ut_create_event() -> None:
    event = Event.from_rawstrings(day="22/11/2019", shift="8h-9h30")
    assert event.day == date(2019, 11, 22)
    assert event.txt_shift == "8h-9h30"


def test_ut_gen_ics(cal_ics: EventCsvParser) -> None:
    eics = EventsIcs(cal_ics)
    eics.create_calendar()

    assert len(eics.get_calendar().events) == 5


def test_ut_gen_ics_orgs(cal_ics: EventCsvParser) -> None:
    eics = EventsIcs(cal_ics)
    eics.create_calendar()

    s = set()

    for e in eics.get_calendar().events:
        s.add(e.organizer)

    assert "MARIE" in s
    assert "JOE" in s
    assert "CLEMENT" in s
