class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def print_node(self):
        print(self._value)

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        self._next = node


class DoubleLinkedList:
    def __init__(self):
        self._first = None
        self._end = None

    def is_empty(self):
        return self._first is None

    def insert_start(self, value):
        node = Node(value)

        if self.is_empty():
            self._end = node

        node.next = self._first
        self._first = node

    def insert_end(self, value):
        node = Node(value)

        if self.is_empty():
            self._first = node
        else:
            self._end.next = node

        self._end = node

    def remove_start(self):
        if self.is_empty():
            print("A lista esta vazia")

            return

        aux = self._first

        if self._first.next is None:
            self._end = None

        self._first = self._first.next

        return aux

    def get_value(self):
        if self.is_empty():
            print("A lista está vazia")
            return

        current = self._first

        while current is not None:
            current.print_node()
            current = current.next
