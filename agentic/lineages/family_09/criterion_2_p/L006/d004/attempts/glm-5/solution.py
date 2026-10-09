import sys
sys.setrecursionlimit(300000)

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
    
    color = [-1] * (n + 1)
    is_bipartite = True
    components = []
    
    for i in range(1, n + 1):
        if color[i] == -1:
            comp = []
            stack = [i]
            color[i] = 0
            while stack:
                u = stack.pop()
                comp.append(u)
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        stack.append(v)
                    elif color[v] == color[u]:
                        is_bipartite = False
            components.append(comp)
    
    if not is_bipartite:
        print("NO")
        return
    
    # DP to check feasibility and reconstruct
    # dp[i] = set of achievable sums using first i components
    # To save memory, use bitset or set
    # Since n <= 100000, Python set is OK
    dp = [set() for _ in range(len(components) + 1)]
    dp[0].add(0)
    
    comp_info = []
    for comp in components:
        cnt0 = sum(1 for u in comp if color[u] == 0)
        cnt1 = len(comp) - cnt0
        comp_info.append((cnt0, cnt1))
    
    for i in range(1, len(components) + 1):
        cnt0, cnt1 = comp_info[i-1]
        for s in dp[i-1]:
            dp[i].add(s + cnt0)
            dp[i].add(s + cnt1)
    
    if k not in dp[len(components)]:
        print("NO")
        return
    
    # Reconstruct: determine which color to pick from each component
    choice = [None] * len(components)  # 0 or 1 indicating which color to pick
    curr = k
    for i in range(len(components), 0, -1):
        cnt0, cnt1 = comp_info[i-1]
        if (curr - cnt0) in dp[i-1]:
            choice[i-1] = 0
            curr -= cnt0
        else:
            choice[i-1] = 1
            curr -= cnt1
    
    # Collect result
    result = []
    for i, comp in enumerate(components):
        target_color = choice[i]
        for u in comp:
            if color[u] == target_color:
                result.append(u)
    
    print("YES")
    print(' '.join(map(str, result)))

solve()