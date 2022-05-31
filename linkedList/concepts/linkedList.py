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
    def __init__(self,head = None) -> None:
        if head:
            self.head = Node(head)
        else:
            self.head = None
    # method for push element to the front 
    def push(self, element) -> None:
        # make a new node 
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node
    # insert node at the end
    def append(self, element) -> None:
        # make new node 
        new_node = Node(element)
        # if list is empty
        if self.head==None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
    # insert element in the middle of the list
    def insert(self, element1, element2) -> None:
        new_node1 = Node(element1)
        new_node2 = Node(element2)

        cur = self.head
        while cur:
            if cur.data==new_node1.data:
                temp = cur.next
                cur.next = new_node2
                new_node2.next = temp
                break
            cur = cur.next
        
        # edge case 
        if not cur:
            print("There is no such element in the list")
    # delete a node from linked list 
    def delete(self, element)->None:
        if self.head == None:
            print("The list is empty")
            return 

        cur = self.head
        if cur.data == element:
            temp = cur.next
            cur = None
            self.head = temp
            return 
        pre = None
        while cur:
            if cur.data==element:
                pre.next = cur.next
                cur.next = None
            pre = cur
            cur = cur.next 
        
    def printList(self) -> None:
        cur = self.head
        while cur:
            print(cur.data , "-> ",end="")
            cur = cur.next
        print("None")

# driver code
if __name__=="__main__":
    ll = LinkedList(4) 
    ll.push(8)         
    ll.push(16)       
    ll.push(28)         
    ll.append(2)
    ll.append(0)
    ll.insert(16, 20)
    ll.delete(0)
    ll.delete(28)
    ll.printList()
