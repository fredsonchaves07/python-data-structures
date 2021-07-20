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

    def search(self, value):
        if self.is_empty():
            print("O Vetor está vazio")

        for i in range(self.__last_position + 1):
            if value == self.__values[i]:
                print(f"{i} - {value}")

    def binary_search(self, value):
        upper_limit = 0
        inferior_limit = self.__last_position

        while True:
            if upper_limit > inferior_limit:
                break

            current_position = int((inferior_limit + upper_limit) / 2)

            if value == self.__values[current_position]:
                print(f"{current_position} - {self.__values[current_position]}")
                break

            if value >= self.__values[current_position]:
                upper_limit = current_position + 1
                continue

            if value <= self.__values[current_position]:
                inferior_limit = current_position - 1
                continue

    def remove(self, value):
        aux_values = []

        for i in range(self.__last_position + 1):
            if self.__values[i] != value:
                aux_values.append(self.__values[i])

        for i in range(len(aux_values)):
            self.__values[i] = aux_values[i]

        self.__last_position = len(aux_values) - 1

    def __str__(self):
        string = ""

        for i in range(self.__last_position + 1):
            string += f"{i} - {self.__values[i]}\n"

        return string
