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

    color = [-1] * n               # -1 = uncoloured, else 0,1,2
    avail = [0b111] * n            # three bits set
    changes = []                   # stack of (vertex, old_avail)

    # order vertices by degree for tie‑breaking
    degree = [len(adj[i]) for i in range(n)]

    def choose_vertex() -> int:
        # pick uncoloured vertex with smallest popcount(avail)
        best = -1
        best_cnt = 4  # more than max 3
        best_deg = -1
        for v in range(n):
            if color[v] != -1:
                continue
            cnt = (avail[v] & 0b111).bit_count()
            if cnt < best_cnt or (cnt == best_cnt and degree[v] > best_deg):
                best = v
                best_cnt = cnt
                best_deg = degree[v]
        return best

    def dfs(coloured: int) -> bool:
        if coloured == n:
            return True
        v = choose_vertex()
        mask = avail[v]
        # try each colour present in mask
        for c in range(3):
            if not (mask >> c) & 1:
                continue
            # assign colour c to v
            color[v] = c
            saved = []          # local list of (u, old_avail)
            conflict = False
            for u in adj[v]:
                if color[u] == -1 and (avail[u] >> c) & 1:
                    old = avail[u]
                    new = old & ~(1 << c)
                    saved.append((u, old))
                    avail[u] = new
                    if new == 0:
                        conflict = True
                        break
            if not conflict:
                if dfs(coloured + 1):
                    return True
            # undo changes
            for u, old in reversed(saved):
                avail[u] = old
            color[v] = -1
        return False

    possible = dfs(0)
    out = []
    if not possible:
        out.append("NO")
    else:
        out.append("YES")
        out.append(' '.join(str(c + 1) for c in color))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()