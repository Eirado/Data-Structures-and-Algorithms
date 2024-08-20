import array as arr

class ArrayQueue:

    """
    arrays have to be resized

    I have to keep track of its current position

    Queue - Maintain 2 pointers head and tail

    first item will be tail

    pos of the next item to enter will be tail

    tail has to be < capacity
    """

    array = arr.array('u',[''])
    N: int = 0

    def resize(self, capacity: int):

        new_array = arr.array('u', [''] * capacity)







