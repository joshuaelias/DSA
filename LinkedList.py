class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head

    def append_node(self, node):
        current = self.head
        if current:
            while current.next_node is not None:
                current = current.next_node

            current.next_node = node
            self.tail = current.next_node
        else:
            self.head = node
            self.tail = self.head

    def add_first(self, node):
        node.next_node = self.head
        self.head = node

        if self.head.next_node is None:
            self.tail = self.head

    def add_last(self, node):

        if self.head is None:
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        self.tail = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception('List is empty')

        current = self.head
        if current.data == target_node_data:
            if current.next_node:
                new_node.next_node = current.next_node
                current.next_node = new_node
            else:
                current.next_node = new_node
                self.tail = new_node
            return

        if self.tail.data == target_node_data:
            self.tail.next_node = new_node
            self.tail = new_node
            return

        while current.next_node:
            if current.data == target_node_data:
                new_node = current.next_node
                current.next_node = new_node
                return

        raise Exception("No node with data '%s' found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception('List is empty')

        if self.head.data == target_node_data:
            self.add_first(new_node)

        prev_node = self.head
        current = self.head
        while current.data != target_node_data:
            if current.next_node:
                prev_node = current
                current = current.next_node
            else:
                raise Exception("No node with data '%s' found" % target_node_data)

        new_node.next_node = current
        prev_node.next_node = new_node

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception('List is empty')

        if self.head.data == target_node_data:
            if self.head.next_node:
                self.head = self.head.next_node
            else:
                # only head exists
                self.head = None
                self.tail = None
            return

        prev_node = self.head
        current = self.head

        while current.data != target_node_data:
            if current.next_node:
                prev_node = current
                current = current.next_node
            else:
                raise Exception("No node with data '%s' found" % target_node_data)

        if self.tail.data == current.data:
            prev_node.next_node = None
            self.tail = prev_node
            return

        prev_node.next_node = current.next_node

    def reverse_iterative(self):
        prev = None
        current = self.head

        while current is not None:
            temp = current.next_node
            current.next_node = prev

            if prev is None:
                self.tail = current

            prev = current
            current = temp
        self.head = prev

    def reverse_recursive_util(self, current, prev):

        if current.next_node is None:
            self.head = current
            current.next_node = prev
            return

        temp = current.next_node
        current.next_node = prev

        if prev is None:
            self.tail = current

        self.reverse_recursive_util(temp, current)

    def reverse_recursive(self):
        if self.head is None:
            raise Exception('List is empty')

        self.reverse_recursive_util(self.head, None)


nameList = LinkedList(Node('test'))
