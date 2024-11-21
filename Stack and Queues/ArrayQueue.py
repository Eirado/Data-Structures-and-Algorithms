import array as arr

class ArrayQueue:

    """
    arrays have to be resized

    I have to keep track of its current position

    Queue - Maintain 2 pointers head and tail

    first item will be tail

    pos of the next item to enter will be tail

    tail has to be < capacity

    dynamic size - some python workarounds

    """

    array = arr.array('i', [0])

    tail: int = 0
    head: int = 0
    N: int = 0

    def enqueue(self, item: int):


        if self.tail == len(self.array):
            self.resize(len(self.array) * 2)

        self.array[self.tail] = item
        self.tail += 1  # tail will always be at the pos that the next will enter

    def print_array(self):
        print(self.array)

    def dequeue(self):

        item = self.array[self.head]
        self.array[self.head] = 0
        self.head += 1

        if 0 < self.array.count(0) >= (len(self.array) - len(self.array) // 4):
            self.resize(len(self.array) // 2)

        if self.array.count(0) == len(self.array):
            self.array = []
            print('array is empty')
            return

        return item

    def resize(self, capacity: int):

        new_array = arr.array('i', [0] * capacity)

        new_index = 0

        for item in self.array:
            if item != 0:
                new_array[new_index] = item
                new_index += 1

        self.array = new_array
        self.tail = new_index
        self.head = 0

def main():
    array_queue = ArrayQueue()
    array_queue.enqueue(1)
    array_queue.enqueue(2)
    array_queue.enqueue(3)
    array_queue.enqueue(4)
    array_queue.enqueue(5)
    array_queue.print_array()
    array_queue.dequeue()
    array_queue.print_array()
    array_queue.dequeue()
    array_queue.print_array()
    array_queue.dequeue()
    array_queue.print_array()
    array_queue.dequeue()
    array_queue.print_array()
    array_queue.enqueue(3)
    array_queue.enqueue(4)
    array_queue.enqueue(5)
    array_queue.enqueue(6)
    array_queue.print_array()
    array_queue.dequeue()
    array_queue.dequeue()
    array_queue.dequeue()
    array_queue.print_array()

if __name__ == '__main__':
    main()






