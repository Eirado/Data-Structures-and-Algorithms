from typing import TypeVar, Generic, Optional

K = TypeVar('K')
V = TypeVar('V')

class Node(Generic[K, V]):
    key: any
    value: any
    next_node: any

    def __init__(self, key: any, value: any, next_node: Optional['Node[K, V]'] = None):
        self.key = key
        self.value = value
        self.next_node = next_node


class SymbolTable(Generic[K, V]):
    def __init__(self):
        self.first: Optional[Node[K, V]] = None

    def get(self, key: any) -> any:

        current = self.first

        while current is not None:

            if key == current.key:dasdasdsa
                return current.value

            current = current.next_node

        return None

    def put(self, key: any, value: any):

        x = self.first

        while x is not None:
            if key == x.key:
                x.value = value
                return
            x = x.next_node

        self.first = Node(key, value, self.first)


def main():
    symbol_table = SymbolTable()

    symbol_table.put('first', 1)
    print(symbol_table.get('first'))


if __name__ == '__main__':
    main()
