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

    colors = [0] * n
    order = sorted(range(n), key=lambda x: -len(adj[x]))  # static ordering by degree

    # For MRV we recompute each step
    def select_vertex():
        best = -1
        best_deg = -1
        for v in range(n):
            if colors[v] == 0:
                # count used colors among neighbors
                used = {colors[nb] for nb in adj[v] if colors[nb] != 0}
                deg = len(used)
                if deg > best_deg:
                    best_deg = deg
                    best = v
        return best

    def dfs(colored_cnt: int) -> bool:
        if colored_cnt == n:
            return True
        v = select_vertex()
        # try colors 1..3
        for c in (1, 2, 3):
            conflict = False
            for nb in adj[v]:
                if colors[nb] == c:
                    conflict = True
                    break
            if not conflict:
                colors[v] = c
                if dfs(colored_cnt + 1):
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