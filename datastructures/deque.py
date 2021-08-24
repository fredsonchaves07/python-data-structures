class Deque:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__start = -1
        self.__end = 0
        self.__values = []
        self.__length = 0

    def is_empty(self):
        return self.__length == 0

    def is_capacity_max(self):
        return self.__length == self.__capacity

    def length(self):
        return self.__length

    def add_start(self, value):
        if self.is_capacity_max():
            print("Fila cheia")
            return

        if self.__start == -1:
            self.__start = 0
            self.__end = 0
        elif self.__start == 0:
            self.__start = self.__length
        else:
            self.__start -= 1

        self.__values.insert(self.__start, value)
        self.__length += 1

    def add_end(self, value):
        if self.is_capacity_max():
            print("Fila cheia")
            return

        if self.__start == -1:
            self.__start = 0
            self.__end = 0
        elif self.__end == self.__capacity - 1:
            self.__end = 0
        else:
            self.__end += 1

        self.__values.insert(self.__end, value)
        self.__length += 1

    def remove_start(self):
        if self.is_empty():
            print("Fila vazia")
            return

        if self.__start == self.__end:
            self.__start = -1
            self.__end = -1
        elif self.__start == self.__capacity - 1:
            self.__start = 0
        else:
            self.__start += 1

        self.__length -= 1

    def remove_end(self):
        if self.is_empty():
            print("Fila vazia")
            return

        if self.__start == self.__end:
            self.__start = -1
            self.__end = -1
        elif self.__start == 0:
            self.__end = self.__capacity - 1
        else:
            self.__end -= 1

        self.__length -= 1

    def get_start(self):
        if self.is_empty():
            print("Fila vazia")
            return

        return self.__values[self.__start]

    def get_end(self):
        if self.is_empty():
            print("Fila vazia")
            return

        return self.__values[self.__end]
