class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def print_ll(self):
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        print(ll_string)

    def to_list(self):
        list_l = []
        node = self.head
        while node:
            list_l.append(node.data)
            node = node.next_node
        return list_l
    def get_data_by_id(self, id):
        node = self.head
        try:
            while node:
                if node.data['id'] == id:
                    return node.data
                node = node.next_node
            return None
        except TypeError:
            print("Данные не являются словарём или в словаре нет id")
