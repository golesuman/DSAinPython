# from tkinter import N


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("postorder traversal is:")
postorder(root)
