import unittest
from src.data_structures.c_queue import QueueArrayBased, QueueNodeBased


class TestQueue(unittest.TestCase):
    def test_array_based(self):
        queue = QueueArrayBased(4)
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

    def test_node_based(self):
        queue = QueueNodeBased(4)
        self.assertTrue(queue.dequeue() is None)
        self.assertTrue(queue.items_count == 0)
        self.assertTrue(queue.size == 4)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        self.assertTrue(queue.items_count == 4)
        self.assertTrue(queue.dequeue() == 1)
        self.assertTrue(queue.dequeue() == 2)
        self.assertTrue(queue.dequeue() == 3)
        self.assertTrue(queue.dequeue() == 4)
        self.assertTrue(queue.dequeue() is None)
        self.assertTrue(queue.items_count == 0)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        queue.clear()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)


if __name__ == '__main__':
    unittest.main()