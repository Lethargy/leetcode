# https://leetcode.com/problems/clone-graph/description/

class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# DFS

def cloneGraph(node):
    if not node:
        return None

    clone = {node: Node(node.val)}
    q = [node]

    while q:
        u = q.pop(0)

        for v in u.neighbors:
            if v not in clone:
                clone[v] = Node(v.val)
                q.append(v)
            clone[u].neighbors.append(clone[v])

    return clone[node]