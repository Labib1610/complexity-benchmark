import sys
from collections import defaultdict, deque

def solve():
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    adj = [[] for _ in range(n)]
    
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        idx += 2
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # Color graph with 2 colors (1 and 2)
    color = [0] * n  # 0 means unvisited
    
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 1
        while queue:
            node = queue.popleft()
            current_color = color[node]
            opposite_color = 3 - current_color  # 1->2, 2->1
            for neighbor in adj[node]:
                if color[neighbor] == 0:
                    color[neighbor] = opposite_color
                    queue.append(neighbor)
                elif color[neighbor] != opposite_color:
                    return False
        return True
    
    for i in range(n):
        if color[i] == 0:
            if not bfs(i):
                print("NO")
                return
    
    # Check all edges satisfy the constraint
    for u, v in edges:
        if (color[u] == 1 and color[v] == 1) or (color[u] == 2 and color[v] == 2):
            print("NO")
            return
    
    print("YES")
    print(" ".join(str(c) for c in color))

solve()