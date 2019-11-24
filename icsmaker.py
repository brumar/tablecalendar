import csv


class Ics:
    def __init__(self, agents):
        self.agents = agents

    @staticmethod
    def from_csv(filepath):
        with open(filepath, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                agents = tuple(row[2:])
                return Ics(agents)
