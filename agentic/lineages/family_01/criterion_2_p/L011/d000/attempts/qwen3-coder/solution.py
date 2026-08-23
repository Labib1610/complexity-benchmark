import sys
from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # If no constraints, any assignment works; lex smallest is all 1s
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list for constraints
    adj = defaultdict(list)
    edges = []
    
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-indexed
        v = int(data[index+1]) - 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
        index += 2
    
    # Color each component with BFS/DFS to check bipartiteness
    color = [-1] * n  # -1: unvisited, 0: color A, 1: color B
    
    # For each connected component
    for i in range(n):
        if color[i] == -1:
            queue = deque()
            queue.append(i)
            color[i] = 0
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                opposite_color = 1 - current_color
                
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = opposite_color
                        queue.append(neighbor)
                    elif color[neighbor] != opposite_color:
                        print("NO")
                        return
    
    # Assign values based on color: color 0 -> 1, color 1 -> 2
    result = []
    for c in color:
        if c == 0:
            result.append('1')
        elif c == 1:
            result.append('2')
        else:
            # Isolated node, assign 1 (lexicographically smallest)
            result.append('1')
    
    # Verify all constraints are satisfied
    for u, v in edges:
        if int(result[u]) + int(result[v]) != 3:
            print("NO")
            return
    
    print("YES")
    print(" ".join(result))

solve()