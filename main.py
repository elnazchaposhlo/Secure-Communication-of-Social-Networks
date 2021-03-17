from Node import Node
Nodes = []
node_1 = Node('node_1')
Nodes.append(node_1)
node_2 = Node('node_2', node_1)
Nodes.append(node_2)
node_3 = Node('node_3', None, node_2)
Nodes.append(node_3)
node_4 = Node('node_4', node_2)
Nodes.append(node_4)
node_5 = Node('node_5')
Nodes.append(node_5)
node_6 = Node('node_6')
Nodes.append(node_6)
node_7 = Node('node_7', [node_5, node_6], node_4)
Nodes.append(node_7)
node_8 = Node('node_8', node_7)
Nodes.append(node_8)
node_9 = Node('node_9', None, node_8)
Nodes.append(node_9)

node_1.populate_parent(node_2)
node_2.populate_children(node_3)
node_2.populate_parent(node_4)
node_3.populate_parent(node_2)
node_4.populate_children(node_7)
node_5.populate_children(node_6)
node_5.populate_parent(node_7)
node_6.populate_parent(node_7)
node_8.populate_children(node_9)

# for node in Nodes:
#     parent = None
#     children = []
# 
#     if node.parent:
#         parent = node.parent.name
# 
#     if node.children:
#         for c in node.children:
#             children.append(c.name)
# 
#     print("Name: {0}, parent: {1}, children: {2}".format(node.name, parent, children))
