import unittest
from scr import queue_list_based


class TestQueue(unittest.TestCase):
    def test_queue(self):
        queue = queue_list_based.Queue()
        self.assertTrue(queue.dequeue() is None)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertTrue(queue.dequeue() == 1)
        self.assertTrue(queue.dequeue() == 2)
        self.assertTrue(queue.dequeue() == 3)
        self.assertTrue(queue.dequeue() is None)
