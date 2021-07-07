class UnorderedVector:
    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self.values = []

    def is_empty(self):
        if self.last_position == -1:
            return True

        return False

    def is_capacity_max(self):
        if self.last_position == self.capacity - 1:
            return True

        return False

    def print(self):
        if self.is_empty():
            print("O vetor está vazio")
        else:
            for i in range(self.last_position + 1):
                print(i, " - ", self.values[i])

    def insert(self, value):
        if self.is_capacity_max():
            print("Capacidade máxima atiginda")
        else:
            self.values.append(value)
            self.last_position += 1

    def search(self, value):
        if self.is_empty():
            print("O Vetor está vazio")

        for i in range(self.last_position + 1):
            if value == self.values[i]:
                print(f"{i} - {value}")

    def remove(self, value):
        for i in range(self.last_position):
            if self.values[i] == value:
                self.values[i] = self.values[i + 1]
            else:
                continue

            if self.values[i] == value:
                continue

            self.last_position = i

    def __get_positions(self, value):
        positions = []

        if self.is_empty():
            return None

        for i in range(self.last_position + 1):
            if value == self.values[i]:
                positions.append(i)

        return positions

    def __str__(self):
        str = ""

        for i in range(self.last_position + 1):
            str += f"{i} - {self.values[i]}\n"

        return str
