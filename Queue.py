class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return

        self.tail.next_node = node

    def dequeue(self):
        if self.head is None:
            raise Exception('Empty Queue')

        self.head = self.head.next_node

    def print_last_queued_item(self):
        if self.tail:
            print(self.tail.data)

    def print_end_of_queue(self):
        if self.head:
            print(self.head.data)


queue = Queue()

queue.enqueue(Node('joshua'))

queue.print_end_of_queue()
queue.print_last_queued_item()
