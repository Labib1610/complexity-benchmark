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
            color[start] = 1
            queue = deque([start])
            side0 = []
            side1 = [start]
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        if color[v] == 1:
                            side1.append(v)
                        else:
                            side0.append(v)
                        queue.append(v)
            components.append((side0, side1))
    
    total = n + 1
    dp = [False] * (total)
    dp[0] = True
    parent = [-1] * (total)
    choice = [-1] * (total)
    
    for idx, (side0, side1) in enumerate(components):
        size0 = len(side0)
        size1 = len(side1)
        new_dp = [False] * (total)
        new_parent = [-1] * (total)
        new_choice = [-1] * (total)
        for s in range(total):
            if dp[s]:
                if s + size0 < total and not new_dp[s + size0]:
                    new_dp[s + size0] = True
                    new_parent[s + size0] = s
                    new_choice[s + size0] = idx
                if s + size1 < total and not new_dp[s + size1]:
                    new_dp[s + size1] = True
                    new_parent[s + size1] = s
                    new_choice[s + size1] = idx
        dp = new_dp
        parent = new_parent
        choice = new_choice
    
    if not dp[k]:
        sys.stdout.write("NO\n")
        return
    
    selected = [False] * len(components)
    cur = k
    while cur > 0:
        idx = choice[cur]
        selected[idx] = True
        prev = parent[cur]
        side0, side1 = components[idx]
        if cur - prev == len(side0):
            cur = prev
        else:
            cur = prev
    
    result = []
    for idx, (side0, side1) in enumerate(components):
        if selected[idx]:
            if len(side0) > 0:
                result.extend(side0)
            else:
                result.extend(side1)
        else:
            if len(side1) > 0:
                result.extend(side1)
            else:
                result.extend(side0)
    
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, result[:k])) + "\n")

solve()