from doubly_linked_list import DoublyLinkedList, Node
class PriorityQueue:

    def __init__(self):
        self.queue = DoublyLinkedList()


    def size(self):
        return self.queue.getLength()

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, x):
        newNode = Node(x)
        curr = self.queue.head

        while curr.next.next and x < curr.next.data:
            curr = curr.next
        self.queue.insertAfter(curr, newNode)

    def dequeue(self):
        return self.queue.popAt(self.queue.getLength())

    def peek(self):
        return self.queue.getAt(self.queue.getLength()).data

pq = PriorityQueue()
pq.enqueue(3)
pq.enqueue(7)
pq.enqueue(4)
pq.enqueue(3)
pq.enqueue(1)
print(pq.queue)