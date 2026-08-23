import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    graph = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
    
    # For each connected component, we need to check if it's bipartite
    # and find a valid assignment
    
    # Color array: 0 = unvisited, 1 = color 1, 2 = color 2
    color = [0] * (n + 1)
    assignment = [0] * (n + 1)
    
    # Check all components
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
            
        # BFS to check bipartiteness and assign values
        queue = deque([start])
        color[start] = 1
        assignment[start] = 1
        
        while queue:
            node = queue.popleft()
            current_assignment = assignment[node]
            
            # The neighbor must have assignment such that product is 2
            # If current is 1, neighbor must be 2
            # If current is 2, neighbor must be 1
            neighbor_assignment = 2 if current_assignment == 1 else 1
            
            for neighbor in graph[node]:
                if color[neighbor] == 0:
                    color[neighbor] = 1 if color[node] == 2 else 2
                    assignment[neighbor] = neighbor_assignment
                    queue.append(neighbor)
                else:
                    # Check consistency
                    if assignment[neighbor] != neighbor_assignment:
                        print("NO")
                        return
    
    # Verify all edges satisfy the constraint
    for u, v in edges:
        if assignment[u] * assignment[v] != 2:
            print("NO")
            return
    
    print("YES")
    print(" ".join(map(str, assignment[1:])))

solve()