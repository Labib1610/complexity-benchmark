import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

color = [-1] * n
components = []  # each: (list of nodes in color0, list of nodes in color1)

for i in range(n):
    if color[i] == -1:
        color[i] = 0
        q = deque([i])
        c0, c1 = [], []
        while q:
            u = q.popleft()
            if color[u] == 0:
                c0.append(u)
            else:
                c1.append(u)
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    sys.exit()
        components.append((c0, c1))

# Now we have components with two possible choices per component.
# We need to see if we can pick exactly k nodes.
# This is a subset sum problem with small component count? n up to 1e5, but components can be many.
# We can use DP with bitset for feasibility.

total0 = sum(len(c0) for c0, _ in components)
total1 = sum(len(c1) for _, c1 in components)

# We can pick any number from 0..total0 from color0 and 0..total1 from color1.
# But we must pick exactly k total.
# Since we can pick any combination from each component (either all from c0 or all from c1),
# the possible sums are all integers from 0 to n? Not exactly, but we can check.

# Actually, we can pick any number of nodes from each component: either all from c0 or all from c1.
# So the possible totals are sums of choices of sizes from each component.
# This is a subset sum with items = sizes of c0 or c1 per component.

# We'll use bitset DP.
possible = 1  # bit 0 set
for c0, c1 in components:
    a = len(c0)
    b = len(c1)
    # shift by a and by b
    possible = (possible << a) | (possible << b)

if k < len(possible) and (possible >> k) & 1:
    # reconstruct
    chosen = []
    # backtrack
    cur = k
    for c0, c1 in reversed(components):
        a = len(c0)
        b = len(c1)
        # check if cur could come from choosing c0
        if cur >= a and ((possible >> (cur - a)) & 1):
            chosen.extend(c0)
            cur -= a
        else:
            chosen.extend(c1)
            cur -= b
        # remove this component's contribution from possible for next step
        possible = (possible >> a) | (possible >> b)  # not exactly, but we can just track
    # Actually the above reconstruction is tricky; easier: store choices during DP.
    # We'll do a simpler approach: since we only need any valid selection, we can just pick greedily.

    # Simpler: we can just pick from color0 until we reach k, else fill with color1.
    # But that might not always work if components restrict.
    # Let's do proper reconstruction with DP table.

    # We'll redo with a list of possible sets.
    dp = [set() for _ in range(n+1)]
    dp[0].add(())
    for idx, (c0, c1) in enumerate(components):
        a = len(c0)
        b = len(c1)
        new_dp = [set() for _ in range(n+1)]
        for s in range(n+1):
            for comb in dp[s]:
                if s + a <= n:
                    new_dp[s+a].add(comb + (idx, 0))
                if s + b <= n:
                    new_dp[s+b].add(comb + (idx, 1))
        dp = new_dp

    if dp[k]:
        comb = next(iter(dp[k]))
        chosen = []
        for idx, choice in comb:
            if choice == 0:
                chosen.extend(components[idx][0])
            else:
                chosen.extend(components[idx][1])
        print("YES")
        print(" ".join(str(x+1) for x in chosen))
    else:
        print("NO")
else:
    print("NO")