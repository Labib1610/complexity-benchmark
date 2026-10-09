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
    pos_in_order = [0] * n
    for i, v in enumerate(order):
        pos_in_order[v] = i

    # domains: 3-bit mask, bit0->color1, bit1->color2, bit2->color3
    full_mask = 0b111
    domain = [full_mask] * n
    color = [0] * n  # 0 means unassigned, else 1..3

    # For fast selection of vertex with smallest domain >0 among unassigned
    unassigned_set = (1 << n) - 1

    # stack to record domain reductions for backtracking
    changes_stack = []

    def select_vertex():
        # choose unassigned vertex with smallest domain size (>0)
        best = -1
        best_cnt = 4
        mask = unassigned_set
        while mask:
            v = (mask & -mask).bit_length() - 1
            mask &= mask - 1
            cnt = domain[v].bit_count()
            if cnt < best_cnt:
                best_cnt = cnt
                best = v
                if cnt == 1:
                    break
        return best

    def assign(v, col):
        nonlocal unassigned_set
        # set color
        color[v] = col
        unassigned_set &= ~(1 << v)
        # record changes for backtrack
        changes = []
        # remove this vertex from neighbors' domains
        neigh = adj[v]
        mask = neigh & unassigned_set
        while mask:
            u = (mask & -mask).bit_length() - 1
            mask &= mask - 1
            if domain[u] & (1 << (col - 1)):
                changes.append((u, domain[u]))
                domain[u] &= ~(1 << (col - 1))
                if domain[u] == 0:
                    # dead end, will be detected later
                    pass
        changes_stack.append(changes)

    def undo(v):
        nonlocal unassigned_set
        # restore domains
        changes = changes_stack.pop()
        for u, prev in reversed(changes):
            domain[u] = prev
        # unassign v
        color[v] = 0
        unassigned_set |= (1 << v)

    def dfs():
        if unassigned_set == 0:
            return True
        v = select_vertex()
        if v == -1:
            return False
        cur_dom = domain[v]
        # try each possible color
        for bit in (0, 1, 2):
            if cur_dom & (1 << bit):
                assign(v, bit + 1)
                # early failure check: any neighbor now has empty domain?
                fail = False
                mask = adj[v] & unassigned_set
                while mask:
                    u = (mask & -mask).bit_length() - 1
                    mask &= mask - 1
                    if domain[u] == 0:
                        fail = True
                        break
                if not fail and dfs():
                    return True
                undo(v)
        return False

    possible = dfs()
    if not possible:
        print("NO")
    else:
        print("YES")
        # output in original order 1..n
        print(' '.join(str(color[i]) for i in range(n)))

if __name__ == "__main__":
    solve()