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
    
    if m != n - 1:
        print("NO")
        return
    
    edges = []
    adj = defaultdict(list)
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        idx += 2
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # Build the tree structure based on the integration order
    # The first node is the root (0-indexed)
    parent = [-1] * n
    children = [[] for _ in range(n)]
    
    # Assume the integration order is the order of edges given
    # We need to determine the parent-child relationships
    # Start with node 0 as the first unit (root)
    visited = [False] * n
    visited[0] = True
    queue = deque([0])
    
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                children[u].append(v)
                queue.append(v)
    
    # Try different permutations using backtracking with pruning
    # But since n can be up to 1000, we need a heuristic approach
    
    # Let's try a greedy approach: place nodes to minimize total length
    # We'll use a BFS-like placement strategy
    
    # For small n, we could try all permutations, but for large n, we need heuristics
    # Let's implement a simple linear arrangement based on BFS ordering
    
    # BFS traversal to get an ordering
    order = []
    visited = [False] * n
    queue = deque([0])
    visited[0] = True
    while queue:
        u = queue.popleft()
        order.append(u)
        # Sort children for deterministic behavior
        for v in sorted(children[u]):
            if not visited[v]:
                visited[v] = True
                queue.append(v)
    
    # Assign positions based on this order
    pos = [0] * n
    for i in range(n):
        pos[order[i]] = i + 1
    
    # Calculate total cost
    total_cost = 0
    for u, v in edges:
        total_cost += abs(pos[u] - pos[v])
    
    if total_cost <= B:
        print("YES")
        print(' '.join(map(str, pos)))
        return
    
    # If the greedy approach fails, try a DFS ordering
    order = []
    visited = [False] * n
    
    def dfs(u):
        visited[u] = True
        order.append(u)
        for v in sorted(children[u]):
            if not visited[v]:
                dfs(v)
                
    visited = [False] * n
    dfs(0)
    
    # Assign positions based on this order
    pos = [0] * n
    for i in range(n):
        pos[order[i]] = i + 1
    
    # Calculate total cost
    total_cost = 0
    for u, v in edges:
        total_cost += abs(pos[u] - pos[v])
    
    if total_cost <= B:
        print("YES")
        print(' '.join(map(str, pos)))
        return
    
    # Try reverse DFS
    order.reverse()
    pos = [0] * n
    for i in range(n):
        pos[order[i]] = i + 1
    
    # Calculate total cost
    total_cost = 0
    for u, v in edges:
        total_cost += abs(pos[u] - pos[v])
    
    if total_cost <= B:
        print("YES")
        print(' '.join(map(str, pos)))
        return
    
    # If all heuristics fail, try a more sophisticated approach
    # For now, let's just say NO if none of the simple approaches work
    print("NO")

if __name__ == "__main__":
    main()