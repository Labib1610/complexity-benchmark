import sys

sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0]*n
    edges = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it))-1
        v = int(next(it))-1
        edges[u].append(v)
        edges[v].append(u)
        adj[u] |= 1<<v
        adj[v] |= 1<<u

    colors = [0]*n
    order = sorted(range(n), key=lambda x: -len(edges[x]))

    # Precompute allowed colors per edge: different colors only
    def dfs(pos):
        if pos==n:
            return True
        v = order[pos]
        used = 0
        for nb in edges[v]:
            c = colors[nb]
            if c:
                used |= 1<<c
        for col in (1,2,3):
            if not (used>>col &1):
                colors[v]=col
                if dfs(pos+1):
                    return True
                colors[v]=0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(map(str, colors)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()