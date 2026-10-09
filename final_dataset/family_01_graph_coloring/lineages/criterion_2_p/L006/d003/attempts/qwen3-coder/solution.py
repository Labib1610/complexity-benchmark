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
        adj[u].append((v, _))
        adj[v].append((u, _))
        edges.append((u, v))
    
    # For each edge, we have a constraint: one value is twice the other
    # So either s[u] = 1 and s[v] = 2, or s[u] = 2 and s[v] = 1
    # This creates a 2-SAT problem
    
    # We'll use graph coloring approach
    # For each component, we try both colorings
    
    color = [0] * (n + 1)  # 0: unvisited, 1: state 1, 2: state 2, -1: state 2, -2: state 1
    
    def bfs(start):
        queue = deque([start])
        color[start] = 1  # Try starting with state 1
        
        while queue:
            u = queue.popleft()
            current_color = color[u]
            
            for v, edge_idx in adj[u]:
                if current_color == 1:  # u is 1, so v must be 2
                    expected_color = 2
                elif current_color == 2:  # u is 2, so v must be 1
                    expected_color = 1
                else:
                    # This shouldn't happen in our implementation
                    continue
                    
                if color[v] == 0:  # Not visited
                    color[v] = expected_color
                    queue.append(v)
                elif color[v] != expected_color:  # Conflict
                    return False
        return True
    
    # Check if bipartite and satisfies constraints
    visited = [False] * (n + 1)
    
    for i in range(1, n + 1):
        if color[i] == 0 and adj[i]:  # Unvisited node with edges
            # Try coloring starting with 1
            temp_color = color[:]
            temp_color[i] = 1
            queue = deque([i])
            
            valid = True
            while queue and valid:
                u = queue.popleft()
                current_color = temp_color[u]
                
                for v, edge_idx in adj[u]:
                    if current_color == 1:  # u is 1, so v must be 2
                        expected_color = 2
                    else:  # u is 2, so v must be 1
                        expected_color = 1
                        
                    if temp_color[v] == 0:  # Not visited
                        temp_color[v] = expected_color
                        queue.append(v)
                    elif temp_color[v] != expected_color:  # Conflict
                        valid = False
                        break
            
            if valid:
                color = temp_color
            else:
                # Try starting with 2
                temp_color = [0] * (n + 1)
                temp_color[i] = 2
                queue = deque([i])
                
                valid = True
                while queue and valid:
                    u = queue.popleft()
                    current_color = temp_color[u]
                    
                    for v, edge_idx in adj[u]:
                        if current_color == 1:  # u is 1, so v must be 2
                            expected_color = 2
                        else:  # u is 2, so v must be 1
                            expected_color = 1
                            
                        if temp_color[v] == 0:  # Not visited
                            temp_color[v] = expected_color
                            queue.append(v)
                        elif temp_color[v] != expected_color:  # Conflict
                            valid = False
                            break
                
                if valid:
                    color = temp_color
                else:
                    print("NO")
                    return
    
    # Assign default values (1) to isolated nodes
    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = 1
    
    # Verify all constraints
    for u, v in edges:
        if not ((color[u] == 1 and color[v] == 2) or (color[u] == 2 and color[v] == 1)):
            print("NO")
            return
    
    print("YES")
    print(" ".join(str(color[i]) for i in range(1, n + 1)))

solve()