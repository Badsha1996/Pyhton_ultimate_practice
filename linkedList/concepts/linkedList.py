# Linked List data structure 
# store data adress to next element instead of random element 
# Array is fixed in size, if we need to insert at the middle of an array
# it can be a problem 
# linked list has dynamic memory which is allocated in run time 
# when u know size of elements use array 
# else linked list is better for access 
# But the best option is ArrayList / vector 

# push in fron and in middle - O(1) time
# push at the end - O(n)

from dataclasses import dataclass


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    