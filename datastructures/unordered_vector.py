import numpy

class UnorderedVector():
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
            print('O vetor está vazio')
        else:
            for i in range(self.last_position + 1):
                print(i, ' - ', self.values[i])
    
    def insert(self, value):
        if self.is_capacity_max():
            print('Capacidade máxima atiginda')
        else:
            self.last_position += 1
            self.values.append(value) 

    def search(self, value):
        if self.is_empty():
            return None

        for i in range(self.last_position + 1):
            if value == self.values[i]:
                return i