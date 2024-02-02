from dynamic_array import Dynamic_array

class Queue:
    def __init__(self):
        self.data = Dynamic_array()

    def push(self, value):
        self.data.push_back(value)

    def pop(self):
        if not self.data:
            raise ValueError("Can't pop element. Queue is empty.")
        self.data.pop_front()


    def head(self):
        if not self.data:
            raise ValueError("Queue is empty.")
        return self.data.data[0]

    def tail(self):
        if not self.data:
            raise ValueError("Queue is empty.")
        return self.data[-1]

    def isEmpty(self):
        return self.data.size == 0

    def size(self):
        return self.data.size
        