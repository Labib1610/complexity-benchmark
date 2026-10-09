import sys
sys.setrecursionlimit(200000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
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
    is_bipartite = True
    components = []
    
    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = 1
            stack = [i]
            comp = []
            while stack:
                u = stack.pop()
                comp.append(u)
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        stack.append(v)
                    elif color[v] == color[u]:
                        is_bipartite = False
            components.append(comp)
    
    if not is_bipartite:
        print("NO")
        return
    
    # DP to find subset sum
    # dp[t] = (c_idx, prev_t) if reachable
    dp = [None] * (k + 1)
    dp[0] = (-1, -1)
    
    for c_idx, comp in enumerate(components):
        cnt1 = sum(1 for u in comp if color[u] == 1)
        cnt2 = len(comp) - cnt1
        sizes = [(cnt1, 1), (cnt2, 2)]
        
        for t in range(k, -1, -1):
            if dp[t] is not None:
                for sz, side in sizes:
                    if t + sz <= k and dp[t + sz] is None:
                        dp[t + sz] = (c_idx, t)
    
    if dp[k] is None:
        print("NO")
        return
    
    # Reconstruct choices
    choice = [0] * len(components)
    curr = k
    while curr > 0:
        c_idx, prev = dp[curr]
        sz = curr - prev
        comp = components[c_idx]
        cnt1 = sum(1 for u in comp if color[u] == 1)
        if sz == cnt1:
            choice[c_idx] = 1
        else:
            choice[c_idx] = 2
        curr = prev
    
    # Build result
    result = []
    for c_idx, comp in enumerate(components):
        side = choice[c_idx]
        for u in comp:
            if color[u] == side:
                result.append(u)
    
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    solve()