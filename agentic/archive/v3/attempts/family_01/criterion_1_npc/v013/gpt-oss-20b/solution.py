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

    color = [-1] * n          # -1 unassigned, else 0..2
    forbidden = [0] * n      # 3-bit mask of forbidden colors

    sys.setrecursionlimit(10000)

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        v = idx
        for col in range(3):
            # conflict with already colored neighbors
            conflict = False
            for u in adj[v]:
                if color[u] == col:
                    conflict = True
                    break
            if conflict:
                continue

            color[v] = col
            changes = []
            ok = True
            for u in adj[v]:
                if color[u] == -1:
                    old = forbidden[u]
                    new = old | (1 << col)
                    if new != old:
                        forbidden[u] = new
                        changes.append((u, old))
                        if new == 7:  # all colors forbidden
                            ok = False
                            break
            if ok and dfs(idx + 1):
                return True
            # revert changes
            for u, old in changes:
                forbidden[u] = old
            color[v] = -1
        return False

    if dfs(0):
        out = ['YES', ' '.join(str(c + 1) for c in color)]
    else:
        out = ['NO']
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()