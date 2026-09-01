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

    col = [0] * n               # 0 = uncoloured, else 1..3
    mask = [0b111] * n          # three bits, 1<<0 -> colour 1, etc.

    # depth‑first search
    def dfs(pos: int) -> bool:
        if pos == n:
            return True
        v = pos
        allowed = mask[v]
        for c in (1, 2, 3):
            bit = 1 << (c - 1)
            if not (allowed & bit):
                continue
            # remember neighbours' masks to restore later
            changed = []
            ok = True
            for nb in adj[v]:
                if col[nb] == 0 and (mask[nb] & bit):
                    old = mask[nb]
                    new = old & ~bit
                    if new == 0:
                        ok = False
                        break
                    mask[nb] = new
                    changed.append((nb, old))
            if ok:
                col[v] = c
                if dfs(pos + 1):
                    return True
                col[v] = 0
            # restore
            for nb, old in changed:
                mask[nb] = old
        return False

    possible = dfs(0)
    out = []
    if not possible:
        out.append("NO")
    else:
        out.append("YES")
        out.append(" ".join(str(col[i]) for i in range(n)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()