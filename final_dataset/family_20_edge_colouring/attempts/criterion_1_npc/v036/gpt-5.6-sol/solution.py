import sys

sys.setrecursionlimit(10000)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return

    n, m = data[0], data[1]
    adj = [[] for _ in range(n)]
    edges = []

    p = 2
    for i in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        edges.append((u, v))
        adj[u].append(i)
        adj[v].append(i)

    if m * 2 != 3 * n or any(len(adj[v]) != 3 for v in range(n)):
        print("NO")
        return

    # A cubic graph with a bridge cannot have a 3-edge-coloring.
    tin = [-1] * n
    low = [0] * n
    timer = 0
    has_bridge = False

    def bridge_dfs(v, parent_edge):
        nonlocal timer, has_bridge
        tin[v] = low[v] = timer
        timer += 1

        for eid in adj[v]:
            if eid == parent_edge:
                continue
            a, b = edges[eid]
            to = b if a == v else a

            if tin[to] == -1:
                bridge_dfs(to, eid)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    has_bridge = True
            else:
                low[v] = min(low[v], tin[to])

    for s in range(n):
        if tin[s] == -1:
            bridge_dfs(s, -1)

    if has_bridge:
        print("NO")
        return

    color = [-1] * m
    mask = [0] * n
    count = [0] * n
    log = []
    assigned = 0
    state_hash = 0

    MASK64 = (1 << 64) - 1

    def splitmix64(x):
        x = (x + 0x9E3779B97F4A7C15) & MASK64
        x = ((x ^ (x >> 30)) * 0xBF58476D1CE4E5B9) & MASK64
        x = ((x ^ (x >> 27)) * 0x94D049BB133111EB) & MASK64
        return (x ^ (x >> 31)) & MASK64

    zobrist = [[0] * 3 for _ in range(m)]
    seed = 0x123456789ABCDEF0
    for eid in range(m):
        for c in range(3):
            seed = splitmix64(seed + eid * 3 + c + 1)
            zobrist[eid][c] = seed

    def rollback(mark):
        nonlocal assigned, state_hash
        while len(log) > mark:
            eid = log.pop()
            c = color[eid]
            bit = 1 << c
            u, v = edges[eid]
            mask[u] ^= bit
            mask[v] ^= bit
            count[u] -= 1
            count[v] -= 1
            color[eid] = -1
            assigned -= 1
            state_hash ^= zobrist[eid][c]

    def assign_with_propagation(first_eid, first_color):
        nonlocal assigned, state_hash

        pending = [(first_eid, first_color)]

        while pending:
            eid, c = pending.pop()

            if color[eid] != -1:
                if color[eid] != c:
                    return False
                continue

            u, v = edges[eid]
            bit = 1 << c

            if (mask[u] & bit) or (mask[v] & bit):
                return False

            color[eid] = c
            mask[u] |= bit
            mask[v] |= bit
            count[u] += 1
            count[v] += 1
            assigned += 1
            state_hash ^= zobrist[eid][c]
            log.append(eid)

            for x in (u, v):
                if count[x] == 2:
                    missing_color = ((~mask[x]) & 7).bit_length() - 1
                    missing_edge = -1
                    for ne in adj[x]:
                        if color[ne] == -1:
                            if missing_edge != -1:
                                return False
                            missing_edge = ne
                    if missing_edge == -1:
                        return False
                    pending.append((missing_edge, missing_color))
                elif count[x] == 3 and mask[x] != 7:
                    return False

        return True

    def parity_components_possible():
        for c in range(3):
            bit = 1 << c
            visited = [False] * n

            for start in range(n):
                if visited[start] or (mask[start] & bit):
                    continue

                size = 0
                stack = [start]
                visited[start] = True

                while stack:
                    v = stack.pop()
                    size += 1
                    for eid in adj[v]:
                        if color[eid] != -1:
                            continue
                        a, b = edges[eid]
                        to = b if a == v else a
                        if mask[to] & bit:
                            continue
                        if not visited[to]:
                            visited[to] = True
                            stack.append(to)

                if size & 1:
                    return False

        return True

    failed = set()
    FAILED_LIMIT = 500000

    def dfs(depth):
        if assigned == m:
            return True

        h = state_hash
        if h in failed:
            return False

        if depth and depth % 48 == 0:
            if not parity_components_possible():
                if len(failed) < FAILED_LIMIT:
                    failed.add(h)
                return False

        best_v = -1
        best_score = -1

        for v in range(n):
            if count[v] != 1:
                continue

            score = 0
            for eid in adj[v]:
                if color[eid] == -1:
                    a, b = edges[eid]
                    to = b if a == v else a
                    score += count[to] * 4
                    if count[to] == 2:
                        score += 8

            if score > best_score:
                best_score = score
                best_v = v

        if best_v == -1:
            # Start an untouched connected component. Color symmetry lets us
            # fix the three incident colors arbitrarily.
            seed_v = -1
            for v in range(n):
                if count[v] == 0:
                    seed_v = v
                    break

            if seed_v == -1:
                if len(failed) < FAILED_LIMIT:
                    failed.add(h)
                return False

            mark = len(log)
            e0, e1, _ = adj[seed_v]

            if assign_with_propagation(e0, 0):
                if assign_with_propagation(e1, 1):
                    if dfs(depth + 1):
                        return True

            rollback(mark)
            if len(failed) < FAILED_LIMIT:
                failed.add(h)
            return False

        uncolored = [eid for eid in adj[best_v] if color[eid] == -1]
        e1, e2 = uncolored[0], uncolored[1]
        remaining = [c for c in range(3) if not (mask[best_v] & (1 << c))]
        c1, c2 = remaining[0], remaining[1]

        options = [(e1, c1, e2, c2), (e1, c2, e2, c1)]

        # Prefer the orientation that is immediately compatible at both
        # opposite endpoints.
        def option_score(option):
            a_e, a_c, b_e, b_c = option
            score = 0
            for eid, c in ((a_e, a_c), (b_e, b_c)):
                u, v = edges[eid]
                to = v if u == best_v else u
                if mask[to] & (1 << c):
                    score -= 1000
                else:
                    score += count[to]
            return -score

        options.sort(key=option_score)

        for first_edge, first_color, _, _ in options:
            mark = len(log)
            if assign_with_propagation(first_edge, first_color):
                if dfs(depth + 1):
                    return True
            rollback(mark)

        if len(failed) < FAILED_LIMIT:
            failed.add(h)
        return False

    if dfs(0):
        print("YES")
        print(" ".join(str(c + 1) for c in color))
    else:
        print("NO")

if __name__ == "__main__":
    main()