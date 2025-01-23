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

        if self.root is None:
            return None

        return self._get(self.root, key)

    def _get(self, node: Node, key):

            if node is None:
                return None

            if node.key > key:
                return self._get(node.left, key)
            elif node.key < key:
                return self._get(node.right, key)
            else:
                return node.value


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


    def floor(self, k):

        x = self._floor(self.root, k)
        if x is None:
            return None

        print(x.key, x.value)
        return x.key


    def delete(self, key):

        if self.root is None:
            return None

        return self._delete(self.root, key)

    def _delete(self, node, key):

        if node is None:
            print('Does not exist')
            return None

        if node.key > key:
            node.left = self._delete(node.left, key)
        elif node.key < key:
            node.right = self._delete(node.right, key)
        else: #
            if node.left is None and node.right is None:
                node = None
            elif node.left is None and node.right is not None:
                node = node.right
            elif node.right is None and node.left is not None:
                node = node.left
            else:

                smallest_node: Node = node.right

                while smallest_node.left is not None:
                    smallest_node = smallest_node.left

                node.key = smallest_node.key
                node.value = smallest_node.value

                smallest_node = self._delete(smallest_node, smallest_node.key)




        return node

    def _floor(self, node, key):

        if node is None:
            return None

        if key == node.key:
            return node

        if node.key > key: # have to keep going to the left until you find a node that is less than the original k
            return self._floor(node.left, key)

        t = self._floor(node.right, key)
        if t is not None:
            return t
        else:
            return node


def main():
    tree = BST() # the efficiency will depend on the order that the keys comes in, this is not taking balancing in consideration
    tree.put(7, 'S')
    tree.put(5, 'X')
    tree.put(20, 'E')
    tree.put(4, 'A')
    tree.put(18, 'C')
    tree.put(25, 'R')
    tree.put(2, 'H')
    tree.put(11, 'M')
    tree.put(19, 'M')
    tree.put(33, 'M')
    tree.put(1, 'M')
    tree.put(3, 'M')
    tree.put(14, 'M')
    tree.put(28, 'M')
    tree.put(12, 'M')
    tree.put(15, 'M')
    tree.put(31, 'M')

    print(tree.get(7))
    tree.floor(29)
    tree.delete(7)
    print(tree.get(7))
    print(tree.get(14))

if __name__ == '__main__':
    main()