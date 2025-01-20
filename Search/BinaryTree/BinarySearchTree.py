from typing import Optional


class Node:

    key: any
    value: any
    left = None
    right = None


    def __init__(self, key, value):

        self.key = key
        self.value = value

class BST:

    root: Node = None

    def get(self, key):

        current_node = self.root
        while current_node is not None:
            if current_node.key > key:
                current_node = current_node.left
                continue
            elif current_node.key < key:
                current_node = current_node.right
                continue
            else:
                return current_node.value

        return None

    def put(self, key, value):
        self.root = self._put(self.root, key, value)

    def _put(self, node, key, value):

        if node is None:
            return Node(key, value)

        if key < node.key:
            node.left = self._put(node.left, key, value)
        elif key > node.key:
            node.right = self._put(node.right, key, value)
        else:
            node.value = value

        return node


def main():
    tree = BST() # the efficiency will depend on the order that the keys comes in, this is not taking balancing in consideration
    tree.put('F', 7)
    tree.put('B', 2)
    tree.put('A', 1)
    tree.put('D', 5)
    tree.put('C', 4)
    tree.put('E', 6)
    tree.put('G', 8)
    print(tree.get('G'))


if __name__ == '__main__':
    main()