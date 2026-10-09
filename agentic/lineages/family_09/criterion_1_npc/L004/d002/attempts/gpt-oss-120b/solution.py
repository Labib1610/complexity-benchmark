import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    edges = [0] * n          # adjacency as bitmask (full graph)
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges[u] |= 1 << v
        edges[v] |= 1 << u

    L = n // 2
    R = n - L
    left_adj = [0] * L
    right_adj = [0] * R
    cross_left = [0] * L          # edges from left vertex to right side
    cross_right = [0] * R         # edges from right vertex to left side

    for i in range(L):
        mask = edges[i]
        left_adj[i] = mask & ((1 << L) - 1)
        cross_left[i] = (mask >> L) & ((1 << R) - 1)

    for i in range(R):
        v = L + i
        mask = edges[v]
        right_adj[i] = (mask >> L) & ((1 << R) - 1)
        cross_right[i] = mask & ((1 << L) - 1)

    # ---------- independent subsets of left ----------
    size_left = [-1] * (1 << L)
    size_left[0] = 0
    for mask in range(1, 1 << L):
        b = mask & -mask
        v = (b.bit_length() - 1)
        prev = mask ^ b
        if size_left[prev] != -1 and (left_adj[v] & prev) == 0:
            size_left[mask] = size_left[prev] + 1

    # ---------- independent subsets of right ----------
    size_right = [-1] * (1 << R)
    size_right[0] = 0
    for mask in range(1, 1 << R):
        b = mask & -mask
        v = (b.bit_length() - 1)
        prev = mask ^ b
        if size_right[prev] != -1 and (right_adj[v] & prev) == 0:
            size_right[mask] = size_right[prev] + 1

    # bestSize / bestMask for right side (SOS DP)
    bestSize = [-1] * (1 << R)
    bestMask = [0] * (1 << R)
    for mask in range(1 << R):
        if size_right[mask] != -1:
            bestSize[mask] = size_right[mask]
            bestMask[mask] = mask

    for i in range(R):
        bit = 1 << i
        for mask in range(1 << R):
            if mask & bit:
                sub = mask ^ bit
                if bestSize[sub] > bestSize[mask]:
                    bestSize[mask] = bestSize[sub]
                    bestMask[mask] = bestMask[sub]

    all_right = (1 << R) - 1

    # ---------- try all left independent masks ----------
    for Lmask in range(1 << L):
        szL = size_left[Lmask]
        if szL == -1:
            continue
        need = k - szL
        if need < 0:
            continue
        # compute forbidden right vertices caused by chosen left vertices
        forbid = 0
        tmp = Lmask
        while tmp:
            b = tmp & -tmp
            v = (b.bit_length() - 1)
            forbid |= cross_left[v]
            tmp ^= b
        allowed = all_right ^ forbid
        if bestSize[allowed] < need:
            continue
        # we have a solution
        Rmask = bestMask[allowed]
        # possibly shrink Rmask to exactly 'need' vertices
        chosen_right = []
        cnt = need
        tmp = Rmask
        while cnt and tmp:
            b = tmp & -tmp
            v = (b.bit_length() - 1)
            chosen_right.append(v)
            cnt -= 1
            tmp ^= b
        # build answer list (1‑based)
        ans = []
        tmp = Lmask
        while tmp:
            b = tmp & -tmp
            v = (b.bit_length() - 1)
            ans.append(v + 1)          # left vertices are 0‑based
            tmp ^= b
        for v in chosen_right:
            ans.append(L + v + 1)       # shift by L for right side
        # output
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, ans)) + "\n")
        return

    sys.stdout.write("NO\n")

if __name__ == "__main__":
    solve()