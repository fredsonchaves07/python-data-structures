class SelectionSort:
    def __init__(self, vector):
        self._length = len(vector)
        print(self._sort_vector(vector))

    def _sort_vector(self, vector):
        for i in range(self._length):
            id_minimun = i
            for j in range(i + 1, self._length):
                if vector[id_minimun] > vector[j]:
                    id_minimun = j
            temp = vector[i]
            vector[i] = vector[id_minimun]
            vector[id_minimun] = temp
        return vector
