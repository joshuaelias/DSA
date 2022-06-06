class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, head=None):
        self.head = head

    def add_head(self, node):
        if self.head is None:
            self.head = node
        else:
            if self.head.right.data > node.data:
                node.right = self.head.right

            if self.head.left.data <= node.data:
                node.left = self.head.left

            self.head = node

    def print_head_data(self):
        if self.head:
            print(self.head.data)
        else:
            raise Exception('List is empty')

    def add_node_recursive(self, node, head=None):
        if head is None:
            head = self.head
        if head:
            if head.data <= node.data:
                if head.right is not None:
                    self.add_node_recursive(node, head.right)
                else:
                    head.right = node
                    return

            if head.data > node.data:
                if head.left is not None:
                    self.add_node_recursive(node, head.left)
                else:
                    head.left = node
                    return
        else:
            raise Exception('List is empty')

    def add_node(self, node):
        self.add_node_recursive(node, self.head)

    def print_tree(self):
        # adjust to return the tree, this is currently only boilerplate
        return self.head


tree = BinarySearchTree()

tree.add_head(Node(10))
tree.add_node(Node(12))
tree.add_node(Node(16))
tree.add_node(Node(7))
tree.add_node(Node(3))
tree.add_node(Node(5))





