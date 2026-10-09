import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # order vertices by degree descending for initial heuristic
    order = sorted(range(n), key=lambda x: -adj[x].bit_count())
    # map from position in order to vertex id and reverse
    pos_of = [0] * n
    for i, v in enumerate(order):
        pos_of[v] = i

    # adjacency in terms of positions
    adj_pos = [0] * n
    for i, v in enumerate(order):
        bits = adj[v]
        # translate neighbor bits to positions
        mask = 0
        while bits:
            nb = (bits & -bits).bit_length() - 1
            mask |= 1 << pos_of[nb]
            bits &= bits - 1
        adj_pos[i] = mask

    colors = [0] * n          # color per position (0=uncolored, 1..3)
    possible = [0b111] * n    # 3-bit mask of allowed colors

    # MRV selection
    def select_vertex():
        best = -1
        best_cnt = 4
        for i in range(n):
            if colors[i] == 0:
                cnt = possible[i].bit_count()
                if cnt < best_cnt:
                    best_cnt = cnt
                    best = i
                    if cnt == 1:
                        break
        return best

    sys.setrecursionlimit(10000)
    def dfs(colored_cnt: int) -> bool:
        if colored_cnt == n:
            return True
        v = select_vertex()
        mask = possible[v]
        # try colors in order 1..3
        for c in (1, 2, 3):
            if mask & (1 << (c - 1)):
                # assign
                colors[v] = c
                # backup possible masks of neighbors
                changed = []
                neigh_mask = adj_pos[v]
                nb = neigh_mask
                while nb:
                    u = (nb & -nb).bit_length() - 1
                    nb &= nb - 1
                    if colors[u] == 0:
                        before = possible[u]
                        possible[u] &= ~(1 << (c - 1))
                        if possible[u] != before:
                            changed.append((u, before))
                        if possible[u] == 0:
                            break
                else:
                    if dfs(colored_cnt + 1):
                        return True
                # revert
                for u, before in changed:
                    possible[u] = before
                colors[v] = 0
        return False

    if dfs(0):
        # translate back to original vertex order
        ans = [0] * n
        for i, v in enumerate(order):
            ans[v] = colors[i]
        print("YES")
        print(' '.join(map(str, ans)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()