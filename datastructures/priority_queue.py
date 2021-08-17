class PriorityQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__values = []
        self.__length = 0

    def is_empty(self):
        return self.__length == 0

    def is_capacity_max(self):
        return self.__length == self.__capacity

    def length(self):
        return self.__length

    def queue(self, value):
        if self.is_capacity_max():
            print("Fila cheia")
            return

        if self.__length == 0:
            self.__values.insert(self.__length, value)
        else:
            aux = self.__length - 1

            while aux >= 0:
                if value > self.__values[aux]:
                    self.__values.insert(aux + 1, value)
                else:
                    break

                aux -= 1

            self.__values.insert(aux + 1, value)

        self.__length += 1

    def dequeue(self):
        if self.is_empty():
            print("Fila vazia")
            return

        value = self.__values[self.__length - 1]
        self.__length -= 1

        return value

    def peek(self):
        if self.is_empty():
            print("Fila vazia")
            return

        print(self.__values[self.__length - 1])
