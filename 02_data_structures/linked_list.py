"""A small singly linked list implementation for learning."""


class Node:
    """One item in a singly linked list."""

    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    """Linked list supporting append, search, and deletion."""

    def __init__(self):
        self.head = None

    def append(self, value):
        """Add a value at the end. Time: O(n), or O(1) with a tail pointer."""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def contains(self, target):
        """Return True when target is present. Time: O(n)."""
        current = self.head
        while current is not None:
            if current.value == target:
                return True
            current = current.next
        return False

    def delete(self, target):
        """Delete the first matching value. Return whether it was found."""
        if self.head is None:
            return False

        if self.head.value == target:
            self.head = self.head.next
            return True

        previous = self.head
        current = self.head.next

        while current is not None:
            if current.value == target:
                previous.next = current.next
                return True
            previous, current = current, current.next

        return False

    def to_list(self):
        """Convert the linked list to a regular Python list."""
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next
        return values


if __name__ == "__main__":
    numbers = SinglyLinkedList()
    for number in (10, 20, 30):
        numbers.append(number)

    print("List:", numbers.to_list())
    print("Contains 20:", numbers.contains(20))
    numbers.delete(20)
    print("After deleting 20:", numbers.to_list())
