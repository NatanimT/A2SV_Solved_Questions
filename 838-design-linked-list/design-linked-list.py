class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        curr = self.head
        while index:
            curr = curr.next
            index -= 1
        return curr.val

    def addAtHead(self, val: int) -> None:
        newnode = Node(val)
        newnode.next = self.head   
        self.head = newnode
        self.length += 1

    def addAtTail(self, val: int) -> None:
        newnode = Node(val)
        if self.head is None:
            self.head = newnode
        else:
            curr = self.head
            while curr.next is not None:   
                curr = curr.next
            curr.next = newnode
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        
        if index == 0:
            self.addAtHead(val)
            return
        
        if index == self.length:
            self.addAtTail(val)
            return
        
        newnode = Node(val)
        curr = self.head
        while index - 1:
            curr = curr.next
            index -= 1
        
        newnode.next = curr.next
        curr.next = newnode
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            while index - 1:
                curr = curr.next
                index -= 1
            curr.next = curr.next.next
        
        self.length -= 1
