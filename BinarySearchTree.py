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

    def get_min(self, head=None):
        if head is None:
            head = self.head

        if head:
            while head.left:
                head = head.left
            return head.data
        else:
            self.raise_exception('List is empty')

    def get_max(self, head=None):
        if head is None:
            head = self.head

        if head:
            while head.right:
                head = head.right
            return head.data
        else:
            self.raise_exception('List is empty')

    def raise_exception(self, message):
        raise Exception(message)

    def exists(self, value):
        if self.head is None:
            self.raise_exception('List is empty')

        head = self.head
        while head.data != value:
            if value >= head.data:
                if head.right:
                    head = head.right
                else:
                    return False

            if value < head.data:
                if head.left:
                    head = head.left
                else:
                    return False
        return True

    def inorder(self, vals=None):
        if self.head is None:
            self.raise_exception('List is empty')


tree = BinarySearchTree()

tree.add_head(Node(10))
tree.add_node(Node(12))
tree.add_node(Node(13))
tree.add_node(Node(14))
tree.add_node(Node(9))
tree.add_node(Node(8))
tree.add_node(Node(7))

print(tree.get_min())
print(tree.get_max())

print(tree.exists(10))
