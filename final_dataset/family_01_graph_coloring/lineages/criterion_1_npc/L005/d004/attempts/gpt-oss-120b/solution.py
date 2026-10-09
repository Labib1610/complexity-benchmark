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
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))

    # precompute allowed pairs for colors 1..3
    allowed = [[True]*4 for _ in range(4)]  # 1-indexed
    for a in (1, 2, 3):
        for b in (1, 2, 3):
            val = (a*a + a*b + b*b) % 3
            allowed[a][b] = (val != 0)

    order = sorted(range(n), key=lambda x: -len(adj[x]))
    color = [0]*n
    found = False

    def backtrack(idx: int) -> bool:
        nonlocal found
        if idx == n:
            return True
        v = order[idx]
        for c in (1, 2, 3):
            ok = True
            for nb in adj[v]:
                if color[nb] and not allowed[c][color[nb]]:
                    ok = False
                    break
            if not ok:
                continue
            color[v] = c
            if backtrack(idx + 1):
                return True
            color[v] = 0
        return False

    if backtrack(0):
        sys.stdout.write("YES\n")
        sys.stdout.write(' '.join(map(str, color)) + "\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == "__main__":
    solve()