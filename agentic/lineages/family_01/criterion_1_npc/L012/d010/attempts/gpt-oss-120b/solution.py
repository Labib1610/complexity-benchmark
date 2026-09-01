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

    col = [0] * n                     # 0 = uncoloured, else 1..3
    mask = [0b111] * n               # bits 0,1,2 correspond to colours 1,2,3

    # recursion
    def dfs(pos: int) -> bool:
        if pos == n:
            return True
        v = pos
        allowed = mask[v]
        for c in (1, 2, 3):
            bit = 1 << (c - 1)
            if not (allowed & bit):
                continue
            # apply colour c to v
            col[v] = c
            changes = []               # list of (vertex, old_mask)
            ok = True
            for nb in adj[v]:
                if col[nb]:
                    if col[nb] == c:   # already coloured same -> conflict
                        ok = False
                        break
                else:
                    if mask[nb] & bit:
                        old = mask[nb]
                        new = old & ~bit
                        if new == 0:
                            ok = False
                            break
                        mask[nb] = new
                        changes.append((nb, old))
            if ok and dfs(pos + 1):
                return True
            # undo
            for nb, old in reversed(changes):
                mask[nb] = old
            col[v] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(col[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()