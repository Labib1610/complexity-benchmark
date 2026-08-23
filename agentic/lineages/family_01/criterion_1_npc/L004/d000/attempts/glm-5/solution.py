import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    full = (1 << (n + 1)) - 1
    # independent sets as bitmask over vertices 1..n
    indep_sets = []
    for mask in range(1 << n):
        ok = True
        for i in range(n):
            if mask & (1 << i):
                if adj[i + 1] & mask:
                    ok = False
                    break
        if ok:
            indep_sets.append(mask)

    indep_sets.sort(key=lambda x: bin(x).count('1'), reverse=True)
    indep_set_list = indep_sets

    # Precompute for each independent set the list of vertices (1-based)
    indep_vertices = []
    for mask in indep_set_list:
        verts = []
        for i in range(n):
            if mask & (1 << i):
                verts.append(i + 1)
        indep_vertices.append(verts)

    # Try all pairs of independent sets for bus1 and bus2
    found = False
    result = None
    for idx1, mask1 in enumerate(indep_set_list):
        if found:
            break
        verts1 = indep_vertices[idx1]
        avail1 = full & ~mask1
        for idx2 in range(idx1, len(indep_set_list)):
            mask2 = indep_set_list[idx2]
            if mask2 & mask1:
                continue
            if mask2 & ~avail1:
                continue
            mask3 = full & ~(mask1 | mask2)
            # check mask3 independent
            ok3 = True
            mm = mask3
            while mm:
                low = mm & (-mm)
                i = low.bit_length() - 1
                if adj[i + 1] & mask3:
                    ok3 = False
                    break
                mm ^= low
            if not ok3:
                continue
            # build assignment
            assign = [0] * (n + 1)
            for v in verts1:
                assign[v] = 1
            for v in indep_vertices[idx2]:
                assign[v] = 2
            mm = mask3
            while mm:
                low = mm & (-mm)
                i = low.bit_length() - 1
                assign[i + 1] = 3
                mm ^= low
            found = True
            result = assign[1:]
            break

    if not found:
        print("NO")
        return

    # Now we have a valid assignment. We need lexicographically smallest.
    # Greedy assignment: assign each vertex 1..n the smallest bus that doesn't
    # conflict with already assigned incompatible neighbors.
    assign = [0] * (n + 1)
    for v in range(1, n + 1):
        for b in (1, 2, 3):
            ok = True
            for u in range(1, n + 1):
                if adj[v] & (1 << u):
                    if assign[u] == b:
                        ok = False
                        break
            if ok:
                assign[v] = b
                break
        else:
            print("NO")
            return

    print("YES")
    print(' '.join(str(assign[i]) for i in range(1, n + 1)))

solve()