class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

    def __str__(self):
        return self.value


class Queue:
    def __init__(self):
        self.top = Node(None)
        self.first = None

    def enqueue(self, value):
        node_to_enqueue = Node(value)

        if not self.top.next_node:
            node_to_enqueue.prev_node = self.top
            self.top.next_node = node_to_enqueue
            self.first = node_to_enqueue

        node_to_enqueue.next_node = self.top.next_node
        self.top.next_node.prev_node = node_to_enqueue
        self.top.next_node = node_to_enqueue

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

        return value
