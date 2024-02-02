from dynamic_array import Dynamic_array

class Stack:
    def __init__(self):
        self.data = Dynamic_array()

    def push(self, value):
        self.data.push_back(value)

    def pop(self):
        if self.data:
            self.data.pop_back()
        else:
            raise ValueError("Can't pop element. Stack is empty.")

    def top(self):
        if self.data.size == 0:
            raise ValueError("Stack is empty.")
        return self.data.data[self.data.size - 1]

    def isEmpty(self):
        return self.data.size == 0

    def size(self):
        return self.data.size


    def __getitem__(self, key):
        raise TypeError("Stack object is not subscriptable")
    def __str__(self):
        if self.data.size == 0:
            res = 'Empty Stack. '
        else:
            res = ''
            for i in range(self.data.size):
                res += str(self.data.data[i]) + ' '
        return f'Size: {self.size}. Capacity: {self.capacity}. Data: {res}'

try:
    s = Stack()
    s.push(10)
    s.push(5)
    s.pop()
    print(s.top())
    s.push(6)
    s.push(7)
    s.pop()
    # print(s[1])
except ValueError as ve:
    print(str(ve))
except TypeError as te:
    print(str(te))

