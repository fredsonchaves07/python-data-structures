class InsertionSort:
    def __init__(self, vector):
        self._length = len(vector)

        print(self._sort_vector(vector))
    
    def _sort_vector(self, vector):
        for i in range(1, self._length):
            marcado = vector[i]
            j = i - 1
            while j >= 0 and marcado < vector[j]:
                vector[j + 1] = vector[j]
                j -= 1
            vector[j + 1] = marcado

        return vector