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
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n  # -1 uncoloured, else 0/1/2

    # precompute degrees for tie‑breaking
    degree = [len(adj[i]) for i in range(n)]

    # helper: choose next vertex (DSATUR)
    def choose_vertex():
        best = -1
        best_score = -1
        best_deg = -1
        for v in range(n):
            if color[v] != -1:
                continue
            # number of coloured neighbours
            score = 0
            for nb in adj[v]:
                if color[nb] != -1:
                    score += 1
            if score > best_score or (score == best_score and degree[v] > best_deg):
                best = v
                best_score = score
                best_deg = degree[v]
        return best

    def dfs(coloured_cnt: int) -> bool:
        if coloured_cnt == n:
            return True
        v = choose_vertex()
        # try colours 0,1,2
        forbidden = 0
        for nb in adj[v]:
            c = color[nb]
            if c != -1:
                forbidden |= 1 << c
        for c in range(3):
            if forbidden & (1 << c):
                continue
            color[v] = c
            if dfs(coloured_cnt + 1):
                return True
            color[v] = -1
        return False

    possible = dfs(0)
    out = []
    if not possible:
        out.append("NO")
    else:
        out.append("YES")
        # convert to 1‑based greenhouse numbers
        out.append(' '.join(str(c + 1) for c in color))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()