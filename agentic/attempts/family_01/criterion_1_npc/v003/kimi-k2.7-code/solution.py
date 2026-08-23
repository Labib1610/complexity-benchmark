import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # domain masks: bits 0,1,2 correspond to colors 1,2,3
    bits = [0] * 8
    for i in range(8):
        bits[i] = (i & 1) + ((i >> 1) & 1) + ((i >> 2) & 1)
    single = [False] * 8
    single[1] = single[2] = single[4] = True

    sys.setrecursionlimit(10000)

    def can_complete(assign):
        dom = [7] * n
        stack = []
        for v in range(n):
            c = assign[v]
            if c:
                dom[v] = 1 << (c - 1)
                stack.append(v)

        # unit propagation from all fixed/forced vertices
        while stack:
            v = stack.pop()
            bit = dom[v]
            mask = adj[v]
            while mask:
                lsb = mask & -mask
                w = lsb.bit_length() - 1
                if dom[w] & bit:
                    dom[w] &= ~bit
                    if dom[w] == 0:
                        return False
                    if single[dom[w]]:
                        stack.append(w)
                mask ^= lsb

        # split remaining graph into connected components
        uncolored = 0
        for v in range(n):
            if not single[dom[v]]:
                uncolored |= 1 << v

        while uncolored:
            lsb = uncolored & -uncolored
            v = lsb.bit_length() - 1
            comp_mask = 0
            frontier = 1 << v
            while frontier:
                lsb2 = frontier & -frontier
                x = lsb2.bit_length() - 1
                comp_mask |= lsb2
                frontier ^= lsb2
                neigh = adj[x] & uncolored & ~comp_mask
                frontier |= neigh
            uncolored &= ~comp_mask

            verts = []
            mm = comp_mask
            while mm:
                lsb2 = mm & -mm
                verts.append(lsb2.bit_length() - 1)
                mm ^= lsb2

            if not search_comp(dom, verts, comp_mask):
                return False
        return True

    def search_comp(dom, verts, comp_mask):
        minv = -1
        mind = 4
        for v in verts:
            d = dom[v]
            if not single[d]:
                cnt = bits[d]
                if cnt < mind:
                    mind = cnt
                    minv = v
                    if cnt == 2:
                        break
        if minv == -1:
            return True

        d = dom[minv]
        for cbit in (1, 2, 4):
            if d & cbit:
                ndom = dom[:]
                ndom[minv] = cbit
                if propagate(ndom, minv, comp_mask):
                    if search_comp(ndom, verts, comp_mask):
                        return True
        return False

    def propagate(dom, v, comp_mask):
        stack = [v]
        while stack:
            v = stack.pop()
            bit = dom[v]
            mask = adj[v] & comp_mask
            while mask:
                lsb = mask & -mask
                w = lsb.bit_length() - 1
                if dom[w] & bit:
                    dom[w] &= ~bit
                    if dom[w] == 0:
                        return False
                    if single[dom[w]]:
                        stack.append(w)
                mask ^= lsb
        return True

    assign = [0] * n
    for i in range(n):
        used = 0
        mask = adj[i]
        while mask:
            lsb = mask & -mask
            w = lsb.bit_length() - 1
            c = assign[w]
            if c:
                used |= 1 << (c - 1)
            mask ^= lsb

        chosen = 0
        for c in (1, 2, 3):
            if used & (1 << (c - 1)):
                continue
            assign[i] = c
            if can_complete(assign):
                chosen = c
                break
            assign[i] = 0

        if chosen == 0:
            sys.stdout.write("NO")
            return

    out = ["YES", " ".join(str(c) for c in assign)]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()