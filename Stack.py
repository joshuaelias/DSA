class StackItem:
    def __init__(self, data, next_item=None, prev_item=None):
        self.data = data
        self.next_item = next_item
        self.prev_item = prev_item


class Stack:
    def __init__(self):
        self.tail = None

    def push(self, data):
        if self.tail is None:
            self.tail = StackItem(data)
            return
        self.tail.next_item = StackItem(data, None, self.tail)
        self.tail = self.tail.next_item

    def pop(self):
        if self.tail is not None:
            self.tail = self.tail.prev_item

    def print_tail(self):
        if self.tail is not None:
            print(self.tail.data)
        else:
            print('Stack is empty')


test_stack = Stack()

test_stack.push('test')
test_stack.print_tail()
