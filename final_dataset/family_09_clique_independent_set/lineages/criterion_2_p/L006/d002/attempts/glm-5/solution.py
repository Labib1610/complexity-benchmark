import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)
    comp = []
    for start in range(1, n + 1):
        if color[start] == 0:
            color[start] = 1
            q = deque([start])
            cnt0 = 0
            cnt1 = 1
            side0 = []
            side1 = [start]
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        if color[v] == 1:
                            cnt1 += 1
                            side1.append(v)
                        else:
                            cnt0 += 1
                            side0.append(v)
                        q.append(v)
            comp.append((cnt0, cnt1, side0, side1))

    total = sum(max(c0, c1) for c0, c1, _, _ in comp)
    if k > total:
        print("NO")
        return

    # DP over components: track achievable counts using the larger side
    # dp[achievable_count] = (prev_count, choice) where choice in {0,1}
    # choice 0 means pick side0, choice 1 means pick side1
    # We store the count of the larger side for each component
    INF = -1
    dp = [INF] * (k + 1)
    dp[0] = -2  # sentinel meaning start
    parent = [None] * (k + 1)

    for i, (c0, c1, s0, s1) in enumerate(comp):
        big = max(c0, c1)
        small = min(c0, c1)
        # We can pick big or small from this component
        # Process in reverse to avoid using same component twice
        new_dp = [INF] * (k + 1)
        new_parent = [None] * (k + 1)
        for j in range(k + 1):
            if dp[j] != INF:
                if j + big <= k:
                    if new_dp[j + big] == INF:
                        new_dp[j + big] = j
                        new_parent[j + big] = (i, 1 if c1 >= c0 else 0)
                if j + small <= k:
                    if new_dp[j + small] == INF:
                        new_dp[j + small] = j
                        new_parent[j + small] = (i, 0 if c1 >= c0 else 1)
        dp = new_dp
        parent = new_parent

    if dp[k] == INF:
        print("NO")
        return

    # Reconstruct
    choices = {}
    cur = k
    while cur > 0:
        prev, (ci, choice) = dp[cur], parent[cur]
        choices[ci] = choice
        cur = prev

    result = []
    for i, (c0, c1, s0, s1) in enumerate(comp):
        choice = choices.get(i, None)
        if choice is None:
            # pick larger side by default (shouldn't happen if k>0 and we need exactly k)
            if c1 >= c0:
                result.extend(s1)
            else:
                result.extend(s0)
        else:
            if choice == 1:
                result.extend(s1)
            else:
                result.extend(s0)

    # Trim to exactly k (in case we picked extra from last component due to small/big)
    # Actually we picked exactly k via DP, but let's be safe
    result = result[:k]
    print("YES")
    print(' '.join(map(str, result)))

solve()