class LinkedList:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.size = 0

        self.left = LinkedList(0)
        self.right = LinkedList(0)

        self.left.next = self.right
        self.right.prev = self.left


    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        newnode = LinkedList(value, self.left.next, self.left)
        self.left.next.prev = newnode
        self.left.next = newnode

        self.size += 1
        return True


    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        newnode = LinkedList(value, self.right, self.right.prev)
        self.right.prev.next = newnode
        self.right.prev = newnode

        self.size += 1
        return True


    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.left.next = self.left.next.next
        self.left.next.prev = self.left

        self.size -= 1
        return True


    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.right.prev = self.right.prev.prev
        self.right.prev.next = self.right

        self.size -= 1
        return True


    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.next.val


    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.val


    def isEmpty(self) -> bool:
        return self.size == 0


    def isFull(self) -> bool:
        return self.size == self.k



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()