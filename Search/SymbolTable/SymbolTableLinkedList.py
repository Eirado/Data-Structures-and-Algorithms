from typing import TypeVar, Generic, Optional

T = TypeVar('T')
V = TypeVar('V')

class Node(Generic[T,V]):
    key: T
    value: V
    next_node = None

    def __init__(self, key, value):
        self.key = key
        self.value = value


class SymbolTableLinkedList(Generic[T,V]):
    first_node: Node[T,V] = None

    def insert(self, key, value):

        current_node = self.first_node

        while current_node is not None:

            if current_node.key == key:
                current_node.value = value
                return

            current_node = current_node.next_node

        new_node: Node[T,V] = Node(key, value)
        new_node.next_node = self.first_node
        self.first_node = new_node

    def search(self, key):

        current_node = self.first_node

        while current_node is not None:

            if current_node.key == key:
                print(current_node.value)
                return current_node.value

            current_node = current_node.next_node

        print('Not found')
        return None

def main():

    symbol_table = SymbolTableLinkedList[int, str]()
    symbol_table.insert(1, 'A')
    symbol_table.search(1)
    symbol_table.insert(2, 'B')
    symbol_table.insert(1, 'Z')
    symbol_table.insert(3, 'C')

    symbol_table.search(1)
    symbol_table.search(3)
    symbol_table.search(1323)

if __name__ == '__main__':
    main()