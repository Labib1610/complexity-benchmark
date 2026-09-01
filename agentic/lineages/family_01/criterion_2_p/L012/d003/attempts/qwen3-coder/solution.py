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
    
    # Try to 2-color the graph with constraints
    # Each component must be bipartite
    # Color 0 means s=1, Color 1 means s=2
    color = [-1] * (n + 1)
    result = [0] * (n + 1)  # 0 means s=1, 1 means s=2
    
    for start in range(1, n + 1):
        if color[start] == -1:
            # BFS to color this component
            queue = deque([start])
            color[start] = 0
            result[start] = 0  # s=1
            
            while queue:
                node = queue.popleft()
                
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        # Assign the opposite value (1->2 or 2->1)
                        # If current node has value 1, neighbor must have 2
                        # If current node has value 2, neighbor must have 1
                        if result[node] == 0:  # node=1
                            result[neighbor] = 1  # neighbor=2
                        else:  # node=2
                            result[neighbor] = 0  # neighbor=1
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    else:
                        # Check consistency
                        # One must be 1, other must be 2
                        if (result[node] == 0 and result[neighbor] == 0) or \
                           (result[node] == 1 and result[neighbor] == 1):
                            print("NO")
                            return
    
    # Verify all edges satisfy the constraint
    for u, v in edges:
        s_u = 1 if result[u] == 0 else 2
        s_v = 1 if result[v] == 0 else 2
        if not ((s_u == 1 and s_v == 2) or (s_u == 2 and s_v == 1)):
            print("NO")
            return
    
    print("YES")
    answer = []
    for i in range(1, n + 1):
        answer.append("1" if result[i] == 0 else "2")
    print(" ".join(answer))

solve()