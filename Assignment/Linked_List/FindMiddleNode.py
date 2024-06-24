class Node:
    def __init__(self,data):
        self.data = data;
        self.next = None;



def createLinkedList(values):
    if not values:
        return None;
    
    head = Node(values[0]);
    curr = head;
    
    for i in range(1,len(values)):
        curr.next = Node(values[i]);
        curr = curr.next;
    
    return head;

