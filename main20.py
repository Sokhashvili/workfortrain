class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def printLeafNodes(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        print(root.value)
    printLeafNodes(root.left)
    printLeafNodes(root.right)
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.right = TreeNode(6)
root.left.left.left = TreeNode(7)

print("Leaf Nodes:")
printLeafNodes(root)