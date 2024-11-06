

class Selection: # O(Nˆ2)/4

    def sort(self, l: list):

     N = len(l)

     for i in range(N):

        min_index = i
        for j in range(i + 1, N):
            if self.less(l[j], l[min_index]):
                min_index = j
        self.exch(l, i, min_index)
        print(l)

    def less(self, x: int, y: int):
        if x < y:
            return True
        else:
            return False

    def exch(self, l: list, x: int, y: int):

        if l[x] != l[y]:
            l[x], l[y] = l[y], l[x]
        return

def main():
    selection = Selection()

    selection.sort([1,2,42,14,553,2,5,2,34,51,52,124,0])


if __name__ == '__main__':
    main()