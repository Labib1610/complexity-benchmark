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
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array: 0 = unvisited, 1 and 2 are the two colors
    color = [0] * (n + 1)
    
    # Check bipartiteness using BFS for each connected component
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
            
        queue = deque()
        queue.append(start)
        color[start] = 1  # Start with color 1
        
        while queue:
            node = queue.popleft()
            
            for neighbor in adj[node]:
                if color[neighbor] == 0:
                    color[neighbor] = 3 - color[node]  # Flip color: 1->2, 2->1
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    print("NO")
                    return
    
    # If we reach here, the graph is bipartite
    print("YES")
    result = []
    for i in range(1, n + 1):
        if color[i] == 1:
            result.append("1")
        else:
            result.append("2")
    print(" ".join(result))

if __name__ == "__main__":
    main()