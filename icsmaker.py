import csv


class Ics:
    def __init__(self, agents):
        self.agents = agents

    @staticmethod
    def from_csv(filepath):
        with open(filepath, "r") as f:
            reader = csv.reader(f)
            first_row = next(reader)
            agents = tuple(first_row[2:])
            for row in reader:
                pass
            return Ics(agents)
