class Node:
    def __init__(self, value):
        self._value = value
        self._next = None
        self._previous = None

    def print_node(self):
        print(self._value)

    @property
    def next(self):
        return self._next

    @property
    def previous(self):
        return self._previous

    @next.setter
    def next(self, node):
        self._next = node

    @previous.setter
    def previous(self, node):
        self._previous = node


class DoublyLinkedList:
    def __init__(self):
        self._first = None
        self._end = None

    def is_empty(self):
        return self._first is None

    def insert_start(self, value):
        node = Node(value)

        if self.is_empty():
            self._end = node
        else:
            self._first.previous = node

        node.next = self._first
        self._first = node

    def inser_end(self, value):
        node = Node(value)

        if self.is_empty():
            self._first = node
        else:
            self._end.next = node
            node.previous = self._end
        self._end = node

    def show_start(self):
        node = self._first

        while node is not None:
            node.print_node()
            node = node.next

    def show_end(self):
        node = self._end

        while node is not None:
            node.print_node()
            node = node.previous

    def remove_start(self):
        aux = self._first

        if self._first.next is None:
            self._end = None
        else:
            self._first.next.previous = None

        self._first = self._first.next

        return aux

    def remove_end(self):
        aux = self._first

        if self._first.next is None:
            self._first = None
        else:
            self._end.previous.next = None

        self._end = self._end.previous

        return aux

    def remove_position(self, value):
        node = self._first

        while node._value != value:
            node = node.next

            if node is None:
                return None

        if node == self._first:
            self._first = node.next
        else:
            node.previous.next = node.next

        if node == self._end:
            self._end = node.previous
        else:
            node.next.previous = node.previous

        return node
