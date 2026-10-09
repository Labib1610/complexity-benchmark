import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n          # adjacency as bitmask of neighbors (n <= 40 fits in int)
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # order vertices by degree descending for heuristic
    order = sorted(range(n), key=lambda x: bin(adj[x]).count("1"), reverse=True)

    color = [-1] * n               # -1 uncolored, else 0,1,2
    possible = [0b111] * n         # 3-bit mask of allowed colors

    # map from position in order to vertex
    pos2v = order
    # map vertex to its position in order (for quick lookup)
    v2pos = [0] * n
    for i, v in enumerate(pos2v):
        v2pos[v] = i

    # precompute neighbor list for fast iteration
    neigh = [ [j for j in range(n) if (adj[i] >> j) & 1] for i in range(n) ]

    # stack for backtracking changes: each entry (vertex, old_mask)
    changes = []

    def assign(v: int, col: int) -> bool:
        """assign color col to vertex v, propagate constraints.
        return False if contradiction."""
        color[v] = col
        # record change for v itself (its mask becomes single color)
        changes.append((v, possible[v]))
        possible[v] = 1 << col

        # propagate to neighbors
        for u in neigh[v]:
            if color[u] == -1:
                if possible[u] & (1 << col):
                    old = possible[u]
                    new = old & ~(1 << col)
                    if new == 0:
                        # contradiction, revert later
                        changes.append((u, old))
                        possible[u] = new
                        return False
                    if new != old:
                        changes.append((u, old))
                        possible[u] = new
        return True

    def undo(to_len: int) -> None:
        """revert changes stack to given length."""
        while len(changes) > to_len:
            v, old = changes.pop()
            possible[v] = old
            if old != 0b111 and color[v] != -1 and (old & (1 << color[v])) == 0:
                # vertex was assigned and its mask no longer contains that color
                color[v] = -1

    def dfs(idx: int) -> bool:
        """try to color vertices from order[idx:]"""
        if idx == n:
            return True
        v = pos2v[idx]
        if color[v] != -1:
            return dfs(idx + 1)

        # try colors allowed by possible mask
        mask = possible[v]
        for col in range(3):
            if mask & (1 << col):
                snap = len(changes)
                if assign(v, col):
                    if dfs(idx + 1):
                        return True
                undo(snap)
        return False

    if dfs(0):
        print("YES")
        # output colors as 1..3
        print(' '.join(str(c + 1) for c in color))
    else:
        print("NO")

if __name__ == "__main__":
    solve()