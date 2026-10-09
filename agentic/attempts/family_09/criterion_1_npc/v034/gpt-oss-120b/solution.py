import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    # adjacency in original graph
    adj_orig = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj_orig[u] |= 1 << v
        adj_orig[v] |= 1 << u

    # adjacency in complement graph (including self? no)
    full = (1 << n) - 1
    adj = [0] * n
    for v in range(n):
        # neighbours in complement = all vertices except self and original neighbours
        adj[v] = full ^ (adj_orig[v] | (1 << v))

    answer_mask = 0
    found = False

    # ----- greedy coloring for a set of candidates (bitmask) -----
    def color_sort(cand_mask: int):
        """return order list (vertices) and colour numbers (same length)"""
        order = []
        colors = []
        # copy of mask to modify
        remaining = cand_mask
        colour = 0
        while remaining:
            colour += 1
            # vertices that can receive this colour: those not adjacent to already coloured in this round
            # we build a mask of vertices that are not adjacent to any vertex already taken in this colour
            # start with all remaining
            avail = remaining
            while avail:
                v = (avail & -avail).bit_length() - 1
                avail &= avail - 1
                order.append(v)
                colors.append(colour)
                # remove v and its neighbours from remaining for this colour
                remaining &= ~((1 << v) | adj[v])
        return order, colors

    # ----- recursive expansion -----
    def expand(R_mask: int, P_mask: int):
        nonlocal answer_mask, found
        if found:
            return
        size_R = R_mask.bit_count()
        if size_R == k:
            answer_mask = R_mask
            found = True
            return
        # prune: not enough candidates left
        if size_R + P_mask.bit_count() < k:
            return

        order, colors = color_sort(P_mask)
        # process in reverse order (non‑increasing colour)
        for i in range(len(order) - 1, -1, -1):
            if found:
                return
            v = order[i]
            # bound with colour
            if size_R + colors[i] < k:
                return
            # new candidate set = vertices adjacent to v within current P
            new_P = P_mask & adj[v]
            expand(R_mask | (1 << v), new_P)
            # remove v from P
            P_mask &= ~(1 << v)

    all_vertices = (1 << n) - 1
    expand(0, all_vertices)

    if not found:
        print("NO")
    else:
        # extract vertices from mask, convert to 1‑based ids
        res = []
        mask = answer_mask
        while mask:
            v = (mask & -mask).bit_length() - 1
            res.append(str(v + 1))
            mask &= mask - 1
        print("YES")
        print(" ".join(res))

if __name__ == "__main__":
    solve()