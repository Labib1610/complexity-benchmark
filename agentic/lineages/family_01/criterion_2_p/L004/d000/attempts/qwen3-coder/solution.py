import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
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
    
    # Color array: 0 = unvisited, 1 and 2 are colors
    color = [0] * (n + 1)
    
    # Check if bipartite using BFS for each component
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
            
        queue = deque()
        queue.append(start)
        color[start] = 1  # Start with color 1
        
        while queue:
            node = queue.popleft()
            current_color = color[node]
            next_color = 2 if current_color == 1 else 1
            
            for neighbor in adj[node]:
                if color[neighbor] == 0:
                    color[neighbor] = next_color
                    queue.append(neighbor)
                elif color[neighbor] == current_color:
                    print("NO")
                    return
    
    # If we reach here, it's bipartite
    # Ensure lexicographically smallest by assigning 1 to nodes with no constraints first
    # But since we already did BFS starting from low nodes, and always preferred color 1 first,
    # the coloring should already be lex smallest.
    
    print("YES")
    print(" ".join(str(color[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    main()