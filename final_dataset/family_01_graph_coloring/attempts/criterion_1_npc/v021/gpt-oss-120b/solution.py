import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [set() for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].add(v)
        adj[v].add(u)

    order = sorted(range(n), key=lambda x: -len(adj[x]))
    color = [0] * n
    sys.setrecursionlimit(10000)
    found = False

    def dfs(pos: int):
        nonlocal found
        if found:
            return
        if pos == n:
            found = True
            return
        v = order[pos]
        used = {color[nb] for nb in adj[v] if color[nb] != 0}
        for c in (1, 2, 3):
            if c not in used:
                color[v] = c
                dfs(pos + 1)
                if found:
                    return
                color[v] = 0

    dfs(0)

    if not found:
        print("NO")
    else:
        print("YES")
        # output in original order 1..n
        print(' '.join(str(color[i]) for i in range(n)))

if __name__ == "__main__":
    solve()