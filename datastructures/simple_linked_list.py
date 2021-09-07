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
        if not self._first.next:
            print("A lista está vazia")

            return None

        aux_node = self._first

        self._first = self._first.next

        return aux_node

    def search(self, value):
        if not self._first.next:
            print("A lista está vazia")

            return None

        aux_node = self._first

        while aux_node._value != value:
            if not aux_node.next:
                print("Elemento não encontrado")
                return None
            else:
                aux_node = aux_node.next

        return aux_node._value

    def remove(self, value):
        if not self._first.next:
            print("A lista está vazia")

            return None

        aux_node = self._first
        before_node = self._first

        while aux_node._value != value:
            if not aux_node.next:
                print("Elemento não encontrado")
                return None
            else:
                before_node = aux_node
                aux_node = aux_node.next

        if aux_node == self._first:
            self._first = self._first.next
        else:
            before_node.next = aux_node.next

        return aux_node._value
