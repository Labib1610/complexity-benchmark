import sys
sys.setrecursionlimit(10000)

def solve():
    import sys
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = []
    adj = [[] for _ in range(n)]
    for idx in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v))
        adj[u].append((v, idx))
        adj[v].append((u, idx))

    # degree check
    if any(len(adj[v]) != 3 for v in range(n)):
        print("NO")
        return

    # edge colors: 0 uncolored, 1..3 colors
    col = [0] * m

    # For each vertex, keep set of used colors
    used = [set() for _ in range(n)]

    # order edges by adjacency (heuristic)
    order = sorted(range(m), key=lambda i: len(adj[edges[i][0]]) + len(adj[edges[i][1]]), reverse=True)

    def dfs(pos):
        if pos == m:
            return True
        e = order[pos]
        if col[e]:
            return dfs(pos + 1)
        u, v = edges[e]
        for c in (1, 2, 3):
            if c not in used[u] and c not in used[v]:
                col[e] = c
                used[u].add(c)
                used[v].add(c)
                if dfs(pos + 1):
                    return True
                used[u].remove(c)
                used[v].remove(c)
                col[e] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(map(str, col)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()