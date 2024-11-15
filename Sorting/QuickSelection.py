import random


class QuickSelection:

    def selection(self, l: list[int], k: int):

        random.shuffle(l)
        lo = 0
        hi = len(l) - 1

        while hi > lo:

            j = self.partition(l, lo, hi)

            if k == j:
                return l[k]
            elif k < j:
               hi = j - 1
            else:
               lo = j + 1

        return l[k]

    def partition(self, l: list[int], lo: int, hi: int):

        i = lo + 1
        j = hi
        p = l[lo]

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

    quick_selection = QuickSelection()
    test_list = [6, 1, 7, 13, 18, 1, 3, 5, 18, 20]
    print(quick_selection.selection(test_list, 8))

if __name__ == '__main__':
    main()