class CircularQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__start = 0
        self.__end = -1
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

        if self.__end == self.__capacity - 1:
            self.__end = -1

        self.__end += 1
        self.__values.insert(self.__end, value)
        self.__length += 1

    def dequeue(self):
        if self.is_empty():
            print("Fila vazia")
            return

        aux = self.__values[self.__start]
        self.__start += 1

        if self.__start == self.__capacity:
            self.__start = 0

        self.__length -= 1
        return aux

    def peek(self):
        if self.is_empty():
            print("Fila vazia")
            return

        print(self.__values[self.__start])
