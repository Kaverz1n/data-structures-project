import unittest

from src.linked_list import Node, LinkedList


class TestNode(unittest.TestCase):

    def test_isinstance(self):
        data = Node({'id': 1})
        self.assertIsInstance(data, Node)

    def test_init(self):
        data = Node({'id': 1})
        self.assertEqual(data.data, {'id': 1})
        self.assertEqual(data.next_node, None)

        data_2 = Node({'id': 2})
        self.assertEqual(data_2.data, {'id': 2})
        self.assertEqual(data_2.next_node, None)

    def test_repr(self):
        data = Node({'id': 0})
        self.assertEqual(repr(data), "Node({'id': 0})")

    def test_str(self):
        data = Node({'id': 0})
        self.assertEqual(str(data), 'Узел односвязного списка')


class TestLinkedList(unittest.TestCase):

    def test_isinstance(self):
        linked_list = LinkedList()
        self.assertIsInstance(linked_list, LinkedList)

    def test_init(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list.linked_list, [])
        self.assertEqual(linked_list.head, None)
        self.assertEqual(linked_list.tail, None)

    def test_insert(self):
        linked_list = LinkedList()

        linked_list.insert_beginning({'id': 1})
        self.assertEqual(len(linked_list.linked_list), 1)
        self.assertIsInstance(linked_list.linked_list[0], Node)
        self.assertEqual(linked_list.head.data, {'id': 1})
        self.assertEqual(linked_list.tail.data, {'id': 1})
        self.assertEqual(linked_list.linked_list[0].data, {'id': 1})
        self.assertEqual(linked_list.linked_list[0].next_node, None)

        linked_list.insert_beginning({'id': 0})
        self.assertEqual(len(linked_list.linked_list), 2)
        self.assertIsInstance(linked_list.linked_list[1], Node)
        self.assertEqual(linked_list.head.data, {'id': 0})
        self.assertEqual(linked_list.tail.data, {'id': 1})
        self.assertEqual(linked_list.linked_list[0].data, {'id': 0})
        self.assertEqual(repr(linked_list.linked_list[0].next_node), "Node({'id': 1})")

        linked_list.insert_at_end({'id': 3})
        self.assertEqual(len(linked_list.linked_list), 3)
        self.assertIsInstance(linked_list.linked_list[-1], Node)
        self.assertEqual(linked_list.head.data, {'id': 0})
        self.assertEqual(linked_list.tail.data, {'id': 3})
        self.assertEqual(linked_list.linked_list[-1].data, {'id': 3})
        self.assertEqual(linked_list.linked_list[-1].next_node, None)
        self.assertEqual(repr(linked_list.linked_list[-2].next_node), "Node({'id': 3})")

        linked_list.insert_at_end({'id': 4})
        self.assertEqual(len(linked_list.linked_list), 4)
        self.assertIsInstance(linked_list.linked_list[-1], Node)
        self.assertEqual(linked_list.head.data, {'id': 0})
        self.assertEqual(linked_list.tail.data, {'id': 4})
        self.assertEqual(linked_list.linked_list[-1].data, {'id': 4})
        self.assertEqual(linked_list.linked_list[-1].next_node, None)
        self.assertEqual(repr(linked_list.linked_list[-2].next_node), "Node({'id': 4})")

    def test_str(self):
        linked_list = LinkedList()
        self.assertEqual(str(linked_list), 'None')

        linked_list.insert_beginning({'id': 1})
        linked_list.insert_beginning({'id': 0})

        self.assertEqual(str(linked_list), "{'id': 0} -> {'id': 1} -> None")
