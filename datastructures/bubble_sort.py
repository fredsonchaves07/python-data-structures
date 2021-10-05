class BubbleSort:
    def __init__(self, vector):
        self._length = len(vector)
        print(self._sort_vector(vector))

    def _sort_vector(self, vector):
        for i in range(self._length):
            for j in range(0, self._length - i - 1):
                if vector[j] > vector[j + 1]:
                    temp = vector[j]
                    vector[j] = vector[j + 1]
                    vector[j + 1] = temp

        return vector
