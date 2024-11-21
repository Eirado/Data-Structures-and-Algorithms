

class BinaryHeap:
    array: list = []
    def __init__(self, l: list):
        self.array = l

    def insert(self, item: int):

        self.array.append(item)
        self.swim(len(self.array) - 1)

    def swim(self, index_k: int):

        while index_k > 1 and self.array[index_k // 2] < self.array[index_k]:
            self.exch(self.array, index_k, index_k // 2)
            index_k = index_k // 2

    def sink(self, index_k):

        N = len(self.array) - 1

        while index_k * 2 < N:

            j = index_k * 2

            if j < N and self.array[j] < self.array[j + 1]:
                j += 1

            if self.array[index_k] > self.array[j]:
                break

            self.exch(self.array, index_k, j)
            index_k = j

    def remove_max(self):

        max_value = self.array[1]

        self.exch(self.array, 1, len(self.array) - 1) # exchange the max which is the 1 by definition with the last one
        self.array.pop(-1)#remove the current that is in the last pos
        self.sink(1)
        return max_value

    def exch(self, l: list, x: int, y: int):
        l[x], l[y] = l[y], l[x]

    def getArray(self):
        return self.array

def main():

    test_list = [None,20, 13, 18, 18, 5, 1, 7, 6, 1, 3]

    heap = BinaryHeap(test_list)
    heap.insert(100)
    max_value = heap.remove_max()
    print(max_value)
    test_list = heap.getArray()
    print(test_list)


if __name__ == '__main__':
    main()