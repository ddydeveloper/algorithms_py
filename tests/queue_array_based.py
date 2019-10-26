import unittest
from scr import queue_array_based


class TestQueue(unittest.TestCase):
    def test(self):
        queue = queue_array_based.Queue(4)
        self.assertTrue(queue.dequeue() is None)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertTrue(queue.dequeue() == 1)
        queue.enqueue(4)
        queue.enqueue(5)

        self.assertTrue(queue.dequeue() == 2)
        self.assertTrue(queue.dequeue() == 3)
        self.assertTrue(queue.dequeue() == 4)
        self.assertTrue(queue.dequeue() == 5)
        self.assertTrue(queue.dequeue() is None)
