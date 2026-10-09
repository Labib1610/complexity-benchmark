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
    
    # Build adjacency list for the graph
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array: 0 = unvisited, 1 = shift 1, 2 = shift 2
    color = [0] * (n + 1)
    
    # Check each connected component
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
            
        # BFS to check bipartiteness and assign colors
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
    # Construct the result with lexicographically smallest assignment
    # That means we prefer shift 1 for earlier workers
    # Since our coloring already ensures no conflicts and we started with shift 1,
    # we just need to output the colors
    result = []
    for i in range(1, n + 1):
        result.append(str(color[i]))
    
    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    main()