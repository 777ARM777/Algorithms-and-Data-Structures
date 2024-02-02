class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Singly_linked_list:
    def __init__(self):
        self.head = None

    def push_back(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = Node(data)
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def push_front(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def pop_back(self):
        if self.head is None:
            raise ValueError('List has no node to pop.')

        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def pop_front(self):
        if self.head is None:
            raise ValueError('List has no node to pop.')

        self.head = self.head.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def insert(self, data, index):
        if index < 0 or index > self.size():
            raise IndexError('List index out of range.')

        if index == 0 or self.head is None:
            self.push_front(data)
        else:
            node = Node(data)
            current = self.head
            i = 0
            while current.next and i < index - 1:
                i += 1
                current = current.next
            node.next = current.next
            current.next = node

    def insert_list(self, pos, singly_linked_list):
        if self.head is None:
            self.head = singly_linked_list.head
            return
        if pos < 0 or pos > self.size():
            raise IndexError("Can't insert list. List index out of range.")
        if singly_linked_list.head is None:
            return

        index = 1
        current = self.head
        while current and index < pos:
            index += 1
            current = current.next

        other_current = singly_linked_list.head
        while other_current.next:
            other_current = other_current.next

        if pos == 0:
            other_current.next = self.head
            self.head = singly_linked_list.head
        else:
            other_current.next = current.next
            current.next = singly_linked_list.head

    def delete(self, index):
        if self.head is None:
            raise ValueError("Can't delete a node. List has no nodes.")
        if index < 0 or index > self.size() - 1:
            raise IndexError("Can't delete element. List index out of range.")

        if index == 0:
            self.pop_front()
        else:
            current = self.head
            i = 1
            while current.next.next and i < index:
                i += 1
                current = current.next
            current.next = current.next.next

    def reverse(self):
        if self.head is None:
            raise ValueError("Can't reverse list. List is empty.")
        current = self.head
        prev = None
        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        self.head = prev

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
        while current and current.next:
            current = current.next.next
            prev = prev.next
            if current == prev:
                return True
        return False

    def get_start_point(self):
        if not self.head or not self.head.next:
            return None
        current = self.head
        prev = self.head
        while current and current.next:
            current = current.next.next
            prev = prev.next
            if current == prev:
                break
        if not current or not current.next:
            return None
        head = self.head
        while prev != head:
            prev = prev.next
            head = head.next
        return head

    def mergeTwoSortedLinkedLists(self, other):
        if self.head is None and other.head is None:
            raise ValueError("Can't merge empty lists.")
        current1 = self.head
        current2 = other.head
        res = Singly_linked_list()
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

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def __str__(self):
        if self.head is None:
            return 'Empty list'
        s = str(self.head.data)
        current = self.head.next
        while current:
            s += '->' + str(current.data)
            current = current.next
        return f"SLL: {s}\tsize: {self.size()}"


if __name__ == '__main__':
    try:
        sll = Singly_linked_list()
        print(sll)

        sll.push_back(97)
        print(sll)

        sll.push_back(3)
        print(sll)

        sll.push_back(5)
        print(sll)

        sll.push_back(7)
        print(sll)

        sll.insert(97, 2)
        print(sll)

        current = sll.head
        current2 = sll.head
        for i in range(2):
            current = current.next
        for i in range(4):
            current2 = current2.next
        current2.next = current
        print(sll.has_cycle())
        print(sll.get_start_point().data)


        # sll.reverse()
        # print(sll)

        # print(sll.get_middle_node())

        # sll.delete(3)
        # print(sll)

        # sll.pop_back()
        # print(sll)

        # print(sll.search(0))
        # print()

        # sll2 = Singly_linked_list()
        # print(sll2)
        #
        # sll2.push_back(2)
        # print(sll2)
        #
        # sll2.push_back(4)
        # print(sll2)
        #
        # sll2.push_back(6)
        # print(sll2)
        #
        # sll2.push_back(8)
        # print(sll2)
        #
        # merged_list = sll2.mergeTwoSortedLinkedLists(sll)
        # print(merged_list)

    except IndexError as ie:
        print(str(ie))

    except ValueError as ve:
        print(str(ve))
