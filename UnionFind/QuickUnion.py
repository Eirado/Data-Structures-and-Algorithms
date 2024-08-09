class QuickUnion:

    def __init__(self, entries: list):
        self.id = entries


    def is_connected(self,p: int, q: int) -> bool:
        if self.find_root(p) == self.find_root(q):
            return True
        else:
            return False
    def find_root(self, x: int): # 6
        while self.id[x] != x:
            x = self.id[x]
        return x

    def unionUF(self, p: int, q: int):

        root_p = self.find_root(p)
        root_q = self.find_root(q)
        self.id[root_p] = root_q
        print(self.id)


def main():
    quick_union = QuickUnion([0,1,2,3,4,5,6,7,8,9])
    quick_union.unionUF(4,3)
    quick_union.unionUF(3, 8)
    quick_union.unionUF(6, 5)
    quick_union.unionUF(9, 4)
    quick_union.unionUF(2, 1)
    print(quick_union.is_connected(8,9))
    print(quick_union.is_connected(5, 4))
    quick_union.unionUF(5, 0)
    quick_union.unionUF(7, 2)
    quick_union.unionUF(6, 1)
    quick_union.unionUF(7, 3)








if __name__ == '__main__':
    main()