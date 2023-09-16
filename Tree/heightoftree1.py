# from tkinter import N


class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.right = None
        self.left = None


def Insert(root, val):
    if root is None:
        return Node(val)
    else:
        if val > root.val:
            root.right = Insert(root.right, val)
        elif val < root.val:
            root.left = Insert(root.left, val)
    return root


def height(root):
    p = root
    if p is None:
        return -1
    left_height = height(p.left)
    right_height = height(p.right)
    return 1 + max(left_height, right_height)


if __name__ == '__main__':
    root = Node(2)
    root = Insert(root, 3)
    root = Insert(root, 1)
    root = Insert(root, 0)
    h = height(root)
    print(h)
