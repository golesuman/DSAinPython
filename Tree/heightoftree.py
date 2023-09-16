class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def height(root):
    p = root
    if p is None:
        return -1
    left_height = height(p.left)
    right_height = height(p.right)
    return 1 + max(left_height, right_height)
