from __future__ import annotations
import csv
from datetime import datetime, date
from typing import Any
from typing import Optional
from typing import Tuple
from _csv import reader
from typing import Iterator
from typing import List


class Event:
    def __init__(self, day: date, shift: str) -> None:
        self.day = day
        self.txt_shift = shift

    @staticmethod
    def from_rawstrings(day: str, shift: str) -> Event:
        d = datetime.strptime(day, "%d/%m/%Y")
        d = date(d.year, d.month, d.day)
        return Event(day=d, shift=shift)


class AgentEvents:
    def __init__(self, events: Optional[Any] = None) -> None:
        self.events = events if events is not None else []

    def __getitem__(self, item):
        # type: (int) -> Event
        return self.events[item]


class EventCsvParser:
    def __init__(self, agents: Tuple[str, str, str, str]) -> None:
        self.agents = agents
        self.agents_dict = {ag: AgentEvents() for ag in self.agents}

    @staticmethod
    def from_csv(filepath: str) -> EventCsvParser:
        with open(filepath, "r") as f:
            reader = csv.reader(f)
            first_row = next(reader)
            agents = tuple(first_row[2:])
            ics = EventCsvParser(agents)
            ics.add_events_from_csvreader(reader)
            return ics

    def add_events_from_csvreader(self, reader: reader) -> None:
        for row in reader:
            event = Event.from_rawstrings(row[0], row[1])
            agents = self.get_agents_from_row(row[2:])
            self.add_event_to_agents(agents, event)

    def add_event_to_agents(self, agents: Iterator, event: Event) -> None:
        for agent in agents:
            self[agent].events.append(event)

    def get_agents_from_row(self, x_list: List[str]) -> Iterator[str]:
        for agent, cell in zip(self.agents, x_list):
            if cell == "x":
                yield agent

    def __getitem__(self, item: str) -> AgentEvents:
        return self.agents_dict[item]
