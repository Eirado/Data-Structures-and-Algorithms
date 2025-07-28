class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    capacity = 10 ** 4

    def __init__(self):
        self.dict = [ListNode(0, 0) for _ in range(self.capacity)]

    def put(self, key: int, value: int) -> None:
        h = hash(key)
        index = h % self.capacity

        cur_node = self.dict[index]

        while cur_node.next:
            if cur_node.next.key == key:
                cur_node.next.value = value
                return
            cur_node = cur_node.next

        cur_node.next = ListNode(key, value)

    def get(self, key: int) -> int:
        h = hash(key)
        index = h % self.capacity

        cur_node = self.dict[index]

        while cur_node.next:
            if cur_node.next.key == key:
                return cur_node.next.value
            cur_node = cur_node.next
        return -1

    def remove(self, key: int) -> None:
        h = hash(key)
        index = h % self.capacity

        cur_node = self.dict[index]

        while cur_node.next:
            if cur_node.next.key == key:
                cur_node.next = cur_node.next.next
                return
            cur_node = cur_node.next

