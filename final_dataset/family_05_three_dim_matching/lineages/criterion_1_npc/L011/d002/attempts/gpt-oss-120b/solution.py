import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    triples = []
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        triples.append((x, y, z))

    # adjacency for quick edge existence check in feasibility test
    adj_xy = [[0] * k for _ in range(k)]  # bitmask of z's for each (x,y)
    for x, y, z in triples:
        adj_xy[x][y] |= 1 << z

    # list of triples per x for ordering
    triples_by_x = [[] for _ in range(k)]
    for idx, (x, y, z) in enumerate(triples):
        triples_by_x[x].append((y, z, idx))

    # Hopcroft–Karp for bipartite matching between unused X and Y
    from collections import deque

    def max_matching(mask_x: int, mask_y: int, mask_z: int) -> int:
        # build adjacency list for current masks
        left = [i for i in range(k) if (mask_x >> i) & 1]
        right_id = {j: idx for idx, j in enumerate([j for j in range(k) if (mask_y >> j) & 1])}
        nL = len(left)
        nR = len(right_id)
        if nL == 0 or nR == 0:
            return 0
        G = [[] for _ in range(nL)]
        for li, x in enumerate(left):
            for y in range(k):
                if (mask_y >> y) & 1:
                    if adj_xy[x][y] & mask_z:
                        G[li].append(right_id[y])

        pairU = [-1] * nL
        pairV = [-1] * nR
        dist = [0] * nL

        INF = 10 ** 9

        def bfs() -> bool:
            q = deque()
            for u in range(nL):
                if pairU[u] == -1:
                    dist[u] = 0
                    q.append(u)
                else:
                    dist[u] = INF
            reachable = False
            while q:
                u = q.popleft()
                for v in G[u]:
                    if pairV[v] == -1:
                        reachable = True
                    elif dist[pairV[v]] == INF:
                        dist[pairV[v]] = dist[u] + 1
                        q.append(pairV[v])
            return reachable

        def dfs(u: int) -> bool:
            for v in G[u]:
                if pairV[v] == -1 or (dist[pairV[v]] == dist[u] + 1 and dfs(pairV[v])):
                    pairU[u] = v
                    pairV[v] = u
                    return True
            dist[u] = INF
            return False

        matching = 0
        while bfs():
            for u in range(nL):
                if pairU[u] == -1 and dfs(u):
                    matching += 1
        return matching

    full_mask = (1 << k) - 1
    used_x = used_y = used_z = 0
    answer = [None] * k
    found = False

    # order xs by fewest available triples to improve pruning
    xs_order = sorted(range(k), key=lambda x: len(triples_by_x[x]))

    def dfs(depth: int) -> None:
        nonlocal used_x, used_y, used_z, found
        if found:
            return
        if depth == k:
            # all selected
            print("YES")
            for tr in answer:
                x, y, z = tr
                print(x + 1, y + 1, z + 1)
            found = True
            return

        # simple bound: need remaining = k - depth
        rem = k - depth
        # quick feasibility via bipartite matching bound
        if max_matching(~used_x & full_mask, ~used_y & full_mask, ~used_z & full_mask) < rem:
            return

        # choose next x with smallest branching
        for x in xs_order:
            if (used_x >> x) & 1:
                continue
            # iterate candidate triples for this x
            for y, z, idx in triples_by_x[x]:
                if (used_y >> y) & 1 or (used_z >> z) & 1:
                    continue
                # select
                used_x |= 1 << x
                used_y |= 1 << y
                used_z |= 1 << z
                answer[depth] = (x, y, z)
                dfs(depth + 1)
                if found:
                    return
                # backtrack
                used_x ^= 1 << x
                used_y ^= 1 << y
                used_z ^= 1 << z
            # if no candidate works for this x, prune
            return

    dfs(0)
    if not found:
        print("NO")

if __name__ == "__main__":
    solve()