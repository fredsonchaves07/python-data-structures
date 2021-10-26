class ShelSort:
    def __init__(self, vector):
        self._length = len(vector)
        self._interval = self._length // 2

        print(self._sort_vector(vector))
    
    def _sort_vector(self, vector):
        while self._interval > 0:
            for i in range(self._interval, self._length):
                aux = vector[i]
                j = 1
                while j >= self._interval and vector[j - self._interval] > aux:
                    vector[j] = vector[j - self._length]
                    j -= self._length
                vector[j] = aux
            self._length //= 2
        
        return vector