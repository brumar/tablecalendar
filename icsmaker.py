import csv


class AgentEvents:
    def __init__(self):
        self.events = []


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
            for row in reader:
                pass
            return Ics(agents)

    def __getitem__(self, item):
        return self.agents_dict[item]
