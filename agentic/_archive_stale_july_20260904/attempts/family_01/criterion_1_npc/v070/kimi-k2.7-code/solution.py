import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    popcount = [0, 1, 1, 2, 1, 2, 2, 3]
    allowed_mask_to_color = [0] * 8
    for c in (1, 2, 3):
        allowed_mask_to_color[1 << (c - 1)] = c

    def propagate(a):
        q = []
        for v in range(1, n + 1):
            if a[v] == 0:
                return False
            if popcount[a[v]] == 1:
                q.append(v)
        while q:
            v = q.pop()
            cm = a[v]
            for u in adj[v]:
                if a[u] & cm:
                    new = a[u] & ~cm
                    if new == 0:
                        return False
                    a[u] = new
                    if popcount[new] == 1:
                        q.append(u)
        return True

    def cycle_colorable(cycle, a):
        k = len(cycle)
        v0 = cycle[0]
        for c0 in (1, 2, 3):
            b0 = 1 << (c0 - 1)
            if not (a[v0] & b0):
                continue
            dp = {c0}
            broken = False
            for idx in range(1, k):
                vi = cycle[idx]
                new_dp = set()
                for ci in (1, 2, 3):
                    bi = 1 << (ci - 1)
                    if a[vi] & bi:
                        if any(cp != ci for cp in dp):
                            new_dp.add(ci)
                dp = new_dp
                if not dp:
                    broken = True
                    break
            if not broken and any(c != c0 for c in dp):
                return True
        return False

    def is_colorable(a):
        if not propagate(a):
            return False
        active = [v for v in range(1, n + 1) if popcount[a[v]] > 1]
        if not active:
            return True

        deg = [0] * (n + 1)
        maxd = 0
        for v in active:
            d = 0
            for u in adj[v]:
                if popcount[a[u]] > 1:
                    d += 1
            deg[v] = d
            if d > maxd:
                maxd = d

        if maxd <= 2:
            visited = [False] * (n + 1)
            for v in active:
                if visited[v]:
                    continue
                comp = []
                stack = [v]
                visited[v] = True
                while stack:
                    x = stack.pop()
                    comp.append(x)
                    for u in adj[x]:
                        if popcount[a[u]] > 1 and not visited[u]:
                            visited[u] = True
                            stack.append(u)
                endpoints = [x for x in comp if deg[x] == 1]
                if len(comp) == 1 or endpoints:
                    continue
                start = comp[0]
                order = []
                prev = -1
                cur = start
                while True:
                    order.append(cur)
                    nxt = -1
                    for u in adj[cur]:
                        if popcount[a[u]] > 1 and u != prev:
                            nxt = u
                            break
                    if nxt == -1 or nxt == start:
                        break
                    prev, cur = cur, nxt
                if not cycle_colorable(order, a):
                    return False
            return True

        v = active[0]
        for x in active[1:]:
            if popcount[a[x]] < popcount[a[v]]:
                v = x
            elif popcount[a[x]] == popcount[a[v]] and deg[x] > deg[v]:
                v = x
        for c in (1, 2, 3):
            bit = 1 << (c - 1)
            if a[v] & bit:
                na = a[:]
                na[v] = bit
                if is_colorable(na):
                    return True
        return False

    allowed = [7] * (n + 1)
    color = [0] * (n + 1)

    def do_assign(v, c, changes):
        bit = 1 << (c - 1)
        if not (allowed[v] & bit):
            return False
        changes.append((v, allowed[v]))
        allowed[v] = bit
        color[v] = c
        q = deque([v])
        while q:
            x = q.pop()
            cx = allowed_mask_to_color[allowed[x]]
            cm = 1 << (cx - 1)
            for u in adj[x]:
                if color[u] == cx:
                    return False
                if allowed[u] & cm:
                    new = allowed[u] & ~cm
                    if new == 0:
                        return False
                    if allowed[u] != new:
                        changes.append((u, allowed[u]))
                        allowed[u] = new
                        if popcount[new] == 1:
                            cc = allowed_mask_to_color[new]
                            if color[u] != 0 and color[u] != cc:
                                return False
                            color[u] = cc
                            q.append(u)
        return True

    for i in range(1, n + 1):
        if color[i] != 0:
            continue
        chosen = False
        for c in (1, 2, 3):
            bit = 1 << (c - 1)
            if not (allowed[i] & bit):
                continue
            changes = []
            if do_assign(i, c, changes):
                if is_colorable(allowed[:]):
                    chosen = True
                    break
            for v, old in reversed(changes):
                allowed[v] = old
                color[v] = 0
        if not chosen:
            sys.stdout.write("NO")
            return

    sys.stdout.write("YES\n")
    sys.stdout.write(' '.join(str(color[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    solve()