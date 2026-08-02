import sys
sys.setrecursionlimit(10000)

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

    # Precompute neighbors with lower index to speed conflict checks
    lower_adj = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for v in adj[i]:
            if v < i:
                lower_adj[i].append(v)

    colors = [0] * (n + 1)  # 1-indexed
    found = False

    def dfs(pos: int) -> bool:
        nonlocal found
        if pos > n:
            found = True
            return True
        for c in (1, 2, 3):
            conflict = False
            for v in lower_adj[pos]:
                if colors[v] == c:
                    conflict = True
                    break
            if not conflict:
                colors[pos] = c
                if dfs(pos + 1):
                    return True
                colors[pos] = 0
        return False

    if dfs(1):
        print("YES")
        print(' '.join(str(colors[i]) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()