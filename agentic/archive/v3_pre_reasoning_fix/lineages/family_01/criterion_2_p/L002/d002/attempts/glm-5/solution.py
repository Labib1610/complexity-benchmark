import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    ptr = 0
    n = int(data[ptr])
    m = int(data[ptr + 1])
    ptr += 2
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[ptr])
        v = int(data[ptr + 1])
        ptr += 2
        adj[u].append(v)
        adj[v].append(u)
    
    state = [0] * (n + 1)
    
    for start in range(1, n + 1):
        if state[start] != 0:
            continue
        
        queue = deque([start])
        state[start] = 1
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if state[v] == 0:
                    state[v] = 3 - state[u]
                    queue.append(v)
                elif state[v] == state[u]:
                    print("NO")
                    return
    
    print("YES")
    print(' '.join(map(str, state[1:])))

solve()