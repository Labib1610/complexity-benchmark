import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(input_data[ptr]) - 1
        ptr += 1
        v = int(input_data[ptr]) - 1
        ptr += 1
        adj[u].append(v)
        adj[v].append(u)
    
    voltage = [0] * n
    
    for start in range(n):
        if voltage[start] != 0:
            continue
        voltage[start] = 1
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if voltage[v] == 0:
                    voltage[v] = 3 - voltage[u]
                    queue.append(v)
                elif voltage[v] == voltage[u]:
                    print("NO")
                    return
    
    print("YES")
    print(" ".join(map(str, voltage)))

solve()