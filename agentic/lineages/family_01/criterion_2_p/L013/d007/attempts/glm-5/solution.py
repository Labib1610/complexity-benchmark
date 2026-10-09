import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    comp = []
    
    for start in range(1, n + 1):
        if color[start] == 0:
            comp_a = []
            comp_b = []
            color[start] = 1
            comp_a.append(start)
            q = deque([start])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        if color[v] == 1:
                            comp_a.append(v)
                        else:
                            comp_b.append(v)
                        q.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
            comp.append((comp_a, comp_b))
    
    # Precompute factorials
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i-1] * i
    
    # Precompute prefix sums of 1/i!
    pref = [0.0] * (n + 1)
    for i in range(1, n + 1):
        pref[i] = pref[i-1] + 1.0 / fact[i]
    
    # For each component, compute sum of 1/i! for each side
    comp_sums = []
    for comp_a, comp_b in comp:
        sum_a = 0.0
        for x in comp_a:
            sum_a += 1.0 / fact[x]
        sum_b = 0.0
        for x in comp_b:
            sum_b += 1.0 / fact[x]
        comp_sums.append((sum_a, sum_b))
    
    # DP to maximize total score
    # dp[mask] = (best_sum, parent_mask, choice)
    # mask bit 0 = choice for comp 0, etc.
    num_comp = len(comp)
    dp = [None] * (1 << num_comp)
    dp[0] = (0.0, -1, -1)
    
    for mask in range(1 << num_comp):
        if dp[mask] is None:
            continue
        cur_sum, _, _ = dp[mask]
        # Find next component to assign
        # Count bits set
        cnt = 0
        temp = mask
        while temp:
            cnt += temp & 1
            temp >>= 1
        if cnt >= num_comp:
            continue
        i = cnt
        sum_a, sum_b = comp_sums[i]
        # Choice 0: assign comp_a to tier 1
        new_mask = mask | (0 << i)
        if dp[new_mask] is None or dp[new_mask][0] < cur_sum + sum_a:
            dp[new_mask] = (cur_sum + sum_a, mask, 0)
        # Choice 1: assign comp_b to tier 1
        new_mask = mask | (1 << i)
        if dp[new_mask] is None or dp[new_mask][0] < cur_sum + sum_b:
            dp[new_mask] = (cur_sum + sum_b, mask, 1)
    
    final_mask = (1 << num_comp) - 1
    best_sum, parent_mask, choice = dp[final_mask]
    
    # Reconstruct choices
    choices = [0] * num_comp
    mask = final_mask
    while mask != 0:
        _, parent_mask, choice = dp[mask]
        i = bin(parent_mask).count('1')
        choices[i] = choice
        mask = parent_mask
    
    # Build final assignment
    p = [0] * (n + 1)
    for i in range(num_comp):
        comp_a, comp_b = comp[i]
        if choices[i] == 0:
            for x in comp_a:
                p[x] = 1
            for x in comp_b:
                p[x] = 2
        else:
            for x in comp_a:
                p[x] = 2
            for x in comp_b:
                p[x] = 1
    
    print("YES")
    print(' '.join(str(p[i]) for i in range(1, n + 1)))

solve()