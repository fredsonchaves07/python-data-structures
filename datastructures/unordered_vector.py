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

    def insert(self, value):
        if self.is_capacity_max():
            print("Capacidade máxima atiginda")
        else:
            self.values.insert(self.last_position + 1, value)
            self.last_position += 1

    def search(self, value):
        if self.is_empty():
            print("O Vetor está vazio")

        for i in range(self.last_position + 1):
            if value == self.values[i]:
                print(f"{i} - {value}")

    def remove(self, value):
        aux_values = []

        for i in range(self.last_position + 1):
            if self.values[i] != value:
                aux_values.append(self.values[i])

        for i in range(len(aux_values)):
            self.values[i] = aux_values[i]

        self.last_position = len(aux_values) - 1
