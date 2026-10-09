import sys
from itertools import permutations
from collections import deque

sys.setrecursionlimit(10000)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return

    n, m = data[0], data[1]
    adj = [[] for _ in range(n)]
    eu = [0] * m
    ev = [0] * m
    epu = [0] * m
    epv = [0] * m

    idx = 2
    valid = True
    for eid in range(m):
        u = data[idx] - 1
        v = data[idx + 1] - 1
        idx += 2

        if not (0 <= u < n and 0 <= v < n) or u == v:
            valid = False
            continue

        eu[eid] = u
        ev[eid] = v
        epu[eid] = len(adj[u])
        epv[eid] = len(adj[v])
        adj[u].append(eid)
        adj[v].append(eid)

    if not valid or any(len(adj[v]) != 3 for v in range(n)):
        print("NO")
        return

    # A cubic graph containing a bridge cannot be 3-edge-colored.
    tin = [-1] * n
    low = [0] * n
    timer = 0
    has_bridge = False
    roots = []

    def dfs(v, parent_edge):
        nonlocal timer, has_bridge
        tin[v] = low[v] = timer
        timer += 1

        for eid in adj[v]:
            if eid == parent_edge:
                continue
            to = ev[eid] if eu[eid] == v else eu[eid]
            if tin[to] == -1:
                dfs(to, eid)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    has_bridge = True
            else:
                low[v] = min(low[v], tin[to])

    for v in range(n):
        if tin[v] == -1:
            roots.append(v)
            dfs(v, -1)

    if has_bridge:
        print("NO")
        return

    perms = list(permutations(range(3)))
    support = [[0] * 3 for _ in range(3)]

    for pi, perm in enumerate(perms):
        bit = 1 << pi
        for pos in range(3):
            support[pos][perm[pos]] |= bit

    possible = [[0] * 3 for _ in range(64)]
    filters = [[0] * 8 for _ in range(3)]

    for mask in range(64):
        for pos in range(3):
            colors = 0
            for color in range(3):
                if mask & support[pos][color]:
                    colors |= 1 << color
            possible[mask][pos] = colors

    for pos in range(3):
        for colors in range(8):
            mask = 0
            for color in range(3):
                if colors & (1 << color):
                    mask |= support[pos][color]
            filters[pos][colors] = mask

    domains = [63] * n

    # Color names may be permuted independently in every connected component.
    for root in roots:
        domains[root] = 1  # permutation (0, 1, 2)

    def propagate(initial_edges, trail):
        q = deque(initial_edges)

        while q:
            eid = q.popleft()
            u = eu[eid]
            v = ev[eid]
            pu = epu[eid]
            pv = epv[eid]

            du = domains[u]
            dv = domains[v]
            allowed = possible[du][pu] & possible[dv][pv]

            if allowed == 0:
                return False

            ndu = du & filters[pu][allowed]
            ndv = dv & filters[pv][allowed]

            if ndu == 0 or ndv == 0:
                return False

            if ndu != du:
                trail.append((u, du))
                domains[u] = ndu
                for ne in adj[u]:
                    if ne != eid:
                        q.append(ne)

            if ndv != dv:
                trail.append((v, dv))
                domains[v] = ndv
                for ne in adj[v]:
                    if ne != eid:
                        q.append(ne)

        return True

    initial_trail = []
    if not propagate(range(m), initial_trail):
        print("NO")
        return

    def rollback(trail, mark):
        while len(trail) > mark:
            v, old_domain = trail.pop()
            domains[v] = old_domain

    trail = []

    def solve():
        chosen = -1
        best_size = 7
        best_score = -1

        for v in range(n):
            size = domains[v].bit_count()
            if 1 < size < best_size:
                chosen = v
                best_size = size
                best_score = sum(6 - domains[
                    ev[eid] if eu[eid] == v else eu[eid]
                ].bit_count() for eid in adj[v])
            elif size == best_size and size > 1:
                score = sum(6 - domains[
                    ev[eid] if eu[eid] == v else eu[eid]
                ].bit_count() for eid in adj[v])
                if score > best_score:
                    chosen = v
                    best_score = score

        if chosen == -1:
            return True

        candidates = []
        mask = domains[chosen]

        while mask:
            bit = mask & -mask
            mask -= bit
            pi = bit.bit_length() - 1
            score = 1

            for pos, eid in enumerate(adj[chosen]):
                if eu[eid] == chosen:
                    other = ev[eid]
                    other_pos = epv[eid]
                else:
                    other = eu[eid]
                    other_pos = epu[eid]

                color = perms[pi][pos]
                count = (domains[other] & support[other_pos][color]).bit_count()
                score *= count

            candidates.append((score, bit))

        candidates.sort(reverse=True)

        for _, bit in candidates:
            mark = len(trail)
            old = domains[chosen]
            trail.append((chosen, old))
            domains[chosen] = bit

            if propagate(adj[chosen], trail) and solve():
                return True

            rollback(trail, mark)

        return False

    if not solve():
        print("NO")
        return

    answer = [0] * m
    for eid in range(m):
        u = eu[eid]
        pi = domains[u].bit_length() - 1
        answer[eid] = perms[pi][epu[eid]] + 1

    print("YES")
    print(*answer)

if __name__ == "__main__":
    main()