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
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Check if solution exists and find it
    # For each edge (u,v), we need s_u^2 + s_v^2 = 5
    # Since s_u, s_v ∈ {1,2}, we have possible sums:
    # 1^2 + 1^2 = 2
    # 1^2 + 2^2 = 5
    # 2^2 + 1^2 = 5
    # 2^2 + 2^2 = 8
    # So we need exactly one of s_u, s_v to be 1 and the other to be 2
    
    # This means the graph must be bipartite
    # Each connected component must be bipartite
    
    color = [0] * (n + 1)  # 0: unvisited, 1: color 1, -1: color -1
    
    # Check if bipartite and assign states
    for start in range(1, n + 1):
        if color[start] == 0:
            queue = deque([start])
            color[start] = 1
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                
                for neighbor in adj[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = -current_color
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        print("NO")
                        return
    
    # Construct the lexicographically smallest solution
    # We want s_i = 1 if color[i] = 1, s_i = 2 if color[i] = -1
    # But we also want lexicographically smallest, so:
    # Assign s_i = 1 if color[i] = 1, s_i = 2 if color[i] = -1
    # OR assign s_i = 2 if color[i] = 1, s_i = 1 if color[i] = -1
    # Choose the one that gives lexicographically smaller sequence
    
    # To get lexicographically smallest, we prefer s_1 = 1 if possible
    result = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if color[i] == 0:
            result[i] = 1  # Isolated vertex, can be either 1 or 2, choose 1 for lex smallest
        elif color[i] == 1:
            result[i] = 1
        else:
            result[i] = 2
    
    # But we need to check if this satisfies the constraint
    # Let's verify with first edge
    valid = True
    for u, v in edges:
        if result[u]**2 + result[v]**2 != 5:
            valid = False
            break
    
    if not valid:
        # Try the other assignment
        for i in range(1, n + 1):
            if color[i] == 0:
                result[i] = 2
            elif color[i] == 1:
                result[i] = 2
            else:
                result[i] = 1
        
        # Verify again
        for u, v in edges:
            if result[u]**2 + result[v]**2 != 5:
                print("NO")
                return
    
    print("YES")
    print(" ".join(map(str, result[1:])))

solve()