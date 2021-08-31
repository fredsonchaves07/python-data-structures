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


class SimpleLinkedList:
    def __init__(self):
        self._first = None

    def add_start(self, value):
        node = Node(value)
        node.next = self._first
        self._first = node

    def get_values(self):
        current_node = self._first

        while current_node:
            current_node.print_node()
            current_node = current_node.next

    def remove_start(self):
        aux_node = self._first

        if not self._first.next:
            return None

        self._first = self._first.next

        return aux_node
