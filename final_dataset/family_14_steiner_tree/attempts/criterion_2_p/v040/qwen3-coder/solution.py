import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m, t = map(int, sys.stdin.readline().split())
    critical = set(map(int, sys.stdin.readline().split()))
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v))
    
    # Since the graph is a tree (m = n-1 and connected), we can use Kruskal's algorithm
    # to find the Minimum Spanning Tree. However, we only care about connecting the critical nodes.
    # This is equivalent to finding the Minimum Spanning Tree of the subtree that contains
    # all the critical nodes. This is known as the Steiner Tree problem on trees.
    
    # For a tree, the Steiner tree is found by:
    # 1. Root the tree at any node
    # 2. For each node, compute the "essential" nodes in its subtree
    # 3. A node is essential if it's critical or if it has more than one child subtree containing critical nodes
    # 4. The cost is the sum of weights of edges leading to essential subtrees
    
    # Let's build the adjacency list
    adj = [[] for _ in range(n + 1)]
    for w, u, v in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # We'll do a DFS to compute for each node:
    # - whether its subtree contains any critical node
    # - the minimal cost to connect all critical nodes in its subtree
    visited = [False] * (n + 1)
    
    def dfs(u):
        visited[u] = True
        # critical_count_in_subtree: number of critical nodes in subtree of u
        critical_count_in_subtree = int(u in critical)
        # connections: list of (cost, count) from children subtrees that contain critical nodes
        connections = []
        
        for v, w in adj[u]:
            if not visited[v]:
                child_critical_count, child_cost = dfs(v)
                if child_critical_count > 0:
                    connections.append((w, child_critical_count))
                    critical_count_in_subtree += child_critical_count
        
        # Now calculate the cost for node u
        total_cost = 0
        if len(connections) > 1:
            # Need to connect multiple branches
            # Sum all connection costs
            total_cost = sum(cost for cost, count in connections)
        elif len(connections) == 1:
            # Only one branch, pass up the cost
            total_cost = connections[0][0]
        # If no connections, cost remains 0
        
        return critical_count_in_subtree, total_cost
    
    # Start DFS from node 1 (or any node)
    _, result = dfs(1)
    print(result)

threading.Thread(target=main).start()