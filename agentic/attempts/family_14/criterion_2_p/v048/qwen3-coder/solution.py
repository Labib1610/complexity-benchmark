import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m, t = map(int, sys.stdin.readline().split())
    priority = set(map(int, sys.stdin.readline().split()))
    
    # If there's only one priority node, we need 0 edges
    if t == 1:
        print(0)
        return

    # Build the tree
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))

    # If t == n, we need all edges
    if t == n:
        total = sum(w for _, _, w in edges)
        print(total)
        return

    # Find the minimal subtree that connects all priority nodes
    # This is the Steiner tree problem on a tree, which can be solved efficiently
    
    # Approach:
    # 1. Pick any priority node as root
    # 2. Do a DFS to compute for each node:
    #    - is_subtree_useful: does the subtree contain any priority node?
    #    - min_cost_to_connect: minimum cost to connect all priority nodes in subtree
    # 3. The answer is min_cost_to_connect[root]

    start = next(iter(priority))
    
    # Build parent pointers and depths via BFS
    parent = {start: None}
    depth = {start: 0}
    bfs_queue = deque([start])
    while bfs_queue:
        u = bfs_queue.popleft()
        for v, w in adj[u]:
            if v not in parent:
                parent[v] = u
                depth[v] = depth[u] + 1
                bfs_queue.append(v)
    
    # Function to find LCA of two nodes
    def lca(u, v):
        while depth[u] > depth[v]:
            u = parent[u]
        while depth[v] > depth[u]:
            v = parent[v]
        while u != v:
            u = parent[u]
            v = parent[v]
        return u

    # Compute pairwise LCAs of priority nodes to build the induced subtree
    # We'll count edge usage in the subtree spanning all priority nodes
    
    # Count how many times each edge is used in the minimal subtree connecting all priority nodes
    # An edge (u, parent[u]) is used if removing it separates the tree into two components,
    # each containing at least one priority node.
    
    # To count this, we can do a tree DP:
    # For each node, count how many priority nodes are in its subtree
    
    # Mark which nodes are priority
    is_priority = [False] * (n + 1)
    for p in priority:
        is_priority[p] = True
        
    # Count priority nodes in subtree rooted at each node
    count_in_subtree = [0] * (n + 1)
    visited = [False] * (n + 1)
    
    # Post-order traversal to compute count_in_subtree
    def dfs_count(node):
        visited[node] = True
        count = 1 if is_priority[node] else 0
        for nei, _ in adj[node]:
            if not visited[nei]:
                count += dfs_count(nei)
        count_in_subtree[node] = count
        return count
    
    dfs_count(start)
    
    # Now traverse the tree again to count edge usage
    edge_usage_count = {}
    visited2 = [False] * (n + 1)
    
    def dfs_edges(node):
        visited2[node] = True
        for nei, w in adj[node]:
            if not visited2[nei]:
                # This edge connects node to nei (going down from node)
                # The subtree is the one rooted at nei
                cnt = count_in_subtree[nei]
                # How many priority nodes are NOT in this subtree?
                not_cnt = t - cnt
                # This edge is used if both cnt >= 1 and not_cnt >= 1
                if cnt >= 1 and not_cnt >= 1:
                    edge_usage_count[(node, nei)] = w
                    edge_usage_count[(nei, node)] = w
                dfs_edges(nei)
                
    dfs_edges(start)
    
    # Sum up all the weights of used edges
    total_weight = sum(set(edge_usage_count.values()))
    
    print(total_weight)

if __name__ == "__main__":
    main()