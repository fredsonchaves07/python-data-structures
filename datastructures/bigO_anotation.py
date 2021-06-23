from timeit import timeit
"""
- Realiza a compração objetiva entre 2 algoritmos considerando as diferenças
entre processamento, sistema operacional, linguagem de programação
- O quanto a "complexidade" do algoritmo aumenta de acordo com as entradas
"""
class BigOAnotation:
    def sum_common_case(self, n):
        sum = 0.0

        for i in range(n + 1):
            sum += i

        print(f'Result: {sum}')
        print(f'Efficient: {timeit()}')
    
    def sum_best_case(self, n):
        sum = (n * (n + 1)) / 2
        
        print(f'Result: {sum}')
        print(f'Efficient: {timeit()}')

    def list1(self):
        list = []

        for i in range(1000):
            list += [i]
        print(f'Result: {list}')
        print(f'Efficient: {timeit()}')
    
    def list2(self):
        result = range(1000)
        for i in result:
            print(f'Result: {i}')
        print(f'Efficient: {timeit()}')
        