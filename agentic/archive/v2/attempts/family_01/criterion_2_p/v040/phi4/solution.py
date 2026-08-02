import sys
from collections import defaultdict

def solve():
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    m = int(data[idx+1])
    idx += 2
    
    graph = defaultdict(list)
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        graph[u].append(v)
        graph[v].append(u)
    
    channels = [0] * (n + 1)
    possible = True
    
    def assign(node, ch):
        nonlocal possible
        if channels[node] != 0:
            if channels[node] != ch:
                possible = False
            return
        
        channels[node] = ch
        for neighbor in graph[node]:
            assign(neighbor, 3 - ch)
    
    for i in range(1, n + 1):
        if channels[i] == 0:
            assign(i, 1)
    
    if not possible:
        print("NO")
    else:
        print("YES")
        result = []
        for i in range(1, n + 1):
            result.append(channels[i])
        print(" ".join(map(str, result)))

solve()