import csv
from datetime import datetime, date


class Event:
    def __init__(self, day, shift):
        self.day = day
        self.txt_shift = shift

    @staticmethod
    def from_rawstrings(day, shift):
        d = datetime.strptime(day, "%d/%m/%Y")
        d = date(d.year, d.month, d.day)
        return Event(day=d, shift=shift)


class AgentEvents:
    def __init__(self, events=None):
        self.events = events if events is not None else []

    def __getitem__(self, item):
        return self.events[item]


class Ics:
    def __init__(self, agents):
        self.agents = agents
        self.agents_dict = {ag: AgentEvents() for ag in self.agents}

    @staticmethod
    def from_csv(filepath):
        with open(filepath, "r") as f:
            reader = csv.reader(f)
            first_row = next(reader)
            agents = tuple(first_row[2:])
            ics = Ics(agents)
            ics.add_events_from_csvreader(reader)
            return ics

    def add_events_from_csvreader(self, reader):
        for row in reader:
            event = Event.from_rawstrings(row[0], row[1])
            agents = self.get_agents_from_row(row[2:])
            for agent in agents:
                self[agent].events.append(event)

    def get_agents_from_row(self, x_list):
        for agent, cell in zip(self.agents, x_list):
            if cell == "x":
                yield agent

    def __getitem__(self, item):
        return self.agents_dict[item]
