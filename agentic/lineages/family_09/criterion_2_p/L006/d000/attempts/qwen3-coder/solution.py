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
    
    # If no edges, we can pick any k nodes
    if m == 0:
        print("YES")
        print(*range(1, k + 1))
        return
    
    # Try to 2-color the graph (check if bipartite)
    color = [-1] * (n + 1)  # -1: unvisited, 0: color A, 1: color B
    bipartite = True
    
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
                        bipartite = False
                        break
                if not bipartite:
                    break
        if not bipartite:
            break
    
    if not bipartite:
        # For non-bipartite graphs, we need to find a maximal independent set
        # This is NP-hard in general, but we can use a greedy approach
        # However, let's first check if we can solve it for bipartite case
        pass
    
    # For bipartite graphs, we can take the larger color class
    if bipartite:
        set_a = [i for i in range(1, n + 1) if color[i] == 0]
        set_b = [i for i in range(1, n + 1) if color[i] == 1]
        
        if len(set_a) >= k:
            print("YES")
            print(*set_a[:k])
            return
        elif len(set_b) >= k:
            print("YES")
            print(*set_b[:k])
            return
        else:
            print("NO")
            return
    
    # For non-bipartite graphs, use greedy approach for maximum independent set
    # This is not optimal but should work for many cases
    degree = [0] * (n + 1)
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
    
    # Greedy: sort nodes by degree (ascending) and try to include them
    nodes = list(range(1, n + 1))
    nodes.sort(key=lambda x: degree[x])
    
    selected = set()
    for node in nodes:
        # Check if node can be added (no neighbors already selected)
        can_add = True
        for neighbor in adj[node]:
            if neighbor in selected:
                can_add = False
                break
        
        if can_add:
            selected.add(node)
            if len(selected) == k:
                print("YES")
                print(*selected)
                return
    
    # If greedy didn't work, try another approach
    # Try selecting nodes with highest degree first (opposite strategy)
    nodes.sort(key=lambda x: degree[x], reverse=True)
    
    selected = set()
    for node in nodes:
        # Check if node can be added
        can_add = True
        for neighbor in adj[node]:
            if neighbor in selected:
                can_add = False
                break
        
        if can_add:
            selected.add(node)
            if len(selected) == k:
                print("YES")
                print(*selected)
                return
    
    print("NO")

solve()