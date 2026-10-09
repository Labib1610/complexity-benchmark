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
    
    # Color array: 0 = unvisited, 1 = shift 1, 2 = shift 2
    color = [0] * (n + 1)
    
    # Check if bipartite using BFS
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
            
        queue = deque()
        queue.append(start)
        color[start] = 1  # Assign shift 1 to the starting node
        
        while queue:
            u = queue.popleft()
            
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - color[u]  # Assign opposite shift
                    queue.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
    
    # If we reach here, a valid assignment exists
    print("YES")
    result = []
    for i in range(1, n + 1):
        if color[i] == 0:
            result.append("1")
        else:
            result.append(str(color[i]))
    print(" ".join(result))

if __name__ == "__main__":
    main()