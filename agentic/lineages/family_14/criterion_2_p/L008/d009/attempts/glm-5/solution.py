import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    R = int(next(it))
    S = int(next(it))
    P = int(next(it))
    
    mandated = [False] * (R + 1)
    for _ in range(P):
        u = int(next(it))
        mandated[u] = True
    
    adj = [[] for _ in range(R + 1)]
    edges = []
    for _ in range(S):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    parent = [0] * (R + 1)
    parent_weight = [0] * (R + 1)
    order = []
    stack = [1]
    parent[1] = 0
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                parent_weight[v] = w
                stack.append(v)
    
    # Process in reverse order (bottom-up)
    # dp[u] = minimum cost to connect all mandated nodes in subtree of u
    #         with u activated
    # cnt[u] = number of mandated nodes in subtree
    dp = [0] * (R + 1)
    cnt = [0] * (R + 1)
    
    for u in reversed(order):
        if mandated[u]:
            cnt[u] = 1
        for v, w in adj[u]:
            if v == parent[u]:
                continue
            cnt[u] += cnt[v]
            if cnt[v] > 0:
                dp[u] += dp[v] + w
    
    # Second DFS: compute answer for each node as root
    # up[u] = cost from parent side (excluding subtree of u)
    # up_cnt[u] = mandated count from parent side
    # total[u] = total cost if u is the highest activated node
    
    up = [0] * (R + 1)
    up_cnt = [0] * (R + 1)
    
    # BFS/stack for top-down
    stack = [1]
    while stack:
        u = stack.pop()
        # Calculate total cost if u is the highest activated node
        total_cost = dp[u] + up[u]
        
        # Prepare for children
        # For each child v, we need:
        # up[v] = up[u] + (dp[u] - dp[v] - w if cnt[v] > 0 else dp[u])
        #         + (w if up_cnt[u] > 0 else 0)
        # up_cnt[v] = up_cnt[u] + (cnt[u] - cnt[v])
        
        # First, compute prefix/suffix for children
        children = []
        for v, w in adj[u]:
            if v == parent[u]:
                continue
            children.append((v, w))
        
        k = len(children)
        if k == 0:
            continue
        
        # Prefix sums
        pref_cnt = [0] * (k + 1)
        pref_dp = [0] * (k + 1)
        for i in range(k):
            v, w = children[i]
            pref_cnt[i+1] = pref_cnt[i] + cnt[v]
            pref_dp[i+1] = pref_dp[i] + (dp[v] + w if cnt[v] > 0 else 0)
        
        # Suffix sums
        suff_cnt = [0] * (k + 1)
        suff_dp = [0] * (k + 1)
        for i in range(k-1, -1, -1):
            v, w = children[i]
            suff_cnt[i] = suff_cnt[i+1] + cnt[v]
            suff_dp[i] = suff_dp[i+1] + (dp[v] + w if cnt[v] > 0 else 0)
        
        # Process each child
        for i in range(k):
            v, w = children[i]
            
            # Mandated count from other children
            other_cnt = pref_cnt[i] + suff_cnt[i+1]
            # Cost from other children
            other_dp = pref_dp[i] + suff_dp[i+1]
            
            # up_cnt for v
            new_up_cnt = up_cnt[u] + other_cnt
            if mandated[u]:
                new_up_cnt += 1
            
            # up cost for v
            new_up = up[u] + other_dp
            if up_cnt[u] > 0:
                new_up += w
            
            up[v] = new_up
            up_cnt[v] = new_up_cnt
            stack.append(v)
    
    # Find the answer
    ans = float('inf')
    for u in range(1, R + 1):
        if cnt[u] + up_cnt[u] == P:
            ans = min(ans, dp[u] + up[u])
    
    print(ans)

solve()