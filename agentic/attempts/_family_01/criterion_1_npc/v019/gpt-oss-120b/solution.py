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

    # order vertices by degree descending
    order = sorted(range(n), key=lambda x: -adj[x].bit_count())
    pos_in_order = [0] * n
    for i, v in enumerate(order):
        pos_in_order[v] = i

    colors = [-1] * n
    # possible colors bitmask for each vertex (bits 0,1,2)
    poss = [(1 << 3) - 1] * n

    # adjacency in order indices for quick check
    adj_order = [0] * n
    for i, v in enumerate(order):
        mask = 0
        nb = adj[v]
        while nb:
            lsb = nb & -nb
            u = (lsb.bit_length() - 1)
            mask |= 1 << pos_in_order[u]
            nb ^= lsb
        adj_order[i] = mask

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        # select vertex with smallest domain among remaining
        # simple: use idx order
        v = order[idx]
        # try each possible color
        avail = poss[v]
        while avail:
            c = (avail & -avail).bit_length() - 1  # color index 0..2
            avail ^= 1 << c
            # assign
            colors[v] = c
            # store changes to revert
            changed = []
            # update neighbors' possible colors
            nb_mask = adj[v]
            while nb_mask:
                lsb = nb_mask & -nb_mask
                u = (lsb.bit_length() - 1)
                nb_mask ^= lsb
                if colors[u] == -1:
                    if poss[u] & (1 << c):
                        poss[u] &= ~(1 << c)
                        changed.append(u)
                        if poss[u] == 0:
                            break
            else:
                # continue recursion
                if dfs(idx + 1):
                    return True
            # revert
            for u in changed:
                poss[u] |= 1 << c
            colors[v] = -1
        return False

    # start recursion
    if dfs(0):
        print("YES")
        # convert to 1..3
        print(' '.join(str(colors[i] + 1) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()