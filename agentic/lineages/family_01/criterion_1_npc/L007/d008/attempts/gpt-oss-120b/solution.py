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

    # bit 0 -> colour 1, bit 1 -> colour 2, bit 2 -> colour 3
    allowed = [0b111] * n
    col = [-1] * n

    # depth‑first search in natural order, trying colours 1,2,3
    def dfs(v: int) -> bool:
        if v == n:
            return True
        mask = allowed[v]
        for c in range(1, 4):          # colours 1..3
            bit = 1 << (c - 1)
            if not (mask & bit):
                continue
            # assign colour c to vertex v
            col[v] = c
            changes = []                # (vertex, old_mask)
            ok = True

            for nb in adj[v]:
                if col[nb] == -1:       # neighbour not coloured yet
                    if allowed[nb] & bit:
                        old = allowed[nb]
                        new = old & ~bit
                        if new == 0:
                            ok = False
                        changes.append((nb, old))
                        allowed[nb] = new
                else:                   # neighbour already coloured
                    if col[nb] == c:
                        ok = False
                if not ok:
                    break

            if ok and dfs(v + 1):
                return True

            # backtrack: restore masks and colour
            for nb, old in reversed(changes):
                allowed[nb] = old
            col[v] = -1
        return False

    possible = dfs(0)

    out = []
    if not possible:
        out.append("NO")
    else:
        out.append("YES")
        out.append(" ".join(str(c) for c in col))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()