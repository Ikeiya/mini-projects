class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
    
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

node1.add_child(node2)
node1.add_child(node3)
node2.add_child(node4)
node2.add_child(node5)
node3.add_child(node6)
node3.add_child(node7)

layer1 = []
layer2 = []
layer3 = []
layer1.append(node1.data)
for i in range(len(node1.children)):
    layer2.append(node1.children[i].data)
for i in range(len(node2.children)):
    layer3.append(node2.children[i].data)
for i in range(len(node3.children)):
    layer3.append(node3.children[i].data)

def printTree(child):
    tempList = []
    for i in range(len(child.children)):
        tempList.append(child.children[i].data)
    print(tempList)
    for i in range(len(child.children)):
        printTree(child.children[i])

def depthSearch(child, target):
    for i in range(len(child.children)):
        if child.children[i].data == target:
            print("Found")
            break
        else:
            print(child.children[i].data)
            depthSearch(child.children[i], target)

def breathSearch(child, target):
    for i in range(len(child.children)):
        print(child.children[i].data)
        if child.children[i].data == target:
            print("Found")
    for i in range(len(child.children)):
        depthSearch(child.children[i], target)
            
print(node1.data)
printTree(node1)
depthSearch(node1, 7)
breathSearch(node1, 7)