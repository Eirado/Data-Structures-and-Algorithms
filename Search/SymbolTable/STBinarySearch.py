

class STBinarySearch:

    values = [5,3,6,4,7,8,9,4,6,8]
    keys = ['A', 'C', 'E', 'H', 'L', 'M', 'P', 'R', 'S', 'X']

    def get(self, key):

        rank = self.rank(key)

        if len(self.values) > rank and self.keys[rank] == key:
            return self.values[rank]
        else:
            return None

    def insert(self, key, value):
        rank = self.rank(key)

        if rank < len(self.keys) and self.keys[rank] == key:
            self.values[rank] = value
            print(self.values)
            return

        self.keys.insert(rank, key)
        self.values.insert(rank, value)

        print(self.keys, self.values)


    def rank(self, key):

        hi = len(self.keys) - 1
        lo = 0

        while lo <= hi:

            mid = lo + (hi - lo) // 2

            if key > self.keys[mid]:
                lo = mid + 1
                continue
            elif key < self.keys[mid]:
                hi = mid - 1
                continue
            elif key == self.keys[mid]:
                return mid

        return lo # can be used to insert


def main():
    st = STBinarySearch()
    st.insert('-1', 214124)


if __name__ == '__main__':
    main()