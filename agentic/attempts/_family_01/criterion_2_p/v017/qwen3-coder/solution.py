import sys
from collections import defaultdict, deque

def solve():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array: 0 means unvisited, 1 and 2 are the two colors
    color = [0] * (n + 1)
    
    # Check if bipartite using BFS
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 1
        
        while queue:
            node = queue.popleft()
            current_color = color[node]
            next_color = 2 if current_color == 1 else 1
            
            for neighbor in adj[node]:
                if color[neighbor] == 0:
                    color[neighbor] = next_color
                    queue.append(neighbor)
                elif color[neighbor] == current_color:
                    return False
        return True
    
    # Process each connected component
    for i in range(1, n + 1):
        if color[i] == 0:
            if not bfs(i):
                print("NO")
                return
    
    # If we reach here, it's bipartite
    # Ensure lexicographically smallest assignment
    # For each component, if color[1] exists in it, we need to make sure 
    # that the color of node 1 (if in this component) is 1
    # But since we start coloring from node 1, and always assign 1 first,
    # and we're doing BFS which explores in order, this should naturally hold
    
    # Actually, let's re-think: we want the lexicographically smallest sequence
    # That means we want the earliest nodes to have '1' if possible
    # So when we start BFS from an unvisited node, we should try to assign it color 1
    
    # Our current approach already does that since we assign color 1 to the starting node
    
    print("YES")
    print(" ".join(str(color[i]) for i in range(1, n + 1)))

solve()