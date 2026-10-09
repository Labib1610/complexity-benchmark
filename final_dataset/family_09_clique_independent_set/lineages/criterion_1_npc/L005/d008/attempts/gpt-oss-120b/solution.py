import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    adj = [0] * n
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        edges.append((u, v))

    p = n // 2          # size of first half
    q = n - p           # size of second half

    # ----- first half enumeration -----
    first_by_size = [[] for _ in range(p + 1)]

    def dfs_first(pos, mask, nei_mask, vertices, nei_to_second):
        if pos == p:
            sz = len(vertices)
            first_by_size[sz].append((mask, nei_to_second, vertices.copy()))
            return
        # skip
        dfs_first(pos + 1, mask, nei_mask, vertices, nei_to_second)
        # take if possible
        if not (nei_mask >> pos) & 1:
            new_mask = mask | (1 << pos)
            new_nei = nei_mask | ((adj[pos] & ((1 << p) - 1)) >> 0)
            # neighbours that lie in second half
            ns = nei_to_second | ((adj[pos] >> p) & ((1 << q) - 1))
            vertices.append(pos)
            dfs_first(pos + 1, new_mask, new_nei, vertices, ns)
            vertices.pop()

    dfs_first(0, 0, 0, [], 0)

    # ----- second half enumeration -----
    second_subsets = []

    # map global index -> local index in second half
    global_to_local = [ -1 ] * n
    for i in range(q):
        global_to_local[p + i] = i

    # pre‑compute adjacency inside second half and to first half
    adj2_local = [0] * q
    adj2_to_first = [0] * q
    for g in range(p, n):
        loc = global_to_local[g]
        # neighbours inside second half
        mask = (adj[g] >> p) & ((1 << q) - 1)
        adj2_local[loc] = mask
        # neighbours in first half
        adj2_to_first[loc] = adj[g] & ((1 << p) - 1)

    def dfs_second(pos, mask, nei_mask, vertices, nei_to_first):
        if pos == q:
            sz = len(vertices)
            second_subsets.append((sz, mask, nei_to_first, vertices.copy()))
            return
        # skip
        dfs_second(pos + 1, mask, nei_mask, vertices, nei_to_first)
        # take if possible
        if not (nei_mask >> pos) & 1:
            new_mask = mask | (1 << pos)
            new_nei = nei_mask | adj2_local[pos]
            nf = nei_to_first | adj2_to_first[pos]
            vertices.append(p + pos)   # store global index
            dfs_second(pos + 1, new_mask, new_nei, vertices, nf)
            vertices.pop()

    dfs_second(0, 0, 0, [], 0)

    # ----- combine -----
    for sz2, mask2, nei_first, verts2 in second_subsets:
        need = k - sz2
        if need < 0 or need > p:
            continue
        for mask1, nei_second, verts1 in first_by_size[need]:
            if (nei_second & mask2) == 0:          # no edge between halves
                # also (nei_first & mask1) == 0 holds automatically because
                # the two masks were built symmetrically, but we can skip test.
                ans = [v + 1 for v in verts1 + verts2]
                print("YES")
                print(*ans)
                return

    print("NO")

if __name__ == "__main__":
    solve()