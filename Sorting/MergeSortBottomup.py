
class MergeSort:

    def sort(self, l: list[int]):

       N = len(l)
       aux = l.copy()
       sz = 1

       while sz < N:

           for lo in range(0, N - sz, 2 * sz):
               mid = lo + sz - 1
               hi = min(lo + 2 * sz - 1, N - 1)
               self.merge(l, aux, lo, mid, hi)
           sz *= 2


    def merge(self, l: list[int], aux: list[int], lo: int, mid: int, hi: int):

        aux[lo:hi + 1] = l[lo:hi + 1]
        i = lo
        j = mid + 1

        for k in range(lo, hi + 1):

            if i > mid:
                l[k] = aux[j]
                j += 1

            elif j > hi:
                l[k] = aux[i]
                i += 1

            elif aux[i] < aux[j]:
                l[k] = aux[i]
                i += 1

            else:
                l[k] = aux[j]
                j += 1


def main():

    merge = MergeSort()
    test_list = [5, 5, 7, 13, 18, 1, 3, 5, 18, 20]

    merge.sort(test_list)

    print(test_list)


if __name__ == '__main__':
    main()
