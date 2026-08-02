import sys
sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
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

    color = [0] * n  # 0 unassigned, 1..3 assigned
    found = False

    def dfs(idx: int) -> bool:
        nonlocal found
        if idx == n:
            found = True
            return True
        v = idx
        # try colors 1..3 in order
        for c in (1, 2, 3):
            # check if any neighbor already colored c
            neigh_mask = adj[v]
            bad = False
            # iterate over set bits in neigh_mask
            msk = neigh_mask
            while msk:
                lsb = msk & -msk
                u = (lsb.bit_length() - 1)
                if color[u] == c:
                    bad = True
                    break
                msk -= lsb
            if bad:
                continue
            color[v] = c
            if dfs(idx + 1):
                return True
            color[v] = 0
        return False

    if dfs(0):
        out = ["YES", " ".join(str(x) for x in color)]
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()