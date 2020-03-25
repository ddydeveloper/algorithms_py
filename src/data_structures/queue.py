from src.data_structures.array import Array
from src.data_structures.node import Node


class QueueArrayBased(Array):
    def __init__(self, size):
        super().__init__(size)
        self.first = None
        self.last = None

    def enqueue(self, value):
        if self.length == self.size:
            raise OverflowError()

        if self.first is None:
            self.first = 0
            self.last = 0
            self.data[0] = value
            self.length += 1
            return

        if self.last == self.size - 1:
            self.last = 0
            self.data[0] = value
        else:
            self.last += 1
            self.data[self.last] = value

        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None

        if self.length == 1:
            value = self.data[self.first]
            self.length = 0
            self.first = None
            self.last = None
            return value

        value = self.data[self.first]

        if self.first == self.size - 1:
            self.first = 0
        else:
            self.first += 1

        self.length -= 1
        return value


class QueueNodeBased:
    def __init__(self, size):
        self.top = Node(None)
        self.first = None
        self.items_count = 0
        self.size = size

    def enqueue(self, value):
        if self.items_count == self.size:
            raise OverflowError()

        node_to_enqueue = Node(value)

        if not self.top.next_node:
            node_to_enqueue.prev_node = self.top
            self.top.next_node = node_to_enqueue
            self.first = node_to_enqueue
        else:
            node_to_enqueue.next_node = self.top.next_node
            self.top.next_node.prev_node = node_to_enqueue
            self.top.next_node = node_to_enqueue

        self.items_count += 1

    def dequeue(self):
        if not self.first:
            return None

        value = self.first.value

        if self.first == self.top.next_node:
            self.first = None
            self.top.next_node = None
        else:
            self.first = self.first.prev_node
            self.first.next_node = None

        self.items_count -= 1

        return value

    def count(self):
        return self.items_count

    def peek(self):
        if not self.first:
            return None

        return self.first.value

    def clear(self):
        self.items_count = 0
        self.first = None
        self.top.next_node = None
