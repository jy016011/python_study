class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None


    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
            curr = curr.next
        return s


    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True


    def getLength(self):
        return self.nodeCount

    # 2일차 실습문제 #2
    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        if pos == 1:
            r = self.head.data
            self.head = self.head.next
        else:
            prev = self.getAt(pos - 1)
            cur = prev.next
            r = cur.data
            prev.next = cur.next
            if pos == self.nodeCount:
                self.tail = prev
        # 노드가 하나일 경우
        if self.nodeCount == 1:
            self.tail = None

        self.nodeCount -= 1
        return r

    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


    def concat(self, L):
        self.tail.next = L.head
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount

a = Node(67)
b = Node(34)
c = Node(28)
L = LinkedList()
print(L)
print(L.insertAt(1, a))
print(L.insertAt(2, b))
print(L.insertAt(0, c))
print(L.insertAt(4, c))
print(L)
print(L.insertAt(3, c))
print(L)
d = Node(1)
print(L.insertAt(1, d))
print(L)
e = Node(999)
print(L.insertAt(3, e))
print(L)
# L.popAt(0)
# L.popAt(6)
print(L.popAt(5))
print(L)
print(L.popAt(1))
print(L)
print(L.popAt(2))
print(L)
print(L.popAt(2))
print(L)
print(L.popAt(1))
print(L)