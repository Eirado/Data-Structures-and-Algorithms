
def binary_search(key: int, l: list):
    arr_len = len(l)
    lo = 0
    hi = arr_len - 1

    while True:
        for i in range(arr_len):
            mid = lo + (hi - lo) // 2
            if key > l[mid]:
                lo = mid + 1
                continue
            if key < l[mid]:
                hi = mid - 1
                continue
            else:
                return l[mid]

l = [6, 13, 14, 25, 33, 43, 51, 53, 64, 72, 84, 93, 95, 96, 97]
key = 97


print(binary_search(key, l))





