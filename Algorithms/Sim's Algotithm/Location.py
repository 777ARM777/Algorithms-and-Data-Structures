class Location:
    def __init__(self, loc: dict):
        self.loc = loc

    def __mul__(self, other):
        if len(self) != len(other):
            raise ValueError("Length of locations must be equal.")

        loc = {}
        for i in self.loc.keys():
            loc[i] = other.loc[self.loc[i]]
        return Location(loc)

    def reverse(self):
        res = {}
        for i in self.loc.keys():
            res[self.loc[i]] = i
        return res

    def __len__(self):
        return len(self.loc)

    def __str__(self):
        return f'{[i for i in self.loc.values()]}'
