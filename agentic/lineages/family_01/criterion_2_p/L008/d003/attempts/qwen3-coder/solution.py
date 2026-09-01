import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # For each edge, determine valid code pairs
    # Codes are 1 or 2
    # Frequency = 10 * s_u + s_v
    # Valid if frequency % 3 == 0
    valid_pairs = set()
    for s_u in [1, 2]:
        for s_v in [1, 2]:
            if (10 * s_u + s_v) % 3 == 0:
                valid_pairs.add((s_u, s_v))
    
    # valid_pairs should be {(1,2), (2,1)} since:
    # 10*1+2 = 12 % 3 = 0  ✓
    # 10*2+1 = 21 % 3 = 0  ✓
    # 10*1+1 = 11 % 3 = 2  ✗
    # 10*2+2 = 22 % 3 = 1  ✗
    
    # This is a 2-coloring problem with specific constraints
    # We can model this as a graph where each node can be colored 1 or 2
    # and for each edge (u,v), the pair (color[u], color[v]) must be in valid_pairs
    
    # Since valid_pairs are (1,2) and (2,1), this is equivalent to 
    # coloring the graph such that adjacent nodes have different colors
    # This is a bipartite check
    
    # But we also need to ensure lexicographically smallest assignment
    # So we try to assign 1 to nodes whenever possible
    
    color = [0] * (n + 1)  # 0: unvisited, 1: color 1, 2: color 2
    visited = [False] * (n + 1)
    
    # Check if graph is bipartite and find a valid 2-coloring
    for start in range(1, n + 1):
        if not visited[start]:
            # BFS to color component
            queue = deque()
            queue.append(start)
            color[start] = 1  # Try to assign 1 first for lexicographically smallest
            visited[start] = True
            
            while queue:
                u = queue.popleft()
                current_color = color[u]
                
                # Determine what color neighbors must have
                # If current node has color 1, neighbors must have color 2
                # If current node has color 2, neighbors must have color 1
                required_neighbor_color = 3 - current_color  # 1->2, 2->1
                
                for v in adj[u]:
                    if not visited[v]:
                        color[v] = required_neighbor_color
                        visited[v] = True
                        queue.append(v)
                    else:
                        # Check if the existing color is consistent
                        if color[v] != required_neighbor_color:
                            print("NO")
                            return
    
    # Verify the solution
    for u, v in edges:
        s_u = color[u]
        s_v = color[v]
        if (10 * s_u + s_v) % 3 != 0:
            print("NO")
            return
    
    # Output the solution
    print("YES")
    result = []
    for i in range(1, n + 1):
        if color[i] == 0:  # Isolated vertex, assign 1
            result.append("1")
        else:
            result.append(str(color[i]))
    print(" ".join(result))

solve()