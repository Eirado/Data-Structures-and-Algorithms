
class Insertion: #O(Nˆ2)/2

    def sort(self, l: list):

        N = len(l)
        for i in range(N):
            for j in range(i, 0, -1):

                if self.less(l[j], l[j - 1]):
                    self.exch(l, j, j - 1)
                    print(l)
                else:
                    break

    def less(self, x: int, y: int):
        return x < y

    def exch(self, l: list, x: int, y: int):
        l[x], l[y] = l[y], l[x]

def main():

    insertion = Insertion()
    random_list = [1,2,42,14,553,2,5,2,34,51,52,124,0]
    insertion.sort(random_list)

if __name__ == '__main__':
    main()