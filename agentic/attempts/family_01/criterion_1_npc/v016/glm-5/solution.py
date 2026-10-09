import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    full = (1 << n) - 1
    comp = [0] * n
    for i in range(n):
        comp[i] = full ^ (1 << i) ^ adj[i]

    def enumerate_independent_sets(G):
        N = len(G)
        order = sorted(range(N), key=lambda x: bin(G[x]).count("1"))
        rank = [0] * N
        for r, v in enumerate(order):
            rank[v] = r
        Gp = [0] * N
        for v in range(N):
            mask = 0
            for u in range(N):
                if (G[v] >> u) & 1:
                    mask |= 1 << rank[u]
            Gp[rank[v]] = mask
        results = []
        def expand(S, idx):
            results.append(S)
            for j in range(idx, N):
                if (S & Gp[j]) == 0:
                    expand(S | (1 << j), j + 1)
        expand(0, 0)
        return results

    ind_sets = enumerate_independent_sets(comp)
    ind_sets.sort()

    def has_subset(mask):
        lo, hi = 0, len(ind_sets)
        while lo < hi:
            mid = (lo + hi) // 2
            if ind_sets[mid] <= mask:
                lo = mid + 1
            else:
                hi = mid
        for i in range(lo - 1, -1, -1):
            S = ind_sets[i]
            if (mask & S) == S:
                return True
            if bin(S).count("1") < bin(mask).count("1"):
                break
        return False

    for S1 in ind_sets:
        rem1 = full ^ S1
        if not has_subset(rem1):
            continue
        for S2 in ind_sets:
            if (S2 & S1) != 0:
                continue
            if (S2 & rem1) != S2:
                continue
            S3 = rem1 ^ S2
            if (S3 & S1) == 0 and (S3 & S2) == 0:
                assign = [0] * n
                for i in range(n):
                    if (S1 >> i) & 1:
                        assign[i] = 1
                    elif (S2 >> i) & 1:
                        assign[i] = 2
                    else:
                        assign[i] = 3
                print("YES")
                print(" ".join(map(str, assign)))
                return

    print("NO")

solve()