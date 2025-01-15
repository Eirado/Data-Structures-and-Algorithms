class HeapSort:
    array: list

    def __init__(self, l: list):

        self.array = l

    def sort(self):

        N = len(self.array) - 1
        for i in range(N // 2, 0, -1): # go to every subheap
            self.sink(i, N) # puts it in the heap order which has the largest item first in the array

        while N > 1: # start puting the greater value in its end position, keep track so it does not sink that much and scuff the last position
            self.exch(1, N)
            N -= 1
            self.sink(1, N)

        print(self.array)
    def sink(self, index_k: int, size: int):

        while index_k < size:

            j = index_k * 2

            if j < size and self.array[j] < self.array[j + 1]:
                j += 1

            if j > size or self.array[index_k] > self.array[j]:
                break

            self.exch(index_k, j)

            index_k = j

    def exch(self, x: int, y: int):
        self.array[x], self.array[y] = self.array[y], self.array[x]


def main():

    heap_sort = HeapSort([None, 4,3,4,5,3,534,6,34,6,34,634,6,34,23,5,23,7,43,6,43,534,5,34,4,3,534,5,3])

    heap_sort.sort()

if __name__ == '__main__':
    main()