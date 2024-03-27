class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.node_count = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos <= 0 or pos > self.node_count:
            return None
        idx = 1
        cur_node = self.head
        while idx < pos:
            cur_node = cur_node.next
            idx += 1
        return cur_node

    def traverse(self): # 2일차 실습문제 # 1: 연결리스트 순회 구현
        cur_node = self.head
        traversed = []
        while cur_node is not None:
            traversed.append(cur_node.data)
            cur_node = cur_node.next

        return traversed

ll = LinkedList()
head = Node(43)
mid = Node(85)
tail = Node(62)
head.next = mid
mid.next = tail
ll.head = head
ll.tail = tail
print(ll.traverse())