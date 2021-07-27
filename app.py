from datastructures.bigO_anotation import BigOAnotation
from datastructures.ordered_vector import OrderedVector
from datastructures.stack import Stack
from datastructures.unordered_vector import UnorderedVector

# Big-O Annotation
# big_anotation = BigOAnotation()
# big_anotation.sum_common_case(100)
# big_anotation.sum_best_case(100)
# big_anotation.list1()
# big_anotation.list2()

# Unordered Vector
# unordered_vector = UnorderedVector(5)
# print(unordered_vector.is_empty())
# unordered_vector.insert(1)
# unordered_vector.insert(5)
# print(unordered_vector.is_empty())
# unordered_vector.insert(7)
# unordered_vector.insert(5)
# unordered_vector.insert(5)
# unordered_vector.search(5)
# unordered_vector.remove(5)
# unordered_vector.search(5)
# unordered_vector.insert(3)
# unordered_vector.insert(6)
# unordered_vector.insert(0)
# unordered_vector.insert(0)
# print(unordered_vector)

# Ordered Vector
# ordered_vector = OrderedVector(5)
# ordered_vector.insert(5)
# ordered_vector.insert(5)
# ordered_vector.insert(0)
# ordered_vector.search(0)
# ordered_vector.remove(5)
# print(ordered_vector.length())
# ordered_vector.insert(1)
# ordered_vector.insert(3)
# ordered_vector.insert(0)
# ordered_vector.insert(5)
# print(ordered_vector)
# ordered_vector.binary_search(5)

# Stack
stack = Stack(5)
stack.insert(10)
stack.insert(1)
stack.insert(2)
print(stack.peek())
stack.insert(10)
stack.search(10)
stack.remove(10)
print(stack.peek())
