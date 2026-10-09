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
    
    # Color the graph with BFS/DFS to check bipartiteness and get lexicographically smallest coloring
    color = {}
    
    # Process nodes in sorted order to ensure lexicographically smallest result
    nodes = list(range(1, n+1))
    
    for start_node in nodes:
        if start_node not in color:
            # Start BFS coloring
            queue = deque()
            queue.append(start_node)
            color[start_node] = 1  # Start with color 1
            
            while queue:
                u = queue.popleft()
                current_color = color[u]
                next_color = 2 if current_color == 1 else 1
                
                for v in adj[u]:
                    if v not in color:
                        color[v] = next_color
                        queue.append(v)
                    elif color[v] == current_color:
                        print("NO")
                        return
    
    # If we reach here, the graph is bipartite
    # Output the colors in order
    result = []
    for i in range(1, n+1):
        result.append(str(color[i]))
    
    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    main()