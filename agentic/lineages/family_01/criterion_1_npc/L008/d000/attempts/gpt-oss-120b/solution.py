import sys

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
    forb = [0] * n              # bitmask of forbidden colours
    stack = []                  # (vertex, old_forb)

    sys.setrecursionlimit(10000)

    def dfs(v: int) -> bool:
        if v == n:
            return True
        allowed = 0b111 ^ forb[v]
        for c in (1, 2, 3):
            if not (allowed & (1 << (c - 1))):
                continue
            col[v] = c
            sz = len(stack)
            conflict = False
            mask = 1 << (c - 1)
            for u in adj[v]:
                if col[u] == 0:
                    old = forb[u]
                    new = old | mask
                    if new != old:
                        stack.append((u, old))
                        forb[u] = new
                        if new == 0b111:
                            conflict = True
                            break
            if not conflict:
                if dfs(v + 1):
                    return True
            # undo changes of this assignment
            while len(stack) > sz:
                u, old = stack.pop()
                forb[u] = old
            col[v] = 0
        return False

    if dfs(0):
        out = ['YES', ' '.join(str(c) for c in col)]
    else:
        out = ['NO']
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()