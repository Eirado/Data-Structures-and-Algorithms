

class Node:
    item: str
    next_node: any

class LinkedQueue:

    first_node = None
    last_node = None
    def enqueue(self, item: str):

        old_node = self.last_node

        self.last_node = Node()
        self.last_node.item = item
        self.last_node.next_node = None

        if self.first_node == None:
            self.first_node = self.last_node
            return

        old_node.next_node = self.last_node

    def dequeue(self):

        dequeued = self.first_node.item
        self.first_node = self.first_node.next_node
        print(dequeued)
        return dequeued

def main():

    linked_queue = LinkedQueue()
    linked_queue.enqueue('a')
    linked_queue.enqueue('b')
    linked_queue.enqueue('c')
    linked_queue.enqueue('d')
    linked_queue.enqueue('e')
    linked_queue.dequeue()
    linked_queue.dequeue()
    linked_queue.dequeue()
    linked_queue.dequeue()
    linked_queue.dequeue()



if __name__ == '__main__':
    main()