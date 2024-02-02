class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_back(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def push_front(self, value):
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def pop_back(self):
        if self.tail is None:
            raise ValueError('List has no node to pop.')
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def pop_front(self):
        if self.head is None:
            raise ValueError('List has no node to pop.')
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def insert(self, value, index):
        size = self.size()
        if index < 0 or index > size:
            raise IndexError('List index out of range.')

        if index == 0 or self.head is None:
            self.push_front(value)
        elif index == size:
            dll.push_back(value)
        else:
            node = Node(value)
            if index < size // 2:
                current = self.head
                i = 0
                while current.next and i < index - 1:
                    i += 1
                    current = current.next
            else:
                current = self.tail
                i = size
                while current.prev and i > index:
                    i -= 1
                    current = current.prev
            node.next = current.next
            current.next.prev = node
            node.prev = current
            current.next = node

    def delete(self, index):
        size = self.size()
        if self.head is None:
            raise ValueError("Can't delete a node. List has no nodes.")
        if index < 0 or index > size - 1:
            raise IndexError("Can't delete element. List index out of range.")

        if index == 0:
            self.pop_front()
        elif index == size - 1:
            self.pop_back()
        else:
            if index < size // 2:
                current = self.head
                i = 0
                while current.next and i < index - 1:
                    i += 1
                    current = current.next
            else:
                current = self.tail
                i = size
                while current.prev and i > index:
                    i -= 1
                    current = current.prev
            current.next = current.next.next
            current.next.prev = current

    def search(self):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def __str__(self):
        if self.head is None:
            return 'Empty list.'
        s = str(self.head.data)
        current = self.head.next
        while current:
            s += '<->' + str(current.data)
            current = current.next
        return f"DLL: {s}\tsize: {self.size()}"


    def get_middle_node(self):
        if self.head is None:
            raise ValueError("Can't get middle node. List is empty.")
        if self.head.next is None:
            return self.head.data
        current = self.head.next
        prev = self.head
        while current and current.next:
            current = current.next.next
            prev = prev.next
        return prev.data

    def has_cycle(self):
        if self.head is None:
            raise ValueError("Can't check cycles. List is empty.")
        current = self.head
        prev = self.head
        while current:
            current = current.next.next
            prev = prev.next
            if current == prev:
                return True
        return False

    def mergeTwoSortedLinkedLists(self, other):
        if self.head is None and other.head is None:
            raise ValueError("Can't merge empty lists.")
        current1 = self.head
        current2 = other.head
        res = Doubly_linked_list()
        while current1 and current2:
            if current1.data < current2.data:
                res.push_back(current1.data)
                current1 = current1.next
            else:
                res.push_back(current2.data)
                current2 = current2.next

        while current1:
            res.push_back(current1.data)
            current1 = current1.next

        while current2:
            res.push_back(current2.data)
            current2 = current2.next

        return res

if __name__ == '__main__':
    try:
        dll = Doubly_linked_list()
        print(dll)

        dll.push_back(1)
        print(dll)

        dll.pop_front()
        print(dll)

        dll.push_back(3)
        print(dll)

        dll.push_back(5)
        print(dll)

        dll.push_back(7)
        print(dll)

        dll.push_back(9)
        print(dll)

        # dll.insert(10, 4)
        # print(dll)

        dll.delete(4)
        print(dll)


        # print(dll.get_middle_node())

        # dll2 = Doubly_linked_list()
        # print(dll2)
        #
        # dll2.push_back(2)
        # print(dll2)
        #
        # dll2.push_back(4)
        # print(dll2)
        #
        # dll2.push_back(6)
        # print(dll2)
        #
        # dll2.push_back(8)
        # print(dll2)
        #
        # dll2.push_back(10)
        # print(dll2)

        # merged_list = dll2.mergeTwoSortedLinkedLists(dll)
        # print(merged_list)

    except IndexError as ie:
        print(str(ie))

    except ValueError as ve:
        print(str(ve))
