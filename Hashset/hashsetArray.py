
# UNFINISHED

class Hashset:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data: list[any] = [None] * capacity

    def add(self, key: int) -> None:
        h = hash(key)
        index = h % self.capacity

        if self.data[index] is not None:
            if key not in self.data[index]:
                self.data[index].append(key)
        else:
            self.data[index] = [key]

    def remove(self, key: int) -> None:
        h = hash(key)
        index = h % self.capacity

        if self.data[index] is not None:
            if key in self.data[index]:
                self.data[index].remove(key)

    def contains(self, key: int) -> bool:
        h = hash(key)
        index = h % self.capacity

        if self.data[index] is not None and key in self.data[index]:
            return True
        else:
            return False


def main():

    hashset =  Hashset(20)

    randomInput = [1,2,3,4,5,6,7,3,2,2,24,5,34,2]
    for i in randomInput:
        hashset.add(i)

    print(hashset.data)

if __name__ == '__main__':
    main()
