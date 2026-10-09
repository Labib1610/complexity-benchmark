import sys
from collections import defaultdict
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m, t = map(int, sys.stdin.readline().split())
    critical = set(map(int, sys.stdin.readline().split()))
    
    # Since the graph is a tree (n nodes, n-1 edges, connected), we can represent it as adjacency list
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # If there's only one critical node, cost is 0
    if t <= 1:
        print(0)
        return
    
    # We need to find the minimal subtree that connects all critical nodes
    # This is known as the Steiner tree problem on a tree
    
    # For a tree, we can solve this efficiently:
    # 1. Root the tree at any node
    # 2. For each node, compute:
    #    - whether the subtree rooted at this node contains any critical node
    #    - the minimal cost to connect all critical nodes in this subtree
    
    # First, let's root the tree at node 1
    root = 1
    
    # Build parent relationships and children lists via DFS
    children = defaultdict(list)
    parent = {}
    parent_weight = {}  # weight from node to its parent
    
    def dfs(node, par, weight_to_parent):
        parent[node] = par
        parent_weight[node] = weight_to_parent
        for nei, w in graph[node]:
            if nei != par:
                children[node].append(nei)
                dfs(nei, node, w)
                
    dfs(root, -1, 0)
    
    # Now we do a post-order traversal to compute the result
    # For each node u, we compute:
    # reachable[u] = True if subtree of u contains any critical node
    # cost[u] = minimal cost to connect all critical nodes in subtree of u
    
    reachable = {}
    cost = {}
    
    # Post-order traversal
    def compute(node):
        is_critical = (node in critical)
        my_reachable = is_critical
        
        # If leaf and not critical, then not reachable
        if not children[node]:
            reachable[node] = my_reachable
            cost[node] = 0
            return
            
        total_cost = 0
        child_count = 0  # number of children that are reachable
        
        for child in children[node]:
            compute(child)
            if reachable[child]:
                child_count += 1
                total_cost += cost[child]
                # Add the edge from node to child if child is relevant
                total_cost += parent_weight[child]  # since parent_weight[child] stores weight from child to node
                
        # If I'm not critical but none of my children are relevant, I'm not relevant
        if not is_critical and child_count == 0:
            reachable[node] = False
            cost[node] = 0
            return
            
        # If I'm not critical and only one child is relevant, I can pass up that relevance
        if not is_critical and child_count == 1:
            reachable[node] = True
            cost[node] = total_cost
            return
            
        # Otherwise (I'm critical or multiple children are relevant), 
        # I must connect them, so I keep all costs
        reachable[node] = True
        cost[node] = total_cost
    
    compute(root)
    print(cost[root])

threading.Thread(target=main).start()