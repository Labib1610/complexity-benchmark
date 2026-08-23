import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
    ptr = 0
    n = int(data[ptr])
    ptr += 1
    m = int(data[ptr])
    ptr += 1
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[ptr])
        v = int(data[ptr + 1])
        ptr += 2
        adj[u].append(v)
        adj[v].append(u)
    
    power = [0] * (n + 1)
    
    for start in range(1, n + 1):
        if power[start] == 0:
            power[start] = 1
            queue = deque([start])
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    required = 3 - power[u]
                    if power[v] == 0:
                        power[v] = required
                        queue.append(v)
                    elif power[v] != required:
                        print("NO")
                        return
    
    print("YES")
    print(" ".join(map(str, power[1:])))

solve()