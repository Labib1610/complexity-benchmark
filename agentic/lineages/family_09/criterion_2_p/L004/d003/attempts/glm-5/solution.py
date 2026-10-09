import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    components = []
    
    for start in range(1, n + 1):
        if color[start] == 0:
            cnt0 = 0
            cnt1 = 0
            members0 = []
            members1 = []
            color[start] = 1
            cnt1 += 1
            members1.append(start)
            q = deque([start])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        if color[v] == 1:
                            cnt1 += 1
                            members1.append(v)
                        else:
                            cnt0 += 1
                            members0.append(v)
                        q.append(v)
            components.append((cnt0, cnt1, members0, members1))
    
    total = sum(max(c[0], c[1]) for c in components)
    if total < k:
        print("NO")
        return
    
    print("YES")
    
    dp = {0: None}
    for idx, (cnt0, cnt1, members0, members1) in enumerate(components):
        new_dp = {}
        for s, parent in dp.items():
            for side in range(2):
                cnt = cnt0 if side == 0 else cnt1
                ns = s + cnt
                if ns <= k and ns not in new_dp:
                    new_dp[ns] = (s, idx, side)
        dp.update(new_dp)
    
    chosen = []
    s = k
    while s > 0:
        parent = dp[s]
        prev_s, comp_idx, side = parent
        comp = components[comp_idx]
        members = comp[2] if side == 0 else comp[3]
        chosen.extend(members)
        s = prev_s
    
    print(' '.join(map(str, chosen)))

solve()