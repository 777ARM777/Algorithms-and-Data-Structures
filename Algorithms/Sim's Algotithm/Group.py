from Location import Location


class Group:
    def __init__(self, *args) -> None:
        self.group = list(args)

    def __str__(self):
        s = ''
        for i in self.group:
            s += i + '\n'


