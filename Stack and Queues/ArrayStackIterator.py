import array as arr

class Stack:

    array = arr.array('i', [0])
    N: int = 0

    def push(self, item: int):

        if self.N == len(self.array):
            self.resize(len(self.array) * 2)

        self.array[self.N] = item
        self.N += 1

    def pop(self):

        if 0 < self.N <= len(self.array) // 4:
            self.resize(len(self.array) // 2)

        self.N -= 1
        item = self.array[self.N]
        self.array[self.N] = 0


        if self.N == 0:
            self.array = []
            print('array is empty')
            return

        print(item)
        return item

    def resize(self, capacity):

        new_array = arr.array('i', [0] * capacity)

        for i in range(self.N):
            new_array[i] = self.array[i]

        self.array = new_array


    def __iter__(self):
        return self.Iterator(self.N, self.array)

    class Iterator:

        def __init__(self, N: int, array):
            self.i = N
            self.array = array
        def __iter__(self):
            return self
        def __next__(self):
            if self.i <= 0:
                raise StopIteration
            self.i -= 1
            return self.array[self.i ]



    def print(self):
        print(self.array)

def main():

    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.print()

    for i in stack:
        print(f'iterable: {i}')

    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.print()
    stack.pop()
    stack.print()


if __name__ == '__main__':
    main()
