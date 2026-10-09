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
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # Color the graph with 2 colors (1 and 2). This is a bipartite check.
    color = [0] * (n + 1)  # 0 means unvisited
    
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
                elif color[neighbor] != next_color:
                    return False
        return True
    
    # Check all components
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        if color[i] == 0:
            if not bfs(i):
                print("NO")
                return
    
    # Verify all edges satisfy the constraint (sum = 3)
    for u, v in edges:
        if color[u] + color[v] != 3:
            print("NO")
            return
    
    # Output the lexicographically smallest solution
    # Since we start with color 1 for each component's root, this gives lex smallest
    print("YES")
    print(" ".join(str(color[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    main()