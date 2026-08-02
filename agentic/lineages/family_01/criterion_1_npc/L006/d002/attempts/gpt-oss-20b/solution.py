import sys

def solve() -> None:
    sys.setrecursionlimit(10000)
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    assigned = [0] * (n + 1)          # 0 means unassigned
    avail = [0b111] * (n + 1)         # available colors mask for each vertex

    def dfs(i: int) -> bool:
        if i > n:
            return True
        mask = avail[i]
        for c in (1, 2, 3):
            if mask & (1 << (c - 1)):
                assigned[i] = c
                changes = []
                fail = False
                for u in adj[i]:
                    if assigned[u] == 0:
                        old = avail[u]
                        new = old & ~(1 << (c - 1))
                        if new != old:
                            changes.append((u, old))
                            avail[u] = new
                            if new == 0:
                                fail = True
                                break
                if not fail and dfs(i + 1):
                    return True
                # backtrack
                for u, old in reversed(changes):
                    avail[u] = old
                assigned[i] = 0
        return False

    if dfs(1):
        print("YES")
        print(' '.join(str(assigned[i]) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()