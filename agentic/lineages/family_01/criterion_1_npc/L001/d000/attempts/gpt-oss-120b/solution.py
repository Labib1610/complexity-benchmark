import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n  # bitmask of neighbors
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # order vertices by degree descending
    order = sorted(range(n), key=lambda x: bin(adj[x]).count("1"), reverse=True)
    colors = [0] * n  # 0 = uncolored, else 1..3

    sys.setrecursionlimit(10000)

    def dfs(pos: int) -> bool:
        if pos == n:
            return True
        v = order[pos]
        # try each color
        neighbor_mask = adj[v]
        for c in (1, 2, 3):
            ok = True
            # check all already colored neighbors
            nb = neighbor_mask
            while nb:
                u = (nb & -nb).bit_length() - 1
                nb &= nb - 1
                if colors[u] == c:
                    ok = False
                    break
            if ok:
                colors[v] = c
                if dfs(pos + 1):
                    return True
                colors[v] = 0
        return False

    if dfs(0):
        out = ["YES", " ".join(str(colors[i]) for i in range(n))]
    else:
        out = ["NO"]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()