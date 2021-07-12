class OrderedVector:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__last_position = -1
        self.__values = []

    def is_empty(self):
        if self.__last_position == -1:
            return True

        return False

    def length(self):
        return self.__last_position + 1

    def is_capacity_max(self):
        if self.__last_position == self.__capacity - 1:
            return True

        return False

    def insert(self, value):
        if self.is_capacity_max():
            print("Capacidade máxima atiginda")
        elif self.length() == 0:
            self.__values.insert(0, value)
            self.__last_position += 1
        else:
            for i in range(self.__last_position + 1):
                if value < self._OrderedVector__values[i]:
                    self.__values.insert(i, value)
                    break
                else:
                    self.__values.insert(self.__last_position + 1, value)
            self.__last_position += 1
