"""
Insert a node at the Head:

Insert a node at the head of a linked list.
input :
1
2
3
output:
1 
2 1
3 2 1
"""


def printList(head):
    curr = head
    while True:
        print(curr.data,"->", end=" ")
        if curr.next == None:
            break
        curr = curr.next
    print("null")
    print()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertNodeAtHead(head, data):
    newNode = Node(data)
    newNode.next = head        
    return newNode


head = None
head = insertNodeAtHead(head, "One")
printList(head)
head = insertNodeAtHead(head, "Two")
printList(head)
head = insertNodeAtHead(head, "Three")
printList(head)
