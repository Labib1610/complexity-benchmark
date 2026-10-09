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
    mask = [0b111] * n           # bits 0,1,2 correspond to colours 1,2,3
    solution = None

    def dfs(idx: int) -> bool:
        nonlocal solution
        if idx == n:
            solution = col.copy()
            return True
        # try colours 1..3
        for c in (1, 2, 3):
            bit = 1 << (c - 1)
            if mask[idx] & bit == 0:
                continue
            # assign
            col[idx] = c
            changes = []          # list of (vertex, old_mask)
            ok = True
            for nb in adj[idx]:
                if col[nb] == 0:          # only affect uncoloured neighbours
                    old = mask[nb]
                    new = old & ~bit
                    if new != old:
                        changes.append((nb, old))
                        mask[nb] = new
                        if new == 0:
                            ok = False
                            break
            if ok and dfs(idx + 1):
                return True
            # undo
            for v, old in changes:
                mask[v] = old
            col[idx] = 0
        return False

    if dfs(0):
        out = ["YES", " ".join(str(x) for x in solution)]
    else:
        out = ["NO"]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()