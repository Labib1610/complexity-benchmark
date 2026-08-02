import sys
sys.setrecursionlimit(1000000)

# -------------------------------------------------------------

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency bitmasks
    adj = [0] * n
    for _ in range(m):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        adj[a] |= 1 << b
        adj[b] |= 1 << a

    colour = [0] * n                     # 0 = not coloured
    mask_col = [0, 0, 0]                 # colours 1,2,3 -> indices 0,1,2

    # ----- forward checking -------------------------------------------------
    def forward_check(v: int) -> bool:
        """After giving v a colour, are all neighbours still colourable?"""
        neigh = adj[v]
        while neigh:
            u = (neigh & -neigh).bit_length() - 1   # lowest set bit
            neigh &= neigh - 1                      # remove the bit
            if colour[u] == 0:                      # u is still uncoloured
                used = 0
                if mask_col[0] & adj[u]:
                    used |= 1
                if mask_col[1] & adj[u]:
                    used |= 2
                if mask_col[2] & adj[u]:
                    used |= 4
                if used == 7:                       # all three colours used
                    return False
        return True

    # ----- backtracking ------------------------------------------------------
    def dfs(idx: int) -> bool:
        if idx == n:          # all vertices coloured
            return True
        v = idx
        for c in range(3):    # try colours 1,2,3
            # skip if neighbour already has the same colour
            if (mask_col[c] & adj[v]) != 0:
                continue
            colour[v] = c + 1
            mask_col[c] |= 1 << v
            if forward_check(v) and dfs(idx + 1):
                return True
            # backtrack
            colour[v] = 0
            mask_col[c] &= ~(1 << v)
        return False

    # -----------------------------------------------------------------------
    if dfs(0):
        print(' '.join(str(colour[i]) for i in range(n)))
    else:
        print(-1)


# -------------------------------------------------------------
if __name__ == "__main__":
    solve()