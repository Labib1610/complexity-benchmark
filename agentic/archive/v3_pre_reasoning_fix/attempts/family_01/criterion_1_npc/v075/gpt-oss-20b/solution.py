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

    col = [0] * n          # 0 unassigned, 1..3 assigned
    possible = [0b111] * n  # bitmask of possible colors for each vertex

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        v = idx
        # try colors 1..3 in order
        for color in (1, 2, 3):
            bit = 1 << (color - 1)
            if (possible[v] & bit) == 0:
                continue
            # check conflict with already colored neighbors
            conflict = False
            for u in adj[v]:
                if col[u] == color:
                    conflict = True
                    break
            if conflict:
                continue

            # assign
            col[v] = color
            changes = []
            ok = True
            for u in adj[v]:
                if col[u] == 0:
                    old = possible[u]
                    new = old & ~bit
                    if new != old:
                        changes.append((u, old))
                        possible[u] = new
                        if new == 0:
                            ok = False
                            break
            if ok:
                if dfs(idx + 1):
                    return True
            # revert
            for u, old in reversed(changes):
                possible[u] = old
            col[v] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(col[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()