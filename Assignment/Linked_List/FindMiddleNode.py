class Node:
    def __init__(self,data):
        self.data = data;
        self.next = None;

def printLinkedList(head):
    if not head:
        return None;
    
    curr = head;
    print("head-- ",end="")
    while(curr):
        print(curr.data,"-> ",end="");
        curr = curr.next;
    print("null","\n");

def findMiddleNode(head):
    if not head:
        return None;

    fast = head;
    slow = head;

    while fast and fast.next:
        slow = slow.next;
        fast = fast.next.next;

    print(f"middle Node : |{slow.data}| : ",end="");
    printLinkedList(head);
   

def createLinkedList(values):
    if not values:
        return None;
    
    head = Node(values[0]);
    curr = head;
    
    for i in range(1,len(values)):
        curr.next = Node(values[i]);
        curr = curr.next;
    
    return head;

