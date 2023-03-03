class Node:
    """ Это узел """

    def __init__(self, data, next=None):
        self.data = data  # тут данные
        self.next = next  # тут ссылка на следующий


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        """ Тут добавление элемента """
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None

        s = self.top
        self.top = self.top.next
        return s.data
