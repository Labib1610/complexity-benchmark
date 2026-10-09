import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1000000)
    
    n, m, B = map(int, sys.stdin.readline().split())
    
    # Build adjacency list to represent the tree
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Since it's a tree, we can root it at node 1
    # We'll perform BFS to determine parent-child relationships
    parent = [-1] * (n + 1)
    children = defaultdict(list)
    visited = [False] * (n + 1)
    queue = deque([1])
    visited[1] = True
    
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                children[u].append(v)
                queue.append(v)
    
    # Now we have a rooted tree with node 1 as root
    # We need to assign positions to minimize total fiber length
    # Strategy: Use dynamic programming or greedy approach
    # Let's try a greedy approach by placing nodes optimally
    
    # We'll use a different strategy:
    # Try to place nodes in a way that minimizes distances
    # One good heuristic is to do a DFS and place children close to their parents
    
    # But let's think differently:
    # Since we want to minimize sum of |pos[u] - pos[v]| over all edges,
    # this is essentially finding a linear arrangement of a tree that minimizes
    # the sum of edge lengths.
    
    # A known result: for trees, there's an optimal layout that can be found
    # by doing an in-order traversal of a centroid decomposition, or more simply,
    # by doing a DFS and laying out nodes consecutively.
    
    # However, let's try a simple approach:
    # Root the tree at node 1, then do a DFS and assign positions in DFS order
    
    position = [0] * (n + 1)
    order = []
    
    def dfs(u):
        order.append(u)
        for v in children[u]:
            dfs(v)
    
    dfs(1)
    
    # Assign positions 1 to n in the order they were visited
    for i in range(n):
        position[order[i]] = i + 1
    
    # Calculate total cost
    total_cost = 0
    for u, v in edges:
        total_cost += abs(position[u] - position[v])
    
    if total_cost <= B:
        print("YES")
        print(*position[1:])
        return
    
    # If the simple DFS order doesn't work, let's try to optimize
    # Maybe we can rearrange to get better cost
    
    # Let's try a different approach: 
    # Place the tree in a way that minimizes bandwidth
    # This is a classic problem. For trees, one good heuristic is
    # to do a BFS layering and place nodes within layers optimally
    
    # But given time constraints, let's try a smarter DFS layout
    
    # Reset
    position = [0] * (n + 1)
    
    # Try placing nodes to minimize distance
    # Root at center node (centroid) might help
    
    # Find centroid
    def get_size(u, par):
        size[u] = 1
        for v in adj[u]:
            if v != par:
                size[u] += get_size(v, u)
        return size[u]
    
    def find_centroid(u, par, total):
        for v in adj[u]:
            if v != par and size[v] > total // 2:
                return find_centroid(v, u, total)
        return u
    
    size = [0] * (n + 1)
    get_size(1, -1)
    centroid = find_centroid(1, -1, n)
    
    # Now root at centroid
    parent = [-1] * (n + 1)
    children = defaultdict(list)
    visited = [False] * (n + 1)
    queue = deque([centroid])
    visited[centroid] = True
    
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                children[u].append(v)
                queue.append(v)
    
    # DFS ordering again but from centroid
    order = []
    def dfs2(u):
        order.append(u)
        for v in children[u]:
            dfs2(v)
            
    dfs2(centroid)
    
    # Assign positions
    for i in range(n):
        position[order[i]] = i + 1
        
    # Recalculate cost
    total_cost = 0
    for u, v in edges:
        total_cost += abs(position[u] - position[v])
        
    if total_cost <= B:
        print("YES")
        print(*position[1:])
        return
        
    # Still not working. Let's try yet another approach.
    # Just try a simple linear arrangement and see
    
    # Actually, the first DFS approach should be reasonably good.
    # Let's recheck our implementation
    
    # Let's just try the simplest approach that should work:
    # Do a DFS from node 1 and assign positions consecutively
    
    # Reset everything
    position = [0] * (n + 1)
    visited = [False] * (n + 1)
    order = []
    
    def dfs_simple(u):
        visited[u] = True
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                dfs_simple(v)
                
    dfs_simple(1)
    
    for i in range(n):
        position[order[i]] = i + 1
        
    total_cost = 0
    for u, v in edges:
        total_cost += abs(position[u] - position[v])
        
    if total_cost <= B:
        print("YES")
        print(*position[1:])
        return
    else:
        print("NO")

if __name__ == "__main__":
    main()