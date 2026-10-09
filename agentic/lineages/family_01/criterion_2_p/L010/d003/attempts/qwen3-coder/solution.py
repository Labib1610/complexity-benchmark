import sys
from collections import defaultdict, deque

def solve():
    import sys
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
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
        index += 2
    
    # Color graph with 2 colors (1 and 2) such that adjacent nodes have sum divisible by 3
    # That means adjacent nodes must be different (since 1+1=2, 2+2=4 not divisible by 3, but 1+2=3 is)
    # So this is a bipartite graph check
    
    color = [-1] * n
    
    for i in range(n):
        if color[i] == -1:
            # BFS to color component
            queue = deque()
            queue.append(i)
            color[i] = 1
            while queue:
                node = queue.popleft()
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 3 - color[node]  # Switch 1->2, 2->1
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        print("NO")
                        return
    
    print("YES")
    print(" ".join(str(c) for c in color))

solve()