import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n
    comps = []          # list of (list0, list1)
    from collections import deque
    for start in range(n):
        if color[start] != -1:
            continue
        q = deque([start])
        color[start] = 0
        list0 = []
        list1 = []
        while q:
            v = q.popleft()
            if color[v] == 0:
                list0.append(v)
            else:
                list1.append(v)
            for to in adj[v]:
                if color[to] == -1:
                    color[to] = color[v] ^ 1
                    q.append(to)
        comps.append((list0, list1))

    # compute maximal independent set size and differences
    diffs = []          # d_i
    larger = []         # list of vertices of larger side
    smaller = []        # list of vertices of smaller side
    max_sum = 0
    for c0, c1 in comps:
        if len(c0) >= len(c1):
            larger.append(c0)
            smaller.append(c1)
            d = len(c0) - len(c1)
        else:
            larger.append(c1)
            smaller.append(c0)
            d = len(c1) - len(c0)
        diffs.append(d)
        max_sum += len(larger[-1])

    if k > max_sum:
        print("NO")
        return

    R = max_sum - k          # amount to reduce
    if R == 0:
        # take all larger sides
        ans = []
        for lst in larger:
            ans.extend(lst)
        print("YES")
        print(' '.join(str(v + 1) for v in ans[:k]))
        return

    # subset sum DP with reconstruction info
    dp = 1                   # bit 0 set
    from_idx = [-1] * (R + 1)   # which component created this sum
    for idx, d in enumerate(diffs):
        if d == 0:
            continue
        shifted = dp << d
        new = shifted & ~dp
        # iterate over set bits of new
        while new:
            low = new & -new
            s = low.bit_length() - 1
            if s <= R:
                from_idx[s] = idx
            new -= low
        dp |= shifted
        # early stop if R already reachable
        if (dp >> R) & 1:
            break

    if (dp >> R) & 1 == 0:
        print("NO")
        return

    # reconstruct which components to switch to smaller side
    take_small = [False] * len(comps)
    cur = R
    while cur:
        idx = from_idx[cur]
        take_small[idx] = True
        cur -= diffs[idx]

    # build answer
    ans = []
    for i, (big, small) in enumerate(zip(larger, smaller)):
        if take_small[i]:
            ans.extend(small)
        else:
            ans.extend(big)
    ans = ans[:k]   # just in case (should be exactly k)
    print("YES")
    print(' '.join(str(v + 1) for v in ans))

if __name__ == "__main__":
    solve()