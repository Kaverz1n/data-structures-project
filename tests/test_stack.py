import unittest

from src.stack import Node, Stack


class TestNode(unittest.TestCase):
    def test_init(self):
        data = Node("Данные", None)
        self.assertEqual(data.data, "Данные")
        self.assertEqual(data.next_node, None)
        data_2 = Node("Данные_2", data)
        self.assertEqual(data_2.data, "Данные_2")
        self.assertEqual(data_2.next_node.data, "Данные")

    def test_repr(self):
        data = Node("Данные", None)
        self.assertEqual(str(data), "Node('Данные', None)")


class TestStack(unittest.TestCase):
    def test_init(self):
        stack = Stack()
        self.assertEqual(stack.stack, [])
        self.assertIsInstance(stack.top, object)

    def test_push(self):
        stack = Stack()
        stack.push("Данные")
        self.assertEqual(stack.stack[-1].data, "Данные")
        self.assertEqual(stack.stack[-1].next_node, None)
        self.assertEqual(len(stack.stack), 1)
        self.assertIsInstance(stack.top, object)
        self.assertEqual(str(stack.top), "Node('Данные', None)")
        stack.push("Данные_2")
        self.assertEqual(len(stack.stack), 2)
        self.assertEqual(stack.stack[-1].data, "Данные_2")
        self.assertEqual(stack.stack[-1].next_node, stack.stack[0])
        self.assertIsInstance(stack.top, object)
        self.assertEqual(str(stack.top), "Node('Данные_2', Node('Данные', None))")

    def test_pop(self):
        stack = Stack()
        stack.push("Данные")
        stack.push("Данные_2")
        self.assertEqual(len(stack.stack), 2)
        self.assertEqual(stack.pop(), "Данные_2")
        self.assertEqual(str(stack.top), "Node('Данные', None)")
        self.assertEqual(len(stack.stack), 1)
        self.assertEqual(stack.pop(), "Данные")
        self.assertEqual(stack.top, None)
        self.assertEqual(len(stack.stack), 0)


    def test_repr(self):
        stack = Stack()
        self.assertEqual(str(stack), "Стак данных")
