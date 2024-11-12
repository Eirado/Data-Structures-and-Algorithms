class Merge:
    def sort(self, l: list[int], aux: list[int], lo: int, hi: int):

        if lo >= hi:
            return

        mid = lo + (hi - lo) // 2

        self.sort(aux, l, lo, mid)
        self.sort(aux, l, mid + 1, hi)

        self.merge(l, aux, lo, mid, hi)

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
    aux = random_list.copy()

    merge.sort(random_list, aux, 0, len(random_list) - 1)

    print(random_list)

if __name__ == '__main__':
    main()
