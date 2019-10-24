class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def findCeilingFloor(root_node, k, floorNum=None, ceilNum=None):
    if root_node == None:
        return root_node
    if not (floorNum == None) and not (ceilNum == None) and floorNum == k - 1 and ceilNum == k + 1:
        return tuple((floorNum, ceilNum))
    if root_node.value < k:
        

root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

print(findCeilingFloor(root, 8))
# (4, 6)