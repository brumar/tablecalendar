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
            for row in reader:
                event = Event.from_rawstrings(row[0], row[1])
                for c, cell in enumerate(row[2:]):
                    if cell == "x":
                        agent = ics.agents[c]
                        ics[agent].events.append(event)
            return ics

    def __getitem__(self, item):
        return self.agents_dict[item]
