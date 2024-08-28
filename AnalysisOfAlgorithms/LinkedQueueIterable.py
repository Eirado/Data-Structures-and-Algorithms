
class Node:

    item: int
    next_node: any

class LinkedQueueIterable:

    first: any = None
    last: any = Node

    def enqueue(self, item: int):

        old_last: any = self.last

        self.last = Node()
        self.last.item = item
        self.last.next_node = None

        if self.first is None:
            self.first = self.last
            return

        old_last.next_node = self.last

    def dequeue(self):

        if self.first is None:
            raise IndexError("Dequeue from empty queue")

        item = self.first.item
        self.first = self.first.next_node
        print(item)
        return item

    def __iter__(self):
        return self.Iterator(self.first)

    class Iterator:
        def __init__(self, first_node: Node):

           self.current_node = first_node

        def __iter__(self):
            return self

        def __next__(self):

            if self.current_node is None:
                raise StopIteration

            item = self.current_node.item
            self.current_node = self.current_node.next_node
            return item

def main():

    queue = LinkedQueueIterable()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    for i in queue:
        print(f'iterable: {i}')

    queue.dequeue()
    queue.dequeue()
    queue.dequeue()





if __name__ == '__main__':
    main()
