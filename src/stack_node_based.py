class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __str__(self):
        return self.value


class Stack:
    def __init__(self):
        self.top = Node(None)
        self._count = 0

    def pop(self):
        if self.top.next_node is None:
            return None
        node_to_pop = self.top.next_node
        self.top.next_node = node_to_pop.next_node
        self._count -= 1
        return node_to_pop.value

    def peek(self):
        if self.top.next_node is None:
            return None
        return self.top.next_node.value

    def count(self):
        return self._count

    def clear(self):
        self._count = 0
        self.top.next_node = None

    def push(self, value):
        new_node = Node(value)
        new_node.next_node = self.top.next_node
        self.top.next_node = new_node
        self._count += 1


