import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    col = [0] * (n + 1)          # 0 = uncoloured, else 1..3
    mask = [0b111] * (n + 1)     # possible colours bitmask
    stack = []                   # (vertex, old_mask)

    sys.setrecursionlimit(10000)

    def dfs(v: int) -> bool:
        if v == n + 1:
            return True
        # vertex already coloured? (should not happen)
        if col[v]:
            return dfs(v + 1)

        allowed = mask[v]
        for c in (1, 2, 3):
            bit = 1 << (c - 1)
            if not (allowed & bit):
                continue
            # remember stack size to undo later
            snap = len(stack)
            col[v] = c
            ok = True
            # propagate to neighbours
            for nb in adj[v]:
                if col[nb]:
                    if col[nb] == c:
                        ok = False
                        break
                    continue
                if mask[nb] & bit:
                    old = mask[nb]
                    stack.append((nb, old))
                    mask[nb] = old & ~bit
                    if mask[nb] == 0:
                        ok = False
                        break
            if ok and dfs(v + 1):
                return True
            # undo changes
            while len(stack) > snap:
                u, old = stack.pop()
                mask[u] = old
            col[v] = 0
        return False

    if dfs(1):
        out = ['YES', ' '.join(str(col[i]) for i in range(1, n + 1))]
    else:
        out = ['NO']
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()