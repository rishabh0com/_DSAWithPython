class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printList(head):
    curr = head;
    while(curr):
        print(curr.data, "-> ", end="")
        curr = curr.next;
    print("null");
    print()

def insertNodeAtTail(head, data):
    newNode = Node(data)
    if head is None:
        return newNode

    curr = head
    while curr.next:
        curr = curr.next

    curr.next = newNode
    return head


head = None
# 1
head = insertNodeAtTail(head, 1);
printList(head);
head = insertNodeAtTail(head, 2);
printList(head);
