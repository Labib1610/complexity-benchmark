import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m, t = map(int, sys.stdin.readline().split())
    priorities = set(map(int, sys.stdin.readline().split()))
    
    # Since m = n - 1 and the graph is connected (as per problem statement),
    # it's a tree.
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    # We need to find the minimal subtree that connects all priority nodes.
    # This is the Steiner tree problem on a tree, which can be solved efficiently.
    
    # Approach:
    # 1. Root the tree at any node.
    # 2. For each node, compute:
    #    - is_needed[node]: whether this node is a priority or has a priority descendant
    #    - cost[node]: sum of edge weights needed in the subtree rooted at node
    # 3. DFS traversal to compute these values.
    
    # Let's root the tree at node 1
    root = 1
    
    # Build parent and depth information via BFS
    parent = [-1] * (n + 1)
    depth = [-1] * (n + 1)
    depth[root] = 0
    queue = deque([root])
    parent_edge_weight = [0] * (n + 1)
    
    while queue:
        u = queue.popleft()
        for v, w in adj[u]:
            if depth[v] == -1:
                depth[v] = depth[u] + 1
                parent[v] = u
                parent_edge_weight[v] = w
                queue.append(v)
    
    # Now we perform a DFS to determine which nodes are needed
    # A node is needed if it is a priority node or if it has a priority descendant
    
    # Get all nodes in topological order (post-order DFS)
    visited = [False] * (n + 1)
    post_order = []
    
    def dfs(u):
        visited[u] = True
        for v, w in adj[u]:
            if not visited[v]:
                dfs(v)
        post_order.append(u)
    
    dfs(root)
    
    # is_needed[u] = True if u is needed (is priority or has priority descendant)
    is_needed = [False] * (n + 1)
    for p in priorities:
        is_needed[p] = True
    
    # Process in reverse post-order to propagate "needed" status upwards
    for u in reversed(post_order):
        if is_needed[u]:
            continue
        for v, w in adj[u]:
            if v != parent[u] and is_needed[v]:
                is_needed[u] = True
                break
    
    # Now calculate the total cost
    # We include the edge from u to parent[u] if u is needed and parent[u] is also needed
    total_cost = 0
    for u in range(1, n + 1):
        if is_needed[u] and parent[u] != -1 and is_needed[parent[u]]:
            total_cost += parent_edge_weight[u]
    
    print(total_cost)

if __name__ == "__main__":
    main()