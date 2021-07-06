from datastructures.bigO_anotation import BigOAnotation
from datastructures.unordered_vector import UnorderedVector

# Big-O Annotation
big_anotation = BigOAnotation()
# big_anotation.sum_common_case(100)
# big_anotation.sum_best_case(100)
# big_anotation.list1()
# big_anotation.list2()

unordered_vector = UnorderedVector(5)
unordered_vector.insert(10)
unordered_vector.insert(20)

print(unordered_vector.search(10))