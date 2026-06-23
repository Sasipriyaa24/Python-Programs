# class TreeNode:
#     def __init__(self,val):
#         self.val = val
#         self.left = None
#         self.right = None

# def preorder(root):
#     if root != None:
#         print(root.val, end=" ")
#         preorder(root.left)
#         preorder(root.right)

# def inorder(root):
#     if root != None:
#         inorder(root.left)
#         print(root.val, end=" ")
#         inorder(root.right)

# def postorder(root):
#     if root != None:
#         postorder(root.left)
#         postorder(root.right)
#         print(root.val, end=" ")

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)

# preorder(root)
# print()
# inorder(root)
# print()
# postorder(root)
# print()

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,val):
        newnode=TreeNode(val)
        if self.root == None:
            self.root=newnode
        def insertrec(root):
            if val<root.val:
                if root.left == None:
                    root.left=newnode
                else:
                    insertrec(root.left)
            elif val>root.val:
                if root.right == None:
                    root.right=newnode
                else:
                    insertrec(root.right)
        insertrec(self.root)

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.val,end=" ")
            self.inorder(root.right)
nodes = [18,24,15,55,4,39,17,23]
bst = BST()
for i in nodes:
    bst.insert(i)
bst.inorder(bst.root)
print()
