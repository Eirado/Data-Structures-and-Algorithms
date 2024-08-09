
#Stack using a linkedList
class Node:
    string: str
    next_node: any
class StackOfStrings:

    first_node = None

    def isEmpty(self):
        if self.first_node == None:
            return True
        else:
            return False
    def push(self, item: str):

        old_node = self.first_node
        self.first_node = Node()
        self.first_node.string = item
        self.first_node.next_node = old_node

    def pop(self):

        print(self.first_node.string)
        self.first_node = self.first_node.next_node



def main():

    stack = StackOfStrings()
    print(stack.isEmpty())
    stack.push("5")
    stack.push("4")
    stack.push("3")
    stack.push("2")
    stack.pop()
    stack.pop()
    stack.push("1")
    print(stack.isEmpty())
    stack.pop()
    stack.pop()
    stack.pop()
    print(stack.isEmpty())


if __name__ == "__main__":
    main()