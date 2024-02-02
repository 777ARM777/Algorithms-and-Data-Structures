class Dynamic_array:
    def __init__(self):
        self.data = []
        self.size = 0
        self.capacity = 0

    def push_back(self, value):
        if self.size == 0 or self.size == self.capacity:
            self.shrink()
        self.data[self.size] = value
        self.size += 1

    def push_front(self, value):
        if self.size == 0 or self.size == self.capacity:
            self.shrink()

        for i in range(self.size, 0, -1):
            self.data[i] = self.data[i - 1]
        self.size += 1
        self.data[0] = value

    def pop_back(self):
        if self.size == 0:
            raise IndexError('Cannot pop from empty array.')
        self.size -= 1
        if self.size < self.capacity // 2:
            self.capacity //= 2

    def pop_front(self):
        if self.size == 0:
            raise IndexError('Cannot pop from empty array.')
        for i in range(self.size - 1):
            self.data[i] = self.data[i + 1]
        self.size -= 1
        if self.size < self.capacity // 2:
            self.capacity //= 2

    def insert(self, value, index):
        if index < 0:
            raise IndexError('List index out of range.')
        if index == 0:
            self.push_front(value)
        elif index >= self.size:
            self.push_back(value)
        else:
            if self.size == 0 or self.size == self.capacity:
                self.shrink()
            for i in range(self.size, index, -1):
                self.data[i] = self.data[i - 1]
            self.data[index] = value
            self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('List index out of range.')
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.size -= 1
        if self.size < self.capacity // 2:
            self.capacity //= 2

    def shrink(self):
        if self.capacity == 0:
            self.capacity = 1
            self.data = [None]
        else:
            self.data = self.data + [None for _ in range(self.size)]
            self.capacity *= 2

    def resize(self, size, value):
        if size == self.size:
            return
        elif size <= 0:
            self.capacity = 1
            self.size = 0
            self.data = []
            return
        elif size < self.size:
            if self.size < self.capacity // 2:
                self.capacity //= 2
        else:
            if size > self.capacity:
                self.capacity = size * 2
            self.data = self.data[:self.size] + [value for _ in range(size - self.size)]
        self.size = size




    def search(self, value):
        for i in self.data:
            if i == value:
                return True
        return False

    def __str__(self):
        if self.size == 0:
            res = 'Empty List. '
        else:
            res = ''
            for i in range(self.size):
                res += str(self.data[i]) + ' '
        return f'Size: {self.size}. Capacity: {self.capacity}. List: {res}'

if __name__ == '__main__':
    try:
        da = Dynamic_array()
        print(da)
        da.push_front(5)
        print(da)
        da.push_back(4)
        print(da)
        da.push_front(6)
        print(da)
        da.push_front(9)
        print(da)

        da.insert(15, 2)
        print(da)

        da.delete(3)
        print(da)
        # da.delete(2)
        # print(da)
        # da.delete(1)
        # print(da)
        # da.delete(0)
        # print(da)
        # da.delete(0)
        # print(da)

        print(da.search(12))
        print(da.search(15))

        da.resize(0, 2)
        print(da)

        # da.pop_back()
        # print(da)
        # da.pop_back()
        # print(da)
        # da.pop_back()
        # print(da)
        # da.pop_back()
        # print(da)

    except IndexError as ie:
        print(str(ie))
