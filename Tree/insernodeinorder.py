from platform import node


class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.right = None
        self.left = None


def Insert(root, key):
    if root is None:
        return Node(key)

    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = Insert(root.right, key)

        else:
            root.left = Insert(root.left, key)

        return root


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


r = Node(50)
r = Insert(r, 30)
r = Insert(r, 20)
r = Insert(r, 40)
r = Insert(r, 70)
inorder(r)
