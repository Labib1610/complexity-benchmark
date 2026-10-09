import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m, B = map(int, sys.stdin.readline().split())
    
    # Build the tree (graph)
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Since it's a tree, m == n - 1
    if m != n - 1:
        print("NO")
        return
    
    # Find a centroid of the tree
    # First, find a node farthest from node 1
    def bfs_farthest(start):
        visited = [False] * (n + 1)
        queue = deque()
        queue.append((start, -1))  # node, parent
        visited[start] = True
        farthest_node = start
        max_dist = 0
        dist = [0] * (n + 1)
        
        while queue:
            u, parent = queue.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    dist[v] = dist[u] + 1
                    if dist[v] > max_dist:
                        max_dist = dist[v]
                        farthest_node = v
                    queue.append((v, u))
        return farthest_node, dist
    
    # Find diameter endpoints
    end1, _ = bfs_farthest(1)
    end2, dist = bfs_farthest(end1)
    diameter = dist[end2]
    
    # Now we need to assign nodes to positions 1..n to minimize sum of |pos[u] - pos[v]| over all edges
    # Strategy: place the tree nodes onto a line such that the total cost is minimized.
    # A good heuristic is to do a BFS traversal starting from a central node (centroid)
    
    # Find centroid
    def find_centroid():
        sz = [0] * (n + 1)
        def dfs_size(u, parent):
            sz[u] = 1
            for v in adj[u]:
                if v != parent:
                    dfs_size(v, u)
                    sz[u] += sz[v]
        
        dfs_size(1, -1)
        
        def dfs_centroid(u, parent, total):
            for v in adj[u]:
                if v != parent and sz[v] > total // 2:
                    return dfs_centroid(v, u, total)
            if total <= 2 * sz[u]:
                return u
            return -1
        
        centroid = dfs_centroid(1, -1, n)
        return centroid
    
    centroid = find_centroid()
    
    # BFS ordering from centroid
    order = []
    visited = [False] * (n + 1)
    queue = deque()
    queue.append(centroid)
    visited[centroid] = True
    
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
    
    # Assign positions 1 to n in BFS order
    position = [0] * (n + 1)
    for i in range(n):
        position[order[i]] = i + 1
    
    # Calculate total wire length
    total_length = 0
    for u, v in edges:
        total_length += abs(position[u] - position[v])
    
    if total_length <= B:
        print("YES")
        result = [0] * n
        for i in range(1, n + 1):
            result[position[i] - 1] = i
        print(' '.join(map(str, result)))
        return
    
    # Try another approach: DFS linear arrangement
    # This is essentially finding a linear arrangement of a tree minimizing sum of edge lengths
    # It's known that for trees, there exists an optimal linear arrangement which is a DFS preorder
    
    def dfs_order(start):
        visited = [False] * (n + 1)
        order_dfs = []
        stack = [start]
        visited[start] = True
        while stack:
            u = stack.pop()
            order_dfs.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
        return order_dfs
    
    # Try DFS from each node as root
    found = False
    best_position = None
    min_cost = float('inf')
    
    # We'll try a few roots
    candidates = [centroid, end1, end2, 1]
    for root in candidates:
        order_dfs = []
        visited = [False] * (n + 1)
        def dfs(u):
            order_dfs.append(u)
            visited[u] = True
            for v in adj[u]:
                if not visited[v]:
                    dfs(v)
        dfs(root)
        
        pos = [0] * (n + 1)
        for i in range(n):
            pos[order_dfs[i]] = i + 1
            
        cost = 0
        for u, v in edges:
            cost += abs(pos[u] - pos[v])
            
        if cost < min_cost:
            min_cost = cost
            best_position = pos[:]
            
        if cost <= B:
            print("YES")
            res = [0] * n
            for i in range(1, n + 1):
                res[pos[i] - 1] = i
            print(' '.join(map(str, res)))
            return
    
    # Check if even the best arrangement works
    if min_cost <= B:
        print("YES")
        res = [0] * n
        for i in range(1, n + 1):
            res[best_position[i] - 1] = i
        print(' '.join(map(str, res)))
    else:
        print("NO")

if __name__ == "__main__":
    main()