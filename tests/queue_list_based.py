import unittest
from scr import queue_list_based


class TestQueue(unittest.TestCase):
    def test_queue(self):
        queue = queue_list_based.Queue(4)
        self.assertTrue(queue.dequeue() is None)
        self.assertTrue(queue.count == 0)
        self.assertTrue(queue.size == 4)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        self.assertTrue(queue.count == 4)
        self.assertTrue(queue.dequeue() == 1)
        self.assertTrue(queue.dequeue() == 2)
        self.assertTrue(queue.dequeue() == 3)
        self.assertTrue(queue.dequeue() == 4)
        self.assertTrue(queue.dequeue() is None)
        self.assertTrue(queue.count == 0)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        queue.clear()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        # queue.enqueue(5)
