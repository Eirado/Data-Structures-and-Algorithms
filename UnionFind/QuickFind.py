class QuickFindUF:

    def __init__(self, entries: list):
        self.id = entries


    def connected(self, p: int, q: int):
        if p == q:
            return print('it is connected')
        else:
            return print('not connected')

    def unionUF(self, p: int, q: int):

        if self.id[p] == self.id[q]:
            return print('already connected')

        pid = self.id[p]
        qid = self.id[q]

        for i in range(len(self.id)):
            if self.id[i] == pid:
                self.id[i] = qid


        print(self.id)

def main():
    quick_find = QuickFindUF([0,1,2,3,4,5,6,7,8,9])
    quick_find.unionUF(4,3)
    quick_find.unionUF(3,8)
    quick_find.unionUF(6,5)
    quick_find.unionUF(9, 4)
    quick_find.unionUF(2,1)
    quick_find.unionUF(8, 9)
    quick_find.unionUF(5, 0)
    quick_find.unionUF(7, 2)
    quick_find.unionUF(6, 1)


if __name__ == '__main__':
    main()