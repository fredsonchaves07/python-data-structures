class Stack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__top = -1
        self.__values = []

    def is_empty(self):
        if self.__top == -1:
            return True

    def length(self):
        return self.__top + 1

    def is_capacity_max(self):
        if self.__top == self.__capacity - 1:
            return True

        return False

    def insert(self, value):
        if self.is_capacity_max():
            print("Capacidade máxima atiginda")
        else:
            self.__top += 1
            self.__values.append(value)

    def search(self, value):
        if self.is_empty():
            print("A pilha está vazia")

        for i in range(self.__top + 1):
            if value == self.__values[i]:
                print(f"{i} - {value}")

    def remove(self, value):
        aux_values = []

        for i in range(self.__top + 1):
            if self.__values[i] != value:
                aux_values.append(self.__values[i])

        for i in range(len(aux_values)):
            self.__values[i] = aux_values[i]

        self.__top = len(aux_values) - 1

    def peek(self):
        if self.__top != -1:
            return self.__values[self.__top]

        return ""
