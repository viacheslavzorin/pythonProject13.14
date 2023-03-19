import unittest
from scr.linked_list import LinkedList

ll = LinkedList()
ll.insert_beginning({'id': 1})
ll.insert_at_end({'id': 2})
ll.insert_at_end({'id': 3})
ll.insert_at_end([1, 2, 3])
ll.insert_beginning({'id': 0})


class LinkedListTestCase(unittest.TestCase):
    def test_print_ll(self):
        self.assertEqual(ll.print_ll(), print("{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> [1, 2, 3] -> None"))

    def test_to_list(self):
        self.assertEqual(print(ll.to_list()), print("[{'id': 0}, {'id': 1}, {'id': 2}, {'id': 3}, [1, 2, 3]]"))
        self.assertEqual(ll.get_data_by_id(1), {'id': 1})
        self.assertEqual(ll.get_data_by_id(4), None)
