class Node:

    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None


    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr.next.next:
            curr = curr.next
            s += repr(curr.data)
            if curr.next.next is not None:
                s += ' -> '
        return s


    def getLength(self):
        return self.nodeCount


    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result

    # 실습 문제
    def reverse(self):
        reversed = []
        cur = self.tail
        while cur.prev.prev:
            cur = cur.prev
            reversed.append(cur.data)
        return reversed


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount + 1:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr


    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True

    def insertBefore(self, next, newNode):
        prev_node = next.prev
        newNode.prev = prev_node
        newNode.next = next
        prev_node.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)

    def popAfter(self, prev):
        cur = prev.next
        if cur.next is None:
            return None
        next = cur.next
        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        return cur.data

    def popBefore(self, next):
        cur = next.prev
        if cur.prev is None:
            return None
        prev = cur.prev
        next.prev = prev
        prev.next = next
        self.nodeCount -= 1
        return cur.data

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        if pos > self.nodeCount // 2:
            next = self.getAt(pos + 1)
            return self.popBefore(next)
        prev = self.getAt(pos - 1)
        return self.popAfter(prev)

    # 실습 문제
    def concat(self, L):
        # 첫번째만 빈 경우
        if self.nodeCount == 0:
            L2_first = L.getAt(1)
            self.head.next = L2_first
            L2_first.prev = self.head
            self.nodeCount = L.nodeCount
        # 두번째만 빈 경우
        elif L.nodeCount == 0:
            last = self.getAt(self.nodeCount)
            last.next = L.tail
            L.tail.prev = last
        # 둘다 안 빈 경우
        else:
            last = self.getAt(self.nodeCount)
            L2_first = L.getAt(1)
            last.next = L2_first
            L2_first.prev = last
            self.nodeCount += L.nodeCount
        # 둘다 빈 경우에는 아래만 해당
        self.tail = L.tail

a = Node(67)
b = Node(34)
c = Node(28)
L = DoublyLinkedList()
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


print(L.insertAt(1, a))
print(L.insertAt(2, b))
print(L.insertAt(0, c))
print(L.insertAt(4, c))
print(L)
print(L.insertAt(3, c))
print(L)
print(L.traverse())
d = Node(1)
print(L.insertAt(1, d))
print(L)
e = Node(999)
print(L.insertAt(3, e))
print(L)
print(L.traverse())
print(L.popAt(4))
print(L)
print(L.nodeCount)