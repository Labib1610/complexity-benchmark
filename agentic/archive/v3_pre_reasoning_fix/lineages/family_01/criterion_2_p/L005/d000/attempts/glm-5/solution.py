import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    ptr = 0
    n = int(data[ptr]); ptr += 1
    m = int(data[ptr]); ptr += 1
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[ptr]); ptr += 1
        v = int(data[ptr]); ptr += 1
        adj[u].append(v)
        adj[v].append(u)
    
    assignment = [0] * (n + 1)  # 0 = unassigned, 1 = shift 1, 2 = shift 2
    
    for start in range(1, n + 1):
        if assignment[start] != 0:
            continue
        assignment[start] = 1
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if assignment[v] == 0:
                    assignment[v] = 3 - assignment[u]  # opposite shift
                    queue.append(v)
                elif assignment[v] == assignment[u]:
                    print("NO")
                    return
    
    print("YES")
    print(' '.join(map(str, assignment[1:])))

solve()