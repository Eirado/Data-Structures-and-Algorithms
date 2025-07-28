class Linkedlist:
    def __init__(self, key: any):
        self.key = key
        self.next = None


class MyHashSet:
    capacity = 10 ** 4

    def __init__(self):
        self.set = [Linkedlist(0) for i in range(self.capacity)]

    def add(self, key: int) -> None:
        h = hash(key)
        index = h % self.capacity
        current_node = self.set[index]
        while current_node.next:
            if current_node.next.key == key:
                return
            current_node = current_node.next
        current_node.next = Linkedlist(key)

    def remove(self, key: int) -> None:
        h = hash(key)
        index = h % self.capacity

        current_node = self.set[index]
        while current_node.next:
            if current_node.next.key == key:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def contains(self, key: int) -> bool:
        h = hash(key)
        index = h % self.capacity
        current_node = self.set[index]
        while current_node.next:
            if current_node.next.key == key:
                return True
            current_node = current_node.next
        return False