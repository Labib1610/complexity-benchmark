import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
        # BFS to check bipartiteness
        color[start] = 1
        queue = deque([start])
        ok = True
        while queue and ok:
            u = queue.popleft()
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    ok = False
                    break
        if not ok:
            print("NO")
            return
    
    # Greedy lexicographically smallest: process 1..n, assign smallest not used by assigned neighbors
    result = [0] * (n + 1)
    for i in range(1, n + 1):
        used = set()
        for v in adj[i]:
            if v < i and result[v] != 0:
                used.add(result[v])
        if 1 not in used:
            result[i] = 1
        else:
            result[i] = 2
    
    print("YES")
    print(' '.join(str(result[i]) for i in range(1, n + 1)))

solve()