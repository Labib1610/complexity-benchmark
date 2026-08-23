import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n, m = int(data[0]), int(data[1])
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array: -1 unvisited, 0 -> channel 1, 1 -> channel 2
    color = [-1] * n
    queue = deque()
    
    # Process each component
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            queue.append(i)
            while queue:
                node = queue.popleft()
                current_color = color[node]
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - current_color
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        print("NO")
                        return
    
    # If we reach here, a valid coloring exists
    # We need the lexicographically smallest one
    # Our BFS already ensures that: we start with color 0 for the first unvisited node,
    # which gives the lex smallest coloring since 0 < 1
    
    result = [str(c + 1) for c in color]
    print("YES")
    print(' '.join(result))

if __name__ == "__main__":
    main()