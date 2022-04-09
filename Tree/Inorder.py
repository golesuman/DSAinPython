

class Node:
    def __init__(self,data=None) -> None:
        self.data = data
        self.right = None
        self.left = None

def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.data)
        Inorder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print('Inorder traversal of binary tree is')
Inorder(root)