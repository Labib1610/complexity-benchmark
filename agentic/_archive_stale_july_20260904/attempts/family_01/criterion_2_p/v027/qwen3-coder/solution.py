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
    
    # Build graph
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array: 0 = unvisited, 1 and 2 are the two colors
    color = [0] * (n + 1)
    
    # Check if bipartite using BFS
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 1
        
        while queue:
            node = queue.popleft()
            current_color = color[node]
            next_color = 3 - current_color  # flips 1->2 and 2->1
            
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
    
    # If we reach here, a valid coloring exists
    # The coloring in 'color' is already the lexicographically smallest 
    # because we assign color 1 to the first unvisited node in each component,
    # and BFS propagates consistently.
    
    print("YES")
    result = []
    for i in range(1, n + 1):
        result.append(str(color[i]))
    print(" ".join(result))

if __name__ == "__main__":
    main()