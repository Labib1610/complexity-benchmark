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

    # domain masks: bit 0 -> colour 1, bit1 -> colour2, bit2 -> colour3
    ALL = 0b111
    domain = [ALL] * n
    colour = [0] * n          # 0 = uncoloured, otherwise 1..3

    # depth‑first search in lexicographic order
    def dfs(idx: int) -> bool:
        if idx == n:
            return True

        # try colours 1,2,3
        for c in (1, 2, 3):
            bit = 1 << (c - 1)
            if not (domain[idx] & bit):
                continue          # colour not allowed by current domain

            # assign colour c to vertex idx
            colour[idx] = c
            mods = []            # (vertex, old_mask) to revert later
            conflict = False

            for nb in adj[idx]:
                if colour[nb] == 0:          # only uncoloured neighbours
                    if domain[nb] & bit:
                        old = domain[nb]
                        new = old & ~bit
                        if new == 0:
                            conflict = True
                        domain[nb] = new
                        mods.append((nb, old))

            if not conflict:
                if dfs(idx + 1):
                    return True

            # revert changes
            for v, old in reversed(mods):
                domain[v] = old
            colour[idx] = 0

        return False

    possible = dfs(0)

    out = []
    if possible:
        out.append("YES")
        out.append(" ".join(str(colour[i]) for i in range(n)))
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()