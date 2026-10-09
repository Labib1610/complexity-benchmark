import sys
from collections import defaultdict, deque

def solve():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        # No conflicts, assign all to phase 1
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array: 0 = unvisited, 1 = phase 1, 2 = phase 2
    color = [0] * (n + 1)
    
    # Check if bipartite using BFS for each component
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
            
        queue = deque()
        queue.append(start)
        color[start] = 1  # Assign to phase 1
        
        while queue:
            node = queue.popleft()
            current_color = color[node]
            
            for neighbor in adj[node]:
                if color[neighbor] == 0:
                    color[neighbor] = 3 - current_color  # Flip color (1->2, 2->1)
                    queue.append(neighbor)
                elif color[neighbor] == current_color:
                    print("NO")
                    return
    
    # If we get here, it's bipartite
    print("YES")
    result = []
    for i in range(1, n + 1):
        if color[i] == 0:
            result.append("1")  # Isolated node, assign to phase 1
        else:
            result.append(str(color[i]))
    
    print(" ".join(result))

solve()