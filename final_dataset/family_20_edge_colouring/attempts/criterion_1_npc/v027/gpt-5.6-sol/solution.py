import sys
from collections import deque

sys.setrecursionlimit(1000000)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return

    n, m = data[0], data[1]
    adj = [[] for _ in range(n)]
    eu = [0] * m
    ev = [0] * m

    p = 2
    valid = (m * 2 == 3 * n)
    for i in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        eu[i] = u
        ev[i] = v
        if u == v:
            valid = False
        adj[u].append(i)
        adj[v].append(i)

    if not valid or any(len(adj[v]) != 3 for v in range(n)):
        print("NO")
        return

    # A bridge in a cubic graph makes a 3-edge-coloring impossible.
    tin = [-1] * n
    low = [0] * n
    timer = 0
    has_bridge = False

    def bridge_dfs(v, parent_edge):
        nonlocal timer, has_bridge
        tin[v] = low[v] = timer
        timer += 1
        for e in adj[v]:
            if e == parent_edge:
                continue
            to = ev[e] if eu[e] == v else eu[e]
            if tin[to] == -1:
                bridge_dfs(to, e)
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

    # Bipartite cubic graphs can always be decomposed into three perfect matchings.
    side = [-1] * n
    bipartite = True
    for s in range(n):
        if side[s] != -1:
            continue
        side[s] = 0
        q = deque([s])
        while q and bipartite:
            v = q.popleft()
            for e in adj[v]:
                to = ev[e] if eu[e] == v else eu[e]
                if side[to] == -1:
                    side[to] = side[v] ^ 1
                    q.append(to)
                elif side[to] == side[v]:
                    bipartite = False
                    break

    if bipartite:
        left = [v for v in range(n) if side[v] == 0]
        active = [True] * m
        answer = [0] * m

        def perfect_matching():
            pair_l = [-1] * n
            pair_r = [-1] * n
            dist = [-1] * n

            def bfs():
                q = deque()
                found = False
                for u in left:
                    if pair_l[u] == -1:
                        dist[u] = 0
                        q.append(u)
                    else:
                        dist[u] = -1
                while q:
                    u = q.popleft()
                    for e in adj[u]:
                        if not active[e]:
                            continue
                        v = ev[e] if eu[e] == u else eu[e]
                        pe = pair_r[v]
                        if pe == -1:
                            found = True
                        else:
                            nu = eu[pe] if ev[pe] == v else ev[pe]
                            if dist[nu] == -1:
                                dist[nu] = dist[u] + 1
                                q.append(nu)
                return found

            def dfs(u):
                for e in adj[u]:
                    if not active[e]:
                        continue
                    v = ev[e] if eu[e] == u else eu[e]
                    pe = pair_r[v]
                    if pe == -1:
                        pair_l[u] = e
                        pair_r[v] = e
                        return True
                    nu = eu[pe] if ev[pe] == v else ev[pe]
                    if dist[nu] == dist[u] + 1 and dfs(nu):
                        pair_l[u] = e
                        pair_r[v] = e
                        return True
                dist[u] = -1
                return False

            matched = 0
            while bfs():
                for u in left:
                    if pair_l[u] == -1 and dfs(u):
                        matched += 1

            if matched != len(left):
                return None
            return [pair_l[u] for u in left]

        for c in range(1, 4):
            matching = perfect_matching()
            if matching is None:
                print("NO")
                return
            for e in matching:
                answer[e] = c
                active[e] = False

        print("YES")
        print(*answer)
        return

    # Exact propagation/backtracking for general cubic graphs.
    color = [0] * m
    mask = [0] * n
    count = [0] * n
    frontier = set()
    trail = []
    assigned = 0

    def rollback(marker):
        nonlocal assigned
        while len(trail) > marker:
            e = trail.pop()
            c = color[e]
            bit = 1 << (c - 1)
            u, v = eu[e], ev[e]

            for x in (u, v):
                old = count[x]
                mask[x] ^= bit
                count[x] -= 1
                if old == 1:
                    frontier.discard(x)
                elif old == 2:
                    frontier.add(x)

            color[e] = 0
            assigned -= 1

    def assign(start_e, start_c):
        nonlocal assigned
        pending = [(start_e, start_c)]

        while pending:
            e, c = pending.pop()
            if color[e]:
                if color[e] != c:
                    return False
                continue

            bit = 1 << (c - 1)
            u, v = eu[e], ev[e]

            if (mask[u] & bit) or (mask[v] & bit):
                return False

            color[e] = c
            trail.append(e)
            assigned += 1

            for x in (u, v):
                old = count[x]
                mask[x] |= bit
                count[x] += 1

                if old == 0:
                    frontier.add(x)
                elif old == 1:
                    frontier.discard(x)

                if count[x] == 2:
                    missing_edge = -1
                    for ne in adj[x]:
                        if color[ne] == 0:
                            missing_edge = ne
                            break
                    if missing_edge == -1:
                        return False
                    missing_mask = 7 ^ mask[x]
                    if missing_mask == 1:
                        missing_color = 1
                    elif missing_mask == 2:
                        missing_color = 2
                    elif missing_mask == 4:
                        missing_color = 3
                    else:
                        return False
                    pending.append((missing_edge, missing_color))

        return True

    def search():
        if assigned == m:
            return True

        chosen_v = -1
        chosen_e = -1

        # Prefer an edge joining two frontier vertices, since it closes a path
        # and usually produces immediate propagation or contradiction.
        for v in frontier:
            if count[v] != 1:
                continue
            for e in adj[v]:
                if color[e] != 0:
                    continue
                to = ev[e] if eu[e] == v else eu[e]
                if count[to] == 1:
                    chosen_v = v
                    chosen_e = e
                    break
            if chosen_v != -1:
                break

        if chosen_v == -1:
            for v in frontier:
                if count[v] == 1:
                    chosen_v = v
                    for e in adj[v]:
                        if color[e] == 0:
                            chosen_e = e
                            break
                    break

        if chosen_v == -1:
            # Start a new connected component. Its colors may be fixed
            # arbitrarily because global color permutations preserve validity.
            root = -1
            for v in range(n):
                if count[v] == 0:
                    root = v
                    break
            if root == -1:
                return assigned == m

            marker = len(trail)
            e0, e1, _ = adj[root]
            if assign(e0, 1) and assign(e1, 2) and search():
                return True
            rollback(marker)
            return False

        available = 7 ^ mask[chosen_v]
        choices = []
        if available & 1:
            choices.append(1)
        if available & 2:
            choices.append(2)
        if available & 4:
            choices.append(3)

        for c in choices:
            marker = len(trail)
            if assign(chosen_e, c) and search():
                return True
            rollback(marker)

        return False

    if search():
        print("YES")
        print(*color)
    else:
        print("NO")


if __name__ == "__main__":
    main()