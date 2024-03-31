from data_structures.linkedList_and_stack.doubly_linked_list import DoublyLinkedList

class Node:

    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None

class LinkedListQueue:

    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.getLength()

    def isEmpty(self):
        return self.size() == 0


    def enqueue(self, item):
        node = Node(item)
        self.data.insertAt(self.data.getLength() + 1, node)

    def dequeue(self):
        return self.data.popAt(1)

    def peek(self):
        return self.data.getAt(1).data

queue = LinkedListQueue()
print(queue.size())
queue.enqueue(1)
print(queue.peek())
queue.enqueue(2)
print(queue.peek())
queue.enqueue(3)
print(queue.peek())
print(queue.dequeue())
print(queue.peek())
print(queue.dequeue())
print(queue.dequeue())
print(queue.isEmpty())
print(queue.size())


class CircularQueue:

    def __init__(self, n):
        self.maxCount = n
        self.data = [None] * n
        self.count = 0
        self.front = -1
        self.rear = -1


    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.maxCount

    def enqueue(self, x):
        if self.isFull():
            raise IndexError('Queue full')
        self.rear = (self.rear + 1) % self.maxCount
        self.data[self.rear] = x
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError('Queue empty')
        self.front = (self.front + 1) % self.maxCount
        x = self.data[self.front]
        self.count -= 1
        return x

    def peek(self):
        if self.isEmpty():
            raise IndexError('Queue empty')
        return self.data[(self.front + 1) % self.maxCount]

print("#########")
cqueue = CircularQueue(5)
print(cqueue.front)
print(cqueue.rear)
cqueue.enqueue(1)
print()
print(cqueue.front)
print(cqueue.rear)
cqueue.enqueue(2)
print()
print(cqueue.front)
print(cqueue.rear)
print()
print(cqueue.dequeue())
print(cqueue.front)
print(cqueue.rear)
print()
print(cqueue.size())
print(cqueue.dequeue())
print(cqueue.isEmpty())
print()
print(cqueue.front)
print(cqueue.rear)
