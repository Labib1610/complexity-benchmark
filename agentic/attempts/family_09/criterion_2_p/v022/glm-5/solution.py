import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    k = int(input_data[idx]); idx += 1
    
    if m == 0:
        if k <= n:
            print("YES")
            print(' '.join(str(i) for i in range(1, k+1)))
        else:
            print("NO")
        return
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n+1)
    components = []
    
    for start in range(1, n+1):
        if color[start] == 0:
            side_a = []
            side_b = []
            color[start] = 1
            side_a.append(start)
            queue = deque([start])
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        if color[v] == 1:
                            side_a.append(v)
                        else:
                            side_b.append(v)
                        queue.append(v)
            components.append((side_a, side_b))
    
    total = len(components)
    dp = [[False] * (k+1) for _ in range(total+1)]
    dp[0][0] = True
    
    for i in range(1, total+1):
        a, b = components[i-1]
        size_a = len(a)
        size_b = len(b)
        for j in range(k+1):
            if dp[i-1][j]:
                if j + size_a <= k:
                    dp[i][j + size_a] = True
                if j + size_b <= k:
                    dp[i][j + size_b] = True
    
    if not dp[total][k]:
        print("NO")
        return
    
    j = k
    chosen = []
    for i in range(total, 0, -1):
        a, b = components[i-1]
        size_a = len(a)
        size_b = len(b)
        if j >= size_a and dp[i-1][j - size_a]:
            chosen.extend(a)
            j -= size_a
        else:
            chosen.extend(b)
            j -= size_b
    
    print("YES")
    print(' '.join(map(str, chosen)))

solve()