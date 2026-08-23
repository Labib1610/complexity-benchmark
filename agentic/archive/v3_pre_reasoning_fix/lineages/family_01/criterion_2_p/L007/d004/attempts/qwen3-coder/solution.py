import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1  # Convert to 0-indexed
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # For each edge (u,v), we need freq[u] * freq[v] = 2
    # This means exactly one of them is 1 and the other is 2
    
    # This is a 2-SAT problem. Each variable can be true (freq=2) or false (freq=1)
    # For each edge (u,v): (u==1 and v==2) or (u==2 and v==1)
    # Which translates to: (u is true and v is false) or (u is false and v is true)
    # In 2-SAT notation: (u OR v) AND (!u OR !v)
    
    # But let's think differently - this is a bipartite graph coloring problem
    # We want to color vertices with {1,2} such that each edge connects a 1 and a 2
    # This is possible iff the graph is bipartite
    
    color = [-1] * n  # -1: unvisited, 0: color 1, 1: color 2
    
    for start in range(n):
        if color[start] == -1:
            # BFS to check if component is bipartite
            queue = deque([start])
            color[start] = 0
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - current_color
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        print("NO")
                        return
    
    # Graph is bipartite, so we can find a valid assignment
    # Assign colors: 0 -> 1, 1 -> 2
    result = []
    for i in range(n):
        if color[i] == -1:  # Isolated vertex, assign 1
            result.append("1")
        else:
            result.append(str(color[i] + 1))
    
    print("YES")
    print(" ".join(result))

solve()