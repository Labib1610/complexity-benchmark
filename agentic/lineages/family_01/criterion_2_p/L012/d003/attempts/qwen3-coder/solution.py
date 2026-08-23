import sys
from collections import defaultdict, deque

def solve():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u-1, v-1))  # Convert to 0-indexed
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    
    # If no constraints, all vessels can be state 1
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Color the graph bipartite (2-coloring)
    color = [-1] * n  # -1: unvisited, 0: color 0, 1: color 1
    
    # Check if graph is bipartite
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 0
        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        return True
    
    # Process each connected component
    for i in range(n):
        if color[i] == -1:
            if not bfs(i):
                print("NO")
                return
    
    # Verify all edges have different colors
    for u, v in edges:
        if color[u] == color[v]:
            print("NO")
            return
    
    # Map colors to states to minimize penalty
    # We want as many 1's as possible, especially at the beginning
    # Color 0 -> state 1, Color 1 -> state 2 
    # Or Color 0 -> state 2, Color 1 -> state 1
    # Choose the mapping that gives minimum penalty
    
    # Try both mappings
    option1 = [1 if color[i] == 0 else 2 for i in range(n)]
    option2 = [2 if color[i] == 0 else 1 for i in range(n)]
    
    # Calculate penalties
    def calculate_penalty(states):
        penalty = 0
        for i in range(n):
            penalty += (states[i] - 1) * (2 ** (n - 1 - i))
        return penalty
    
    penalty1 = calculate_penalty(option1)
    penalty2 = calculate_penalty(option2)
    
    if penalty1 <= penalty2:
        result = option1
    else:
        result = option2
    
    print("YES")
    print(" ".join(map(str, result)))

solve()