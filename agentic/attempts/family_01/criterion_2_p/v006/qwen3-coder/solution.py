import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array: 0 = unvisited, 1 = shift 1, 2 = shift 2
    color = [0] * (n + 1)
    
    # Check if bipartite using BFS for each component
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
            
        # BFS
        queue = deque()
        queue.append(start)
        color[start] = 1  # Assign shift 1 to the starting node
        
        while queue:
            u = queue.popleft()
            current_color = color[u]
            next_color = 2 if current_color == 1 else 1
            
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = next_color
                    queue.append(v)
                elif color[v] == current_color:
                    print("NO")
                    return
    
    # If we reach here, a valid assignment exists
    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    main()