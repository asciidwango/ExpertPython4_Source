class Aggregator:
    def __init__(self):
        self.all_aggregated = []
        self.last_aggregated = None

    def aggregate(self, value):
        self.last_aggregated = value
        self.all_aggregated.append(value)