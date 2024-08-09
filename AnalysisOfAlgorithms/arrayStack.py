import array as arr

class ArrayStack: # not a perfect implementation due to skill issue, but the concept is right(array dont accept None)

    array = arr.array('i', [0])
    N: int = 0

    def push(self, num: int):

        if self.N == len(self.array):
            self.resize(len(self.array) * 2)

        self.array[self.N] = num
        self.N += 1

    def pop(self):

        item: int = 0

        if self.array.count(0) == len(self.array):
            self.array = []
            print(self.array)
            return

        if 0 < self.N <= len(self.array) // 4:
            self.resize(len(self.array) // 2)

        self.N -= 1
        item = self.array[self.N]
        self.array[self.N] = 0

        print(item)
        return item

    def resize(self, capacity: int):

        new_array = arr.array('i', [0] * capacity)

        for i in range(self.N):
            new_array[i] = self.array[i]

        self.array = new_array

    def print_stack(self):
        print(self.array)


def main():

    stack = ArrayStack()
    stack.push(2)
    stack.print_stack()
    stack.push(3)
    stack.print_stack()
    stack.push(4)
    stack.print_stack()
    stack.push(5)
    stack.print_stack()
    stack.push(6)
    stack.push(6)
    stack.push(6)
    stack.push(6)
    stack.push(6)
    stack.push(6)
    stack.print_stack()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.print_stack()






if __name__ == '__main__':
    main()