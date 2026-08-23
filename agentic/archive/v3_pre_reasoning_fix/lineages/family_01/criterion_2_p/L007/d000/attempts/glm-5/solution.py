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
    
    shift = [0] * (n + 1)
    
    for start in range(1, n + 1):
        if shift[start] != 0:
            continue
        shift[start] = 1
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if shift[v] == 0:
                    shift[v] = 3 - shift[u]
                    queue.append(v)
                elif shift[v] == shift[u]:
                    print("NO")
                    return
    
    print("YES")
    print(' '.join(map(str, shift[1:])))

solve()