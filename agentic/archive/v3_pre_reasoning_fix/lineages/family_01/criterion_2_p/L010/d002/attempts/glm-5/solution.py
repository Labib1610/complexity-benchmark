import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    ptr = 0
    n = int(data[ptr])
    ptr += 1
    m = int(data[ptr])
    ptr += 1
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[ptr])
        ptr += 1
        v = int(data[ptr])
        ptr += 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * (n + 1)  # -1: unassigned, 0: solvent 1, 1: solvent 2
    
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        queue = deque([start])
        color[start] = 0  # Assign to solvent 1 (lexicographically smallest)
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
    
    print("YES")
    print(" ".join(str(color[i] + 1) for i in range(1, n + 1)))

solve()