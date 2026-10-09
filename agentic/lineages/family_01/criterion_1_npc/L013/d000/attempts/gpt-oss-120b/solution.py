import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        adj[u].append(v)
        adj[v].append(u)

    # ---------- greedy trial ----------
    order = sorted(range(n), key=lambda x: -len(adj[x]))
    greedy_col = [0] * n
    for v in order:
        used = 0
        for nb in adj[v]:
            c = greedy_col[nb]
            if c:
                used |= 1 << (c - 1)
        # pick the smallest colour not used
        for col in (1, 2, 3):
            if not (used & (1 << (col - 1))):
                greedy_col[v] = col
                break
        else:
            # greedy failed
            greedy_col = None
            break

    if greedy_col is not None:
        print("YES")
        print(" ".join(map(str, greedy_col)))
        return

    # ---------- backtracking ----------
    ALL = 0b111  # three colours possible
    domains = [ALL] * n
    col = [0] * n

    # order vertices by degree for tie‑breaking in MRV
    degree = [len(adj[v]) for v in range(n)]

    from functools import lru_cache

    # popcount for tiny ints
    def bits(x):
        return (x & 1) + ((x >> 1) & 1) + ((x >> 2) & 1)

    def dfs(domains, col, left):
        if left == 0:
            return col
        # MRV: vertex with smallest domain size (>0) and highest degree tie‑break
        best_v = -1
        best_sz = 4  # larger than any possible domain size
        best_deg = -1
        for v in range(n):
            if col[v] == 0:
                sz = bits(domains[v])
                if sz < best_sz or (sz == best_sz and degree[v] > best_deg):
                    best_sz = sz
                    best_v = v
                    best_deg = degree[v]
                if sz == 1:
                    break  # cannot get better
        v = best_v
        mask = domains[v]
        # try colours in order 1,2,3
        for c in (1, 2, 3):
            bit = 1 << (c - 1)
            if not (mask & bit):
                continue
            new_domains = domains[:]
            new_col = col[:]
            new_col[v] = c
            fail = False
            # forward checking
            for nb in adj[v]:
                if new_col[nb] == 0:
                    if new_domains[nb] & bit:
                        new_domains[nb] &= ~bit
                        if new_domains[nb] == 0:
                            fail = True
                            break
            if not fail:
                res = dfs(new_domains, new_col, left - 1)
                if res is not None:
                    return res
        return None

    answer = dfs(domains, col, n)
    if answer is None:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, answer)))

if __name__ == "__main__":
    solve()