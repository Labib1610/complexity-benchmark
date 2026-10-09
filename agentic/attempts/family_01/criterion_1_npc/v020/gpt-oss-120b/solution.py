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

    # order vertices by degree descending for heuristic
    order = sorted(range(n), key=lambda x: -len(adj[x]))
    pos_in_order = [0]*n
    for i, v in enumerate(order):
        pos_in_order[v] = i

    colors = [-1]*n  # -1 uncolored, 0..2 colors

    # adjacency check using order positions for faster conflict test
    def can_color(v, c):
        for nb in adj[v]:
            if colors[nb] == c:
                return False
        return True

    # select next uncolored vertex: the one with highest degree (first in order)
    def select_vertex():
        for v in order:
            if colors[v] == -1:
                return v
        return -1

    def dfs(colored_cnt: int) -> bool:
        if colored_cnt == n:
            return True
        v = select_vertex()
        for c in range(3):
            if can_color(v, c):
                colors[v] = c
                if dfs(colored_cnt + 1):
                    return True
                colors[v] = -1
        return False

    possible = dfs(0)

    if not possible:
        print("NO")
    else:
        print("YES")
        # output 1-indexed drive numbers
        print(' '.join(str(c+1) for c in colors))

if __name__ == "__main__":
    solve()