import node
node_1 = Node(node_2,10)
node_2 = Node([node_1,node_2],node4,10)
node_3 = Node(node_2,10)
node_4 = Node([node_2,node_7],10)
node_5 = Node(node_7,10)
node_6 = Node(node_7,10)
node_7 = Node([node_5,node_6,node_8],node_4,10)
node_8 = Node([node_9],node_7,10)
node_9 = Node(node_8,10)

def get_depth_first_nodes(root):
    nodes = []
    stack = [root]
    while stack:
        cur_node = stack[0]
        stack = stack[1:]
        for child in cur_node.get_rev_children():
            stack.insert(0, child)
        nodes.append(cur_node) 
    return nodes

nodes_list = get_depth_first_nodes(node_4)
for index,curnode in enumerate(node_list):
    curnode.encrypt()
    result = curnode.calculatekeys()
    