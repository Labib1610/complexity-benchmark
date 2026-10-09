import sys
from collections import defaultdict, deque

def solve():
    n, m, k = map(int, input().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # If no edges, we can select any k nodes
    if m == 0:
        print("YES")
        print(' '.join(map(str, range(1, k+1))))
        return
    
    # Check if graph is bipartite and find the two sets
    color = [-1] * (n + 1)
    set1, set2 = [], []
    
    def is_bipartite(start):
        queue = deque([start])
        color[start] = 0
        set1.append(start) if color[start] == 0 else set2.append(start)
        
        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    if color[neighbor] == 0:
                        set1.append(neighbor)
                    else:
                        set2.append(neighbor)
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        return True
    
    # Process all components
    visited = [False] * (n + 1)
    all_set1, all_set2 = [], []
    
    for i in range(1, n + 1):
        if not visited[i] and adj[i]:  # Non-isolated node
            set1, set2 = [], []
            color = [-1] * (n + 1)
            
            if not is_bipartite(i):
                # This shouldn't happen according to problem statement
                print("NO")
                return
            
            # Mark all nodes in this component as visited
            for node in set1:
                visited[node] = True
                all_set1.append(node)
            for node in set2:
                visited[node] = True
                all_set2.append(node)
    
    # Add isolated nodes (nodes with no edges) to both sets
    isolated = []
    for i in range(1, n + 1):
        if not adj[i]:  # Isolated node
            isolated.append(i)
    
    # We can put isolated nodes in whichever set is better
    size1 = len(all_set1)
    size2 = len(all_set2)
    
    # Maximum independent set size is max(size1, size2) + isolated nodes
    max_sensors = max(size1, size2) + len(isolated)
    
    if k > max_sensors:
        print("NO")
        return
    
    # Try to take k nodes
    if k <= len(all_set1):
        print("YES")
        print(' '.join(map(str, all_set1[:k])))
    elif k <= len(all_set2):
        print("YES")
        print(' '.join(map(str, all_set2[:k])))
    elif k <= len(all_set1) + len(isolated):
        needed = k - len(all_set1)
        result = all_set1 + isolated[:needed]
        print("YES")
        print(' '.join(map(str, result)))
    elif k <= len(all_set2) + len(isolated):
        needed = k - len(all_set2)
        result = all_set2 + isolated[:needed]
        print("YES")
        print(' '.join(map(str, result)))
    else:
        print("NO")

solve()