import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    components = []
    is_bipartite = True
    
    setrecursionlimit(1 << 25)
    
    for start in range(1, n+1):
        if color[start] == 0:
            comp = [[], []]
            stack = [(start, 1)]
            color[start] = 1
            while stack:
                node, c = stack.pop()
                comp[c-1].append(node)
                nc = 3 - c
                for nb in adj[node]:
                    if color[nb] == 0:
                        color[nb] = nc
                        stack.append((nb, nc))
                    elif color[nb] == c:
                        is_bipartite = False
            components.append(comp)
    
    if not is_bipartite:
        print("NO")
        return
    
    total = sum(max(len(c[0]), len(c[1])) for c in components)
    if k > total:
        print("NO")
        return
    
    dp = [False] * (k + 1)
    dp[0] = True
    parent = [-1] * (k + 1)
    
    for idx, comp in enumerate(components):
        a = len(comp[0])
        b = len(comp[1])
        for j in range(k, -1, -1):
            if dp[j]:
                if j + a <= k and not dp[j + a]:
                    dp[j + a] = True
                    parent[j + a] = idx
                if j + b <= k and not dp[j + b]:
                    dp[j + b] = True
                    parent[j + b] = idx
    
    if not dp[k]:
        print("NO")
        return
    
    choice = [0] * len(components)
    cur = k
    while cur > 0:
        idx = parent[cur]
        a = len(components[idx][0])
        b = len(components[idx][1])
        if cur >= a and dp[cur - a] and (cur - a == 0 or parent[cur - a] != -1):
            choice[idx] = 0
            cur -= a
        else:
            choice[idx] = 1
            cur -= b
    
    result = []
    for i, comp in enumerate(components):
        result.extend(comp[choice[i]])
    
    print("YES")
    print(' '.join(map(str, result[:k])))

solve()