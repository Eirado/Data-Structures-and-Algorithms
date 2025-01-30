from enum import Enum
from typing import Optional

class Queue_node:

    value: any
    next_node = None

    def __init__(self, value, next_node=None):
        self.value = value

class Queue:

    first_node: Queue_node = None
    last_node: Queue_node = None

    def enqueue(self, value):

        if value is None:
            return

        old_node = self.last_node

        self.last_node = Queue_node(value)

        if self.first_node is None:
            self.first_node = self.last_node
            return

        old_node.next_node = self.last_node

    def dequeue(self):
        dequeued = self.first_node.value
        self.first_node = self.first_node.next_node
        return dequeued

    def is_empty(self):
        return self.first_node is None


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
        else:
            if node.left is None and node.right is None:
                node = None
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:  #remove and substitute with the smallest node from the right subtree

                smallest_node: Node = node.right

                while smallest_node.left is not None:
                    smallest_node = smallest_node.left

                node.key = smallest_node.key
                node.value = smallest_node.value

                smallest_node = self._delete(smallest_node, smallest_node.key)
            #OR
            # else: # #remove and substitute with the largest node from the left subtree
            #
            #     largest_node: Node = node.left
            #
            #     while largest_node.right is not None:
            #         largest_node = largest_node.right
            #
            #     node.key = largest_node.key
            #     node.value = largest_node.value
            #
            #     largest_node = self._delete(largest_node, largest_node.key)

        return node

    def _floor(self, node, key):

        if node is None:
            return None

        if key == node.key:
            return node

        if node.key > key:  # have to keep going to the left until you find a node that is less than the original k
            return self._floor(node.left, key)

        t = self._floor(node.right, key)
        if t is not None:
            return t
        else:
            return node

    class OrderBST(Enum):

        preorder = 1
        inorder = 2
        postorder = 3
        levelorder = 4

    preorder_results = []
    inorder_results = []
    postorder_results = []
    levelorder_results = []

    def _preorder(self, node):
        if node is None:
            return

        self.preorder_results.append(node.key)
        self._preorder(node.left)
        self._preorder(node.right)

    def _inorder(self, node):

        if node is None:
            return

        self._inorder(node.left)
        self.inorder_results.append(node.key)
        self._inorder(node.right)

    def _postorder(self, node):

        if node is None:
            return

        self._postorder(node.left)
        self._postorder(node.right)
        self.postorder_results.append(node.key)


    def _level_order(self, node):

        queue = Queue()
        queue.enqueue(node)

        self.__level_order(queue)


    def __level_order(self, queue):

        if queue.is_empty():
            return

        node = queue.dequeue()

        self.levelorder_results.append(node.key)

        if node.left:
            queue.enqueue(node.left)
        if node.right:
             queue.enqueue(node.right)


        self.__level_order(queue)


    def choose_oder(self, n: int):
        if n == 1:
            self._preorder(self.root)
        elif n == 2:
            self._inorder(self.root)
        elif n == 3:
            self._postorder(self.root)
        elif n == 4:
            self._level_order(self.root)

        else:
            print("Default case executed")


def main():
    tree = BST()  # the efficiency will depend on the order that the keys comes in, this is not taking balancing in consideration
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

    # print(tree.get(7))
    # tree.floor(29)
    # tree.delete(7)
    # print(tree.get(7))
    # print(tree.get(14))

    tree.choose_oder(tree.OrderBST.preorder.value)
    tree.choose_oder(tree.OrderBST.inorder.value)
    tree.choose_oder(tree.OrderBST.postorder.value)
    tree.choose_oder(tree.OrderBST.levelorder.value)

    print(tree.preorder_results)
    print(tree.inorder_results)
    print(tree.postorder_results)
    print(tree.levelorder_results)

if __name__ == '__main__':
    main()
