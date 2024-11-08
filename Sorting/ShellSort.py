class Shell:

    def sort(self, l: list):
        N = len(l)
        gap = 1  # if start with 0 it will work but is probably less efficient

        while gap < N / 3:
            gap = 3 * gap + 1 # for the 3x + 1  logic

        while gap >= 1:

            for i in range(gap, N):
                for j in range(i, gap - 1, -gap):

                    if self.less(l[j], l[j - gap]):
                        self.exch(l, j, j - gap)
            print(l)
            gap //= 3

    def less(self, x: int, y: int):
        return x < y

    def exch(self, l: list, x: int, y: int):
        l[x], l[y] = l[y], l[x]


def main():
    pass

    shellSort = Shell()

    random_list_1 = [3, 277, 93, 3, 2, 32, 13, 777, 23, 12, 34, 12, 41, 25, 12, 6, 3247, 435, 2, 4, 23, 4, 213, 453,
                     125, 80, 32, 4,
                     94, 423, 5, 31, 531, 90, 4, 12, 5, 12, 51, 325, 345, 43, 5, 345, 43]
    random_list_2 = [3, 22, 14, -1, 31, 10, 7, 25]

    shellSort.sort(random_list_1)


if __name__ == '__main__':
    main()
