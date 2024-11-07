

class Shell:

    def sort(self, l: list):
        N = len(l)
        h = 4
        for i in range(N):

            for j in range(i, 0, -1):
                if self.less(l[j], l[j - h]):
                    self.exch(l, j, j - h)
                
    def less(self, x: int, y: int):
        return x < y


    def exch(self, l: list, x: int, y: int):
        l[x], l[y] = l[y], l[x]


def main():

    shellSort = Shell()

    shellSort.sort()



if __name__ == '__name__':
    main()