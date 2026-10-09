import sys
from collections import defaultdict, deque

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    adj = defaultdict(list)
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # For each edge (u,v), we need lcm(3*c_u + 1, 3*c_v + 1) = 28
    # Possible values for 3*c + 1: 4 (when c=1) and 7 (when c=2)
    # We need to check which pairs give lcm = 28:
    # lcm(4,4) = 4
    # lcm(4,7) = 28  <-- Valid
    # lcm(7,4) = 28  <-- Valid
    # lcm(7,7) = 7
    
    # So adjacent nodes must have different values
    # This is a bipartite graph check
    
    color = [-1] * (n + 1)
    
    # Check if the graph is bipartite
    for start in range(1, n + 1):
        if color[start] == -1:
            queue = deque([start])
            color[start] = 0
            
            while queue:
                node = queue.popleft()
                
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        print("NO")
                        return
    
    # If bipartite, construct the assignment
    # We want lexicographically smallest assignment
    # Color 0 -> assign 1, Color 1 -> assign 2 (since 4,7 gives lcm=28)
    assignment = [0] * (n + 1)
    for i in range(1, n + 1):
        if color[i] == 0:
            assignment[i] = 1
        else:
            assignment[i] = 2
    
    # Verify the solution
    for u, v in edges:
        val_u = 3 * assignment[u] + 1
        val_v = 3 * assignment[v] + 1
        if lcm(val_u, val_v) != 28:
            print("NO")
            return
    
    print("YES")
    print(" ".join(map(str, assignment[1:])))

solve()