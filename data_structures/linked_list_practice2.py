class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail

    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr.next:
            curr = curr.next
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
        return s

    def getLength(self):
        return self.nodeCount

    def traverse(self):
        result = []
        curr = self.head
        while curr.next:
            curr = curr.next
            result.append(curr.data)
        return result

    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr

    def insertAfter(self, prev, newNode):
        newNode.next = prev.next
        if prev.next is None:
            self.tail = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos != 1 and pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)

    def popAfter(self, prev):
        if prev == self.tail:
            return None
        cur = prev.next
        prev.next = cur.next
        if prev.next is None:
            self.tail = prev
        self.nodeCount -= 1
        return cur.data


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        prev = self.getAt(pos - 1)
        return self.popAfter(prev)

    def concat(self, L):
        self.tail.next = L.head.next
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