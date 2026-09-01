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

    # colour of each vertex, 0 = uncoloured, otherwise 1..3
    color = [0] * n
    # allowed colours mask, bits 0,1,2 correspond to colours 1,2,3
    allowed = [0b111] * n

    # depth‑first search, vertices are processed in order 0..n-1
    def dfs(pos: int) -> bool:
        if pos == n:
            return True
        v = pos
        mask = allowed[v]
        # try colours 1,2,3 (bits 0,1,2) in increasing order
        for c in range(3):
            bit = 1 << c
            if mask & bit == 0:
                continue
            # forward checking: remove colour c from neighbours
            changes = []          # list of (neighbour, previous_allowed)
            ok = True
            for nb in adj[v]:
                if color[nb] == 0:
                    prev = allowed[nb]
                    new = prev & ~bit
                    if new != prev:
                        allowed[nb] = new
                        changes.append((nb, prev))
                        if new == 0:
                            ok = False
                            break
                else:
                    if color[nb] == c + 1:
                        ok = False
                        break
            if ok:
                color[v] = c + 1
                if dfs(pos + 1):
                    return True
                color[v] = 0
            # restore neighbours' allowed masks
            for nb, prev in changes:
                allowed[nb] = prev
        return False

    possible = dfs(0)

    out = []
    if not possible:
        out.append("NO")
    else:
        out.append("YES")
        out.append(" ".join(str(col) for col in color))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()