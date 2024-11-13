class Merge:
    def __recursive_sort(self, l: list[int], aux: list[int], lo: int, hi: int):

        if lo >= hi:
            return

        mid = lo + (hi - lo) // 2

        self.__recursive_sort(aux, l, lo, mid) # aux in the place of l there is a trick to do not have to copy everything back to l(all the merging is change l anyway)
        self.__recursive_sort(aux, l, mid + 1, hi)

        print(lo, hi)

        self.merge(l, aux, lo, mid, hi)

    def sort(self, l: list[int]):

        aux = l.copy()
        self.__recursive_sort(l, aux, 0, len(l) - 1)

    def merge(self, l: list[int], aux: list[int], lo: int, mid: int, hi: int):

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
    merge = Merge()

    random_list = [1, 2, 4, 5, 4, 7, 4, 7, 8, 456, 74, 584, 3, 634, 7, 34, 3, 534, 734, 73, 23, 532, 5, 2346]

    test = [4, 3, 2, 1]

    #merge.sort(test)
    random_test = [3,2]
    aux = random_test.copy()
    merge.merge(random_test, aux, 0, 0 , 1)

    print(random_test)


if __name__ == '__main__':
    main()
