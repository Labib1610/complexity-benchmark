import sys
sys.setrecursionlimit(100000)

def solve() -> None:
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        adj[u].append(v)
        adj[v].append(u)

    domains = [7] * n          # bitmask: 1->1, 2->2, 3->4
    assign = [0] * n

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        for color in (1, 2, 3):
            mask = 1 << (color - 1)
            if domains[idx] & mask:
                assign[idx] = color
                changes = []
                ok = True
                for nb in adj[idx]:
                    if assign[nb] == 0:
                        prev = domains[nb]
                        if prev & mask:
                            new = prev & ~mask
                            if new == 0:
                                ok = False
                                break
                            domains[nb] = new
                            changes.append((nb, prev))
                if ok and dfs(idx + 1):
                    return True
                # revert changes
                for nb, prev in changes:
                    domains[nb] = prev
                assign[idx] = 0
        return False

    if dfs(0):
        out = ["YES"]
        out.append(' '.join(map(str, assign)))
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()