import sys
from collections import defaultdict, deque

def solve():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        # No constraints, assign all to shift 1 (lexicographically smallest)
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array: 0=unvisited, 1=shift 1, 2=shift 2
    color = [0] * (n + 1)
    
    # Check if bipartite using BFS
    for start in range(1, n + 1):
        if color[start] == 0:
            queue = deque()
            color[start] = 1
            queue.append(start)
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                neighbor_color = 3 - current_color  # Because shifts must sum to 3
                
                for neighbor in adj[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = neighbor_color
                        queue.append(neighbor)
                    elif color[neighbor] != neighbor_color:
                        print("NO")
                        return
    
    # If we reach here, a valid assignment exists
    # Generate the lexicographically smallest one
    result = []
    for i in range(1, n + 1):
        if color[i] == 0:
            result.append("1")  # Unconstrained nodes get shift 1
        else:
            result.append(str(color[i]))
    
    print("YES")
    print(" ".join(result))

solve()