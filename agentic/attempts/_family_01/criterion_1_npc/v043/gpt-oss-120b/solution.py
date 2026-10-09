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

    # domain masks: bit 0->color1, bit1->color2, bit2->color3
    ALL = 0b111
    domains = [ALL] * n
    colors = [0] * n  # 0 means unassigned, else 1..3

    # order vertices by degree for heuristic
    order = sorted(range(n), key=lambda x: -adj[x].bit_count())
    # map from position in order to vertex
    pos_of = [0] * n
    for i, v in enumerate(order):
        pos_of[v] = i

    # helper to pick next vertex: unassigned with smallest domain size
    def select_vertex():
        best = -1
        best_sz = 4
        for v in range(n):
            if colors[v] == 0:
                sz = domains[v].bit_count()
                if sz < best_sz:
                    best_sz = sz
                    best = v
                    if sz == 1:
                        break
        return best

    # stack for backtracking changes: list of (vertex, old_mask)
    changes = []

    def assign(v, col):
        """assign color col (1..3) to vertex v, propagate constraints.
           return False if conflict arises."""
        colors[v] = col
        # domain becomes only this color
        old = domains[v]
        changes.append((v, old))
        domains[v] = 1 << (col - 1)

        # remove this color from neighbors
        mask = 1 << (col - 1)
        nb = adj[v]
        while nb:
            u = (nb & -nb).bit_length() - 1
            nb &= nb - 1
            if colors[u] == 0:
                if domains[u] & mask:
                    old_u = domains[u]
                    changes.append((u, old_u))
                    domains[u] = old_u & ~mask
                    if domains[u] == 0:
                        return False
        return True

    def undo(to_len):
        while len(changes) > to_len:
            v, old = changes.pop()
            domains[v] = old
            if colors[v] != 0 and old != (1 << (colors[v] - 1)):
                # if we are reverting an assignment, reset color
                colors[v] = 0

    def dfs(assigned_cnt):
        if assigned_cnt == n:
            return True
        v = select_vertex()
        if v == -1:
            return False
        cur_mask = domains[v]
        # try each possible color
        for col in (1, 2, 3):
            if cur_mask & (1 << (col - 1)):
                checkpoint = len(changes)
                if assign(v, col):
                    if dfs(assigned_cnt + 1):
                        return True
                undo(checkpoint)
        return False

    possible = dfs(0)
    if not possible:
        print("NO")
    else:
        print("YES")
        print(' '.join(str(c) for c in colors))

if __name__ == "__main__":
    solve()