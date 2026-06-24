class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Bst:
    def __init__(self):
        self.root = None

    def insert(self, val):
        newnode = Node(val)

        if self.root is None:
            self.root = newnode
            return

        def insertat(root):
            if val < root.val:
                if root.left is None:
                    root.left = newnode
                else:
                    insertat(root.left)

            elif val > root.val:
                if root.right is None:
                    root.right = newnode
                else:
                    insertat(root.right)

        insertat(self.root)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=" ")
            self.inorder(root.right)

    def search(self, t, root):
        if root is None:
            return False

        if root.val == t:
            return True

        elif t < root.val:
            return self.search(t, root.left)

        else:
            return self.search(t, root.right)

    def findMin(self, node):
        while node.left:
            node = node.left
        return node

    def deleteNode(self, root, key):
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # Node with one child or no child
            if root.left is None:
                return root.right

            if root.right is None:
                return root.left

            # Node with two children
            successor = self.findMin(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)

        return root


# Driver code
nodes = [10, 7, 18, 29, 25, 24]

bst = Bst()

for i in nodes:
    bst.insert(i)

print("Before deletion:")
bst.inorder(bst.root)

bst.root = bst.deleteNode(bst.root, 18)

print("\nAfter deletion:")
bst.inorder(bst.root)

print("\nSearch 24:", bst.search(24, bst.root))