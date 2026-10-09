import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2

    # If m == 0, any assignment works. Choose lexicographically smallest.
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return

    # Build adjacency list for constraints
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Color the graph with 2 colors (1 and 2). This is a bipartite check.
    color = [-1] * n

    def bfs(start):
        queue = [start]
        color[start] = 1
        while queue:
            node = queue.pop(0)
            current_color = color[node]
            next_color = 2 if current_color == 1 else 1
            for neighbor in adj[node]:
                if color[neighbor] == -1:
                    color[neighbor] = next_color
                    queue.append(neighbor)
                elif color[neighbor] == current_color:
                    return False
        return True

    # Check if the graph is bipartite
    for i in range(n):
        if color[i] == -1:
            if not bfs(i):
                print("NO")
                return

    # Now check the additional constraint: no u == v in edges
    for u, v in edges:
        if u == v:
            print("NO")
            return

    print("YES")
    print(" ".join(str(c) for c in color))

if __name__ == "__main__":
    main()