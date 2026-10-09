import sys

sys.setrecursionlimit(10000)

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
        mask = 0
        nb = adj[v]
        while nb:
            lsb = nb & -nb
            nb -= lsb
            u = (lsb.bit_length() - 1)
            mask |= 1 << pos_of[u]
        adj_pos[i] = mask

    colors = [-1] * n          # color per position
    allowed = [0b111] * n      # 3 bits per vertex, 1=allowed

    # MRV selection
    def select_vertex():
        best = -1
        best_cnt = 4
        for i in range(n):
            if colors[i] == -1:
                cnt = (allowed[i] & 0b111).bit_count()
                if cnt < best_cnt:
                    best_cnt = cnt
                    best = i
                    if cnt == 1:
                        break
        return best

    def dfs(assigned: int) -> bool:
        if assigned == n:
            return True
        v = select_vertex()
        mask = allowed[v] & 0b111
        # try colors
        while mask:
            cbit = mask & -mask
            mask -= cbit
            c = (cbit.bit_length() - 1)  # 0,1,2
            # assign
            colors[v] = c
            # backup allowed of neighbors
            changed = []
            nb_mask = adj_pos[v]
            while nb_mask:
                lsb = nb_mask & -nb_mask
                nb_mask -= lsb
                u = (lsb.bit_length() - 1)
                if colors[u] == -1:
                    before = allowed[u]
                    allowed[u] &= ~(1 << c)
                    if allowed[u] != before:
                        changed.append((u, before))
                    if allowed[u] == 0:
                        break
            else:
                if dfs(assigned + 1):
                    return True
            # revert
            for u, prev in changed:
                allowed[u] = prev
            colors[v] = -1
        return False

    if dfs(0):
        # translate back to original vertex order
        ans = [0] * n
        for pos, col in enumerate(colors):
            v = order[pos]
            ans[v] = col + 1
        print("YES")
        print(' '.join(map(str, ans)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()