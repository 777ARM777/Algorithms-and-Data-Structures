from Location import Location


class Table:
    def __init__(self, base):
        self.table = [[None for _ in range(base)] for __ in range(base)]

        e_tmp = {}
        for i in range(1, base + 1):
            e_tmp[i] = i
        e = Location(e_tmp)

        for i in range(base):
            for j in range(i):
                self.table[i][j] = None
            self.table[i][i] = e
