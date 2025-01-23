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


        return self._get(self.root, key)

    def _get(self, node: Node, key):

        while node is not None:
            if node.key > key:
                node = self._get(node.left, key)
            elif node.key < key:
                node = self._get(node.right, key)
            else:
                return node

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


    def floor(self, k):

        x = self._floor(self.root, k)
        if x is None:
            return None

        print(x.key, x.value)
        return x.key


    # def delete(self, key):
    #     return self._delete(self.root, key)
    #
    # def _delete(self, node, key):
    #
    #
    #
    #     while node is not None:
    #
    #         if node.key > key:
    #             node = node.left
    #         elif node.key < key:
    #             node = node.right
    #         else:
    #
    #
    #
    #
    #
    #
    #
    #      return None

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
    tree.put('S', 7)
    tree.put('X', 2)
    tree.put('E', 1)
    tree.put('A', 5)
    tree.put('C', 4)
    tree.put('R', 6)
    tree.put('H', 8)
    tree.put('M', 10)
    print(tree.get('M').value)
    tree.floor('N')

if __name__ == '__main__':
    main()