import sys
from collections import defaultdict, deque

def solve():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m, k = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # If no edges, we can pick any k nodes
    if m == 0:
        print("YES")
        print(' '.join(map(str, range(1, min(k+1, n+1)))))
        return
    
    # Since the graph is bipartite (as it represents a valid gear system),
    # we can 2-color it. Then pick the larger color class.
    
    color = {}
    visited = set()
    
    # Check if graph is bipartite and find a valid 2-coloring
    def bfs(start):
        queue = deque([start])
        color[start] = 0
        visited.add(start)
        c0_nodes = [start]
        c1_nodes = []
        
        while queue:
            node = queue.popleft()
            current_color = color[node]
            
            for neighbor in adj[node]:
                if neighbor not in visited:
                    color[neighbor] = 1 - current_color
                    visited.add(neighbor)
                    if color[neighbor] == 0:
                        c0_nodes.append(neighbor)
                    else:
                        c1_nodes.append(neighbor)
                    queue.append(neighbor)
                elif color[neighbor] == current_color:
                    # Not bipartite, but problem states it's guaranteed to be
                    pass
        
        return c0_nodes, c1_nodes
    
    # Find all components
    all_c0 = []
    all_c1 = []
    
    for i in range(1, n+1):
        if i not in visited:
            c0_nodes, c1_nodes = bfs(i)
            all_c0.extend(c0_nodes)
            all_c1.extend(c1_nodes)
    
    # Choose the larger independent set
    if len(all_c0) >= k:
        print("YES")
        print(' '.join(map(str, all_c0[:k])))
    elif len(all_c1) >= k:
        print("YES")
        print(' '.join(map(str, all_c1[:k])))
    else:
        # Try to see if there's another way, but since graph is bipartite,
        # max independent set is max(|c0|, |c1|)
        # So if both are < k, then impossible
        print("NO")

solve()