import unittest

from src.queue import Node, Queue


class TestNode(unittest.TestCase):
    def test_init(self):
        data = Node('Данные')
        self.assertEqual(data.data, "Данные")
        self.assertEqual(data.next_node, None)

        data_2 = Node('Данные_2')
        self.assertEqual(data_2.data, "Данные_2")
        self.assertEqual(data_2.next_node, None)

    def test_repr(self):
        data = Node('Данные')
        self.assertEqual(repr(data), "Node('Данные', None)")


class TestQueue(unittest.TestCase):

    def test_str(self):
        queue = Queue()
        self.assertEqual(str(queue), '')

        queue.enqueue('Данные')
        queue.enqueue('Данные_2')
        self.assertEqual(str(queue), 'Данные\nДанные_2')

    def test_enqueue(self):
        queue = Queue()

        queue.enqueue('Данные')
        self.assertEqual(queue.head.data, 'Данные')
        self.assertEqual(queue.tail.data, 'Данные')

        queue.enqueue('Данные_2')
        self.assertEqual(queue.head.data, 'Данные')
        self.assertEqual(queue.tail.data, 'Данные_2')

        queue.enqueue('Данные_3')
        self.assertEqual(queue.head.data, 'Данные')
        self.assertEqual(queue.tail.data, 'Данные_3')

        self.assertEqual(queue.head.next_node.data, 'Данные_2')
        self.assertEqual(queue.head.next_node.next_node.data, 'Данные_3')

    def test_dequeue(self):
        queue = Queue()

        queue.enqueue('Данные')
        queue.dequeue()
        self.assertEqual(queue.head, None)
        self.assertEqual(queue.tail, None)

        queue.enqueue('Данные')
        queue.enqueue('Данные_2')
        queue.enqueue('Данные_3')
        queue.dequeue()
        self.assertEqual(queue.head.data, 'Данные_2')
        queue.dequeue()
        self.assertEqual(queue.head.data, 'Данные_3')
        queue.dequeue()
        self.assertEqual(queue.head, None)

        queue.enqueue('Данные')
        self.assertEqual(queue.dequeue().data, 'Данные')
