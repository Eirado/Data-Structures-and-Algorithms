import random


class Knuth:
    def shuffle(self, l: list[int]):
        N = len(l)
        for i in range(N):
            random_number = random.randrange(i + 1)
            self.exch(l, i, random_number)
            print(l)

    def exch(self, l: list, x: int, y: int):
        l[x], l[y] = l[y], l[x]


def main():
    knuth = Knuth()
    knuth.shuffle([1, 2, 3, 4, 5, 6])


if __name__ == '__main__':
    main()
