import random


class QuickSort:

    def sort(self, l: list[int]):

        random.shuffle(l)
        self.__recursive_sort(l, 0, len(l) - 1)

    def __recursive_sort(self, l: list[int], lo, hi):

        if lo >= hi:
            return

        j = self.partition(l, lo, hi)
        self.__recursive_sort(l, lo, j - 1)
        self.__recursive_sort(l, j + 1, hi)
    def partition(self, l: list[int], lo, hi):

        p = l[lo]  # pivot
        j = hi
        i = lo + 1

        while True:

            while l[i] < p:
                i += 1
                if i == hi:
                    break

            while l[j] > p:
                j -= 1
                if j == lo:
                    break

            if i >= j:
                break

            self.exch(l, i, j)

        self.exch(l, lo, j)

        return j

    def exch(self, l: list[int], x: int, y: int):
        l[x], l[y] = l[y], l[x]


def main():
    quicksort = QuickSort()
    test_list = [6, 1, 7, 13, 18, 1, 3, 5, 18, 20]

    quicksort.sort(test_list)
    print(test_list)


if __name__ == '__main__':
    main()
