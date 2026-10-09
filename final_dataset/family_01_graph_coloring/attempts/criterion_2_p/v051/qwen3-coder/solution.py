import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        # No constraints, assign all to 1 (lexicographically smallest)
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array: 0 means unvisited, 1 and 2 are the colors
    color = [0] * (n + 1)
    
    # Check if bipartite using BFS for each component
    for start in range(1, n + 1):
        if color[start] == 0:
            # Start BFS coloring
            queue = deque()
            queue.append(start)
            color[start] = 1  # Assign 1 first for lex smallest
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                
                for neighbor in adj[node]:
                    if color[neighbor] == 0:
                        # Assign the opposite color
                        color[neighbor] = 3 - current_color
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        # Conflict found, not bipartite
                        print("NO")
                        return
    
    # If we reach here, it's bipartite. Output the coloring
    print("YES")
    # We need to output colors for nodes 1 to n
    result = []
    for i in range(1, n + 1):
        result.append(str(color[i]))
    print(" ".join(result))

if __name__ == "__main__":
    main()