from scr.datastr import Node, Stack
import unittest
from scr.custom_queue import Queue


class NodeStackTestCase(unittest.TestCase):
    def est_node_init(self):
        node = Node(10)
        self.assertEqual(node.data, 10)
        self.assertEquel(node.next, None)

    def test_stack_pop(self):
        stack = Stack()
        stack.push("1")
        stack.push("a")
        data = stack.pop()
        self.assertEqual(stack.top.data, '1')
        self.assertEqual(stack.top.next, None)
        self.assertEqual(data, "a")

    def test_stack_push(self):
        stack = Stack()
        stack.push("a")
        self.assertEqual(stack.top.data, "a")
        self.assertEqual(stack.top.next, None)

    def test_stac_init(self):
        stack = Stack()
        self.assertEqual(stack.top, None)

    def test_queue_init(self):
        queue = Queue()
        self.assertEqual(queue.head, None)
        self.assertEqual(queue.tail, None)
    def test_enqueue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.head.data, "data1")
        self.assertEqual(queue.head.next.data, "data2")
        self.assertEqual(queue.tail.data, "data3")
        self.assertEqual(queue.tail.next, None)
