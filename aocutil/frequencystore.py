import bisect

class FrequencyStore:
    def __init__(self):
        self.values = []
        self.frequencies = []

    def insert(self, value):
        if len(self.values) == 0:
            self.values.insert(0, value)
            self.frequencies.insert(0, 1)
            return

        index = bisect.bisect_left(self.values, value)
        if index >= len(self.values):
            self.values.append(value)
            self.frequencies.append(1)
        elif self.values[index] != value:
            self.values.insert(index, value)
            self.frequencies.insert(index, 1)
        else:
            self.frequencies[index] += 1

    def get_frequencies(self):
        return self.frequencies
