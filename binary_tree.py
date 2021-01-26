class BTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def inorder(root):
    """
    Inorder (Left, Root, Right)
    """
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def preorder(root):
    """
    Preorder (Root, Left, Right)
    """
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    """
    Postorder (Left, Right, Root)
    """
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

if __name__ == "__main__":
    root = BTreeNode(1)
    root.left = BTreeNode(2)
    root.right = BTreeNode(3)
    root.left.left = BTreeNode(4)
    root.left.right = BTreeNode(5)
    print("Inorder: ", end="")
    inorder(root)
    print()
    print("Preorder: ", end="")
    preorder(root)
    print()
    print("Postorder: ", end="")
    postorder(root)
    print()