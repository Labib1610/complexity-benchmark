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
        adj[u].append(v)
        adj[v].append(u)

    # bit masks: colour 1 -> 1<<0, colour 2 -> 1<<1, colour 3 -> 1<<2
    ALL = 0b111

    # initial state
    colour = [0] * n          # 0 = uncoloured, else 1..3
    domain = [ALL] * n

    # helper: count bits in mask (popcount)
    popcnt = lambda x: (x & 1) + ((x >> 1) & 1) + ((x >> 2) & 1)

    # recursive search
    def dfs(col, dom):
        # check if finished
        if all(c != 0 for c in col):
            return col

        # choose vertex with smallest domain (MRV)
        v = -1
        best = 4  # larger than any possible domain size
        for i in range(n):
            if col[i] == 0:
                sz = popcnt(dom[i])
                if sz < best:
                    best = sz
                    v = i
                    if best == 1:
                        break
        if best == 0:          # dead end
            return None

        mask = dom[v]
        # try colours 1,2,3 that are still possible
        for c in (1, 2, 3):
            if mask & (1 << (c - 1)):
                col2 = col[:]          # copy current state
                dom2 = dom[:]          # copy domains
                col2[v] = c
                # forward checking: delete colour c from neighbours
                ok = True
                bit = 1 << (c - 1)
                for nb in adj[v]:
                    if col2[nb] == 0:
                        nd = dom2[nb] & ~bit
                        if nd != dom2[nb]:
                            dom2[nb] = nd
                            if nd == 0:
                                ok = False
                                break
                if not ok:
                    continue
                res = dfs(col2, dom2)
                if res is not None:
                    return res
        return None

    ans = dfs(colour, domain)
    out = []
    if ans is None:
        out.append("NO")
    else:
        out.append("YES")
        out.append(" ".join(str(c) for c in ans))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()