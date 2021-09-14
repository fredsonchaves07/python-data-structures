import algorithms
from algorithms import expression_validate
from datastructures.bigO_anotation import BigOAnotation
from datastructures.circular_queue import CircularQueue
from datastructures.deque import Deque
from datastructures.double_linked_list import DoubleLinkedList
from datastructures.ordered_vector import OrderedVector
from datastructures.priority_queue import PriorityQueue
from datastructures.simple_linked_list import SimpleLinkedList
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
# stack = Stack(5)
# stack.insert(10)
# stack.insert(1)
# stack.insert(2)
# print(stack.peek())
# stack.insert(10)
# stack.remove()
# print(stack.peek())

# expression = "a{b(c]d}e"

# print(expression_validate.is_valid_expression(expression))

# Queue
# queue = CircularQueue(5)
# queue.peek()
# queue.queue(1)
# queue.peek()
# queue.queue(5)
# queue.peek()
# queue.queue(3)
# queue.queue(4)
# queue.queue(2)
# queue.queue(7)
# queue.dequeue()
# queue.dequeue()
# queue.peek()

# Priority Queue
# queue = PriorityQueue(5)
# queue.peek()
# queue.queue(30)
# queue.peek()
# queue.queue(50)
# queue.peek()
# queue.queue(10)
# queue.peek()
# queue.dequeue()
# queue.peek()

# Deque
# deque = Deque(5)
# deque.add_end(5)
# print(deque.get_start(), deque.get_end())
# deque.add_end(10)
# print(deque.get_start(), deque.get_end())
# deque.add_start(3)
# print(deque.get_start(), deque.get_end())
# deque.add_start(2)
# deque.add_end(11)
# print(deque.get_start(), deque.get_end())
# deque.remove_start()
# deque.remove_end()
# print(deque.get_start(), deque.get_end())
# deque.remove_end()
# print(deque.get_start(), deque.get_end())

# SimpleLinkedList
# linked_list = SimpleLinkedList()
# linked_list.add_start(1)
# linked_list.add_start(5)
# linked_list.add_start(2)
# linked_list.add_start(10)
# linked_list.get_values()
# linked_list.remove_start()
# linked_list.get_values()
# linked_list.search(5)
# linked_list.remove(2)

double_linked_list = DoubleLinkedList()
double_linked_list.insert_start(1)
double_linked_list.insert_start(2)
double_linked_list.insert_start(5)
double_linked_list.insert_start(7)
double_linked_list.insert_start(3)
double_linked_list.get_value()
