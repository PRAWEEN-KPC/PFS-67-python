"""Stack and queue implementations using Python lists and collections."""


class Stack:
    """Last In, First Out (LIFO) collection."""

    def __init__(self):
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self._items[-1]

    def is_empty(self):
        return not self._items

    def __len__(self):
        return len(self._items)


from collections import deque


class Queue:
    """First In, First Out (FIFO) collection."""

    def __init__(self):
        self._items = deque()

    def enqueue(self, value):
        self._items.append(value)

    def dequeue(self):
        if not self._items:
            raise IndexError("dequeue from an empty queue")
        return self._items.popleft()

    def is_empty(self):
        return not self._items

    def __len__(self):
        return len(self._items)


if __name__ == "__main__":
    stack = Stack()
    stack.push("first")
    stack.push("second")
    print("Stack pop:", stack.pop())

    queue = Queue()
    queue.enqueue("first")
    queue.enqueue("second")
    print("Queue dequeue:", queue.dequeue())
