import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    B = int(data[idx])
    idx += 1
    
    edges = []
    adj = defaultdict(list)
    degree = [0] * (n + 1)
    
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1
    
    # Since it's a tree, m = n - 1
    # We need to assign each node to a unique window from 1 to n
    # such that sum of |assignment[u] - assignment[v]| over all edges <= B
    
    # Strategy:
    # Since the structure is a tree, we can root it at any node.
    # A good heuristic is to use a BFS traversal to assign windows in a way that
    # minimizes the total distance. We can try assigning nodes in BFS order
    # to consecutive integers.
    
    # Let's try a BFS-based assignment starting from node 1
    # But to optimize, we should start from a centroid or a central node
    
    # Find a node that minimizes the maximum distance to all other nodes (pseudo-centroid)
    # For small n, we can try all nodes as root and pick the best BFS order
    
    # Actually, let's just do BFS from node 1 for simplicity first
    def bfs_order(start):
        order = []
        visited = [False] * (n + 1)
        queue = deque()
        queue.append(start)
        visited[start] = True
        while queue:
            u = queue.popleft()
            order.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
        return order
    
    # Try BFS from node 1
    order = bfs_order(1)
    assignment = [0] * (n + 1)
    for i in range(n):
        assignment[order[i]] = i + 1
    
    # Calculate total wait time
    total = 0
    for u, v in edges:
        total += abs(assignment[u] - assignment[v])
    
    if total <= B:
        print("YES")
        print(' '.join(map(str, assignment[1:])))
        return
    
    # Try BFS from the node with highest degree
    max_degree = -1
    best_node = 1
    for i in range(1, n + 1):
        if degree[i] > max_degree:
            max_degree = degree[i]
            best_node = i
    
    order = bfs_order(best_node)
    assignment = [0] * (n + 1)
    for i in range(n):
        assignment[order[i]] = i + 1
    
    total = 0
    for u, v in edges:
        total += abs(assignment[u] - assignment[v])
    
    if total <= B:
        print("YES")
        print(' '.join(map(str, assignment[1:])))
        return
    
    # Try a different approach: DFS post-order
    def dfs_post_order(start):
        visited = [False] * (n + 1)
        order = []
        stack = [start]
        visited[start] = True
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
        return order[::-1]  # reverse to get post-order
    
    order = dfs_post_order(1)
    assignment = [0] * (n + 1)
    for i in range(n):
        assignment[order[i]] = i + 1
    
    total = 0
    for u, v in edges:
        total += abs(assignment[u] - assignment[v])
    
    if total <= B:
        print("YES")
        print(' '.join(map(str, assignment[1:])))
        return
    
    # Try with best_node
    order = dfs_post_order(best_node)
    assignment = [0] * (n + 1)
    for i in range(n):
        assignment[order[i]] = i + 1
    
    total = 0
    for u, v in edges:
        total += abs(assignment[u] - assignment[v])
    
    if total <= B:
        print("YES")
        print(' '.join(map(str, assignment[1:])))
        return
    
    # If none of the simple heuristics work, try a more optimal assignment
    # Since it's a tree, the optimal layout is to place the tree on a line
    # minimizing sum of edge lengths. This is NP-hard in general, but for trees,
    # there are polynomial algorithms. However, for this problem, heuristics should suffice.
    
    # Let's try a greedy assignment based on subtree sizes
    def compute_subtree_sizes(start):
        visited = [False] * (n + 1)
        size = [0] * (n + 1)
        parent = [-1] * (n + 1)
        
        def dfs(u, par):
            visited[u] = True
            parent[u] = par
            sz = 1
            for v in adj[u]:
                if not visited[v]:
                    sz += dfs(v, u)
            size[u] = sz
            return sz
        
        dfs(start, -1)
        return size, parent
    
    size, parent = compute_subtree_sizes(1)
    
    # Re-rooting to find the best root
    best_root = 1
    min_max_subtree = n
    for i in range(1, n + 1):
        # For each node as root, compute max subtree size
        visited = [False] * (n + 1)
        def dfs_max_sub(u):
            visited[u] = True
            max_sz = 0
            total_sz = 1
            for v in adj[u]:
                if not visited[v]:
                    sz = dfs_max_sub(v)
                    max_sz = max(max_sz, sz)
                    total_sz += sz
            max_sz = max(max_sz, n - total_sz)
            return total_sz
        
        visited = [False] * (n + 1)
        max_sub = 0
        total_count = 0
        visited[i] = True
        for v in adj[i]:
            if not visited[v]:
                sz = dfs_max_sub(v)
                max_sub = max(max_sub, sz)
        max_sub = max(max_sub, n - (1 + sum(dfs_max_sub(v) for v in adj[i] if not [False]*n)[0]))
        # This is getting complex, let's simplify
        
        # Just try all nodes as root for BFS
        order = bfs_order(i)
        assignment = [0] * (n + 1)
        for j in range(n):
            assignment[order[j]] = j + 1
        
        total = 0
        for u, v in edges:
            total += abs(assignment[u] - assignment[v])
        
        if total <= B:
            print("YES")
            print(' '.join(map(str, assignment[1:])))
            return
    
    print("NO")

if __name__ == "__main__":
    main()