import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    g = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        g[u].append(v)
        g[v].append(u)

    colour = [-1] * n
    comps0 = []          # list of vertices of colour 0 per component
    comps1 = []          # list of vertices of colour 1 per component
    a = []               # sizes
    b = []

    for start in range(n):
        if colour[start] != -1:
            continue
        q = deque([start])
        colour[start] = 0
        cur0 = []
        cur1 = []
        while q:
            v = q.popleft()
            if colour[v] == 0:
                cur0.append(v)
            else:
                cur1.append(v)
            for to in g[v]:
                if colour[to] == -1:
                    colour[to] = colour[v] ^ 1
                    q.append(to)
        comps0.append(cur0)
        comps1.append(cur1)
        a.append(len(cur0))
        b.append(len(cur1))

    t = len(a)

    # ----- DP with checkpoints (every 64 components) -----
    STEP = 64
    checkpoints = []          # (index, bitset)
    dp = 1                    # only sum 0 reachable
    checkpoints.append((0, dp))
    for i in range(t):
        dp = (dp << a[i]) | (dp << b[i])
        if (i + 1) % STEP == 0:
            checkpoints.append((i + 1, dp))
    final_dp = dp

    if (final_dp >> k) & 1 == 0:
        print("NO")
        return

    # function to obtain pref bitset before component idx (0‑based)
    # recompute from nearest earlier checkpoint
    def pref_before(idx: int) -> int:
        # find checkpoint with index <= idx
        cp_idx = (idx // STEP) * STEP
        # locate stored bitset
        for j in range(len(checkpoints)-1, -1, -1):
            if checkpoints[j][0] == cp_idx:
                base = checkpoints[j][1]
                break
        else:
            base = 1  # should not happen
        # recompute forward from cp_idx to idx
        for i in range(cp_idx, idx):
            base = (base << a[i]) | (base << b[i])
        return base

    need = k
    answer = []
    # walk backwards
    for i in range(t - 1, -1, -1):
        pref = pref_before(i)          # sums reachable before component i
        take0 = False
        if need >= a[i] and ((pref >> (need - a[i])) & 1):
            take0 = True
        if take0:
            answer.extend(v + 1 for v in comps0[i])
            need -= a[i]
        else:
            answer.extend(v + 1 for v in comps1[i])
            need -= b[i]

    # need must be zero now
    print("YES")
    print(' '.join(map(str, answer[:k])))

if __name__ == "__main__":
    solve()