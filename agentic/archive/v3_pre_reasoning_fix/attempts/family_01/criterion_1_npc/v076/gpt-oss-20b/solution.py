import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    neighbors = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        neighbors[u].append(v)
        neighbors[v].append(u)

    color = [-1] * n          # -1 uncolored, otherwise 1..3
    allowed = [0b111] * n     # 3-bit mask of allowed colors for uncolored nodes
    colored_mask = [0, 0, 0, 0]  # indexed by color 1..3

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        node = idx
        for c in (1, 2, 3):
            if adj[node] & colored_mask[c]:
                continue  # conflict with already colored neighbor
            # apply color
            color[node] = c
            colored_mask[c] |= 1 << node
            changes = []  # list of (neighbor, old_allowed)
            ok = True
            for nb in neighbors[node]:
                if color[nb] == -1:
                    old = allowed[nb]
                    new = old & ~(1 << (c - 1))
                    if new != old:
                        changes.append((nb, old))
                        allowed[nb] = new
                        if new == 0:
                            ok = False
                            break
            if ok and dfs(idx + 1):
                return True
            # revert
            for nb, old in changes:
                allowed[nb] = old
            colored_mask[c] &= ~(1 << node)
            color[node] = -1
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(color[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()