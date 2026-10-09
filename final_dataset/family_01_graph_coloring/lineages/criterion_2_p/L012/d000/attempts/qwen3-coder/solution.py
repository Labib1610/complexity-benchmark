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
    
    # Color array: 0 = unvisited, 1 = color 1, 2 = color 2
    color = [0] * (n + 1)
    
    # Check if bipartite using BFS
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
            
        queue = deque()
        queue.append(start)
        color[start] = 1  # Start with color 1
        
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
    
    # If we reach here, the graph is bipartite
    # The coloring gives us a valid assignment
    # We need the lexicographically smallest one
    # That means we prefer to assign 1 to earlier nodes if possible
    
    # To get the lex smallest, we can just make sure node 1 gets color 1
    # If node 1 got color 2 in our BFS, we flip all colors
    
    if color[1] == 2:
        # Flip all colors
        for i in range(1, n + 1):
            if color[i] == 1:
                color[i] = 2
            else:
                color[i] = 1
    
    print("YES")
    print(" ".join(str(color[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    main()