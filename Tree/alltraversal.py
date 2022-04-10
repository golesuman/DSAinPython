class Node:
    def __init__(self,data=None) -> None:
        self.data = data
        self.right = None
        self.left = None

def Insert(root, data):
    if root is None:
        return Node(data)

    else:
        if root.data < data:
            root.right = Insert(root.right, data)
        elif root.data > data:
            root.left = Insert(root.left, data)
    return root

def Preorder(root):
    if root:
        print(root.data)
        Preorder(root.left)
        Preorder(root.right)


def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.data)
        Preorder(root.right)

def Postorder(root):
    if root:
        Postorder(root.left)
        Postorder(root.right)
        print(root.data)
    
    
root = Node(5)
root = Insert(root, 5)
root = Insert(root, 10)
root = Insert(root, 30)
print('-------PreOrder-------')
Preorder(root)
print('-------Inorder------')
Inorder(root)
print('------PostOrder-----')
Postorder(root)

