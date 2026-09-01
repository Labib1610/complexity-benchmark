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

    # bit helpers
    def bit(col):        # col is 1,2,3
        return 1 << (col - 1)

    # domains: 3 bits, initially all colours possible
    domain = [0b111] * n
    col = [-1] * n      # -1 = uncoloured

    # forward checking after assigning vertex v with colour c
    def propagate(v, c):
        """remove colour c from neighbours' domains,
        return list of (w, old_mask) for restored later,
        and a flag `failed` if some domain becomes empty."""
        changes = []
        failed = False
        mask = bit(c)
        for w in adj[v]:
            if col[w] == -1:
                old = domain[w]
                new = old & ~mask
                if new != old:
                    domain[w] = new
                    changes.append((w, old))
                if new == 0:
                    failed = True
        return changes, failed

    def restore(changes):
        for w, old in changes:
            domain[w] = old

    # depth‑first search, vertices are processed in order 0..n-1
    def dfs(pos: int) -> bool:
        if pos == n:
            return True
        allowed = domain[pos]
        for c in (1, 2, 3):
            if allowed & bit(c):
                col[pos] = c
                changes, bad = propagate(pos, c)
                if not bad and dfs(pos + 1):
                    return True
                restore(changes)
                col[pos] = -1
        return False

    possible = dfs(0)

    out = []
    if possible:
        out.append("YES")
        out.append(" ".join(str(x) for x in col))
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()