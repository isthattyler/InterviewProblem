class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    def preorder(self):
        print(self.value, end=" ")
        if self.left: 
            self.left.preorder()
        if self.right: 
            self.right.preorder()

def invert(node):
    if node == None:
      return node
    leftTemp = node.left
    node.left = invert(node.right) # Swap left to right
    node.right = invert(leftTemp) # Vice versa
    return node

root = Node('a') 
root.left = Node('b') 
root.right = Node('c') 
root.left.left = Node('d') 
root.left.right = Node('e') 
root.right.left = Node('f') 

print("\n")
print("Before: ")
root.preorder()
# a b d e c f 
print("\n")
invert(root)
print("After:")
root.preorder()
# a c f b e d
print("\n")