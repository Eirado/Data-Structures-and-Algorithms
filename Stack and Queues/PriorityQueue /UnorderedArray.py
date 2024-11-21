
class PQarray:

    array = []

    def __init__(self, l: list[int]):
        l = self.array

    def push(self, item: int):
        self.array.append(item)


    def remove_max(self):
        max_index = 0
        for i in range(len(self.array)):
            if self.array[i] > self.array[max_index]:
                max_index = i

        self.array[max_index], self.array[-1] = self.array[-1], self.array[max_index]
        return self.array.pop()