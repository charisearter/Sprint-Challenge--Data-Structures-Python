class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        prevNode = None  # SLL nothing before it (should work...)

        while self.head != None or self.head.next != None:  # while head has value or next has value
            nextNode = self.head.next  # variable for next node

            self.head.next = prevNode  # head prev set to null
            prevNode = self.head  # old head set to previous
            self.head = nextNode  # head.next set to head
        return prevNode  # return the new head
