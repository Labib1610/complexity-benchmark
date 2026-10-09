import sys

sys.setrecursionlimit(10000)

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
    color = [-1] * n

    def dfs(pos: int) -> bool:
        if pos == n:
            return True
        v = order[pos]
        used = {color[nb] for nb in adj[v] if color[nb] != -1}
        for c in range(3):
            if c not in used:
                color[v] = c
                if dfs(pos + 1):
                    return True
                color[v] = -1
        return False

    if dfs(0):
        print("YES")
        # map 0,1,2 to 1,2,3
        print(' '.join(str(c + 1) for c in color))
    else:
        print("NO")

if __name__ == "__main__":
    solve()