import sys

def solve() -> None:
    sys.setrecursionlimit(1000000)
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
        if v not in adj[u]:
            adj[u].append(v)
            adj[v].append(u)

    color = [0] * n          # 0 = unassigned, 1/2/3 = colors
    avail = [0b111] * n      # bitmask of available colors for each vertex

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        v = idx
        for c in (1, 2, 3):
            bit = 1 << (c - 1)
            if (avail[v] & bit) == 0:
                continue
            color[v] = c
            changes = []
            ok = True
            for u in adj[v]:
                if color[u] == 0:
                    if avail[u] & bit:
                        old = avail[u]
                        avail[u] &= ~bit
                        changes.append((u, old))
                        if avail[u] == 0:
                            ok = False
                            break
            if ok and dfs(idx + 1):
                return True
            # revert changes
            for u, old in changes:
                avail[u] = old
            color[v] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(color[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()