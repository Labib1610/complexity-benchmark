import sys
sys.setrecursionlimit(10000)

def solve():
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

    colors = [0] * n  # 0 unassigned, 1-3 assigned

    def dfs(idx):
        if idx == n:
            return True
        v = idx
        for col in (1, 2, 3):
            # check conflict with already colored neighbors
            conflict = False
            for nb in adj[v]:
                if colors[nb] == col:
                    conflict = True
                    break
            if conflict:
                continue
            colors[v] = col

            # early pruning: ensure every later uncolored vertex has at least one available color
            ok = True
            for j in range(idx + 1, n):
                if colors[j] == 0:
                    has = False
                    for c in (1, 2, 3):
                        bad = False
                        for nb in adj[j]:
                            if colors[nb] == c:
                                bad = True
                                break
                        if not bad:
                            has = True
                            break
                    if not has:
                        ok = False
                        break
            if ok:
                if dfs(idx + 1):
                    return True
            colors[v] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(map(str, colors)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()