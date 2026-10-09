import sys
from collections import deque

sys.setrecursionlimit(1_000_000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

nL, nR, m = data[0], data[1], data[2]
left = [0] * m
right = [0] * m

deg_l = [0] * nL
deg_r = [0] * nR

p = 3
for i in range(m):
    u = data[p] - 1
    v = data[p + 1] - 1
    p += 2
    left[i] = u
    right[i] = v
    deg_l[u] += 1
    deg_r[v] += 1

if m == 0:
    sys.stdout.write("YES\n\n")
    sys.exit()

Delta = max(max(deg_l), max(deg_r))
answer = [0] * m


def covering_matching(edges, bound):
    adj_l = {}
    adj_r = {}
    dl = {}
    dr = {}

    for eid in edges:
        u = left[eid]
        v = right[eid]
        adj_l.setdefault(u, []).append((v, eid))
        adj_r.setdefault(v, []).append((u, eid))
        dl[u] = dl.get(u, 0) + 1
        dr[v] = dr.get(v, 0) + 1

    required_l = [u for u, d in dl.items() if d == bound]
    required_r = [v for v, d in dr.items() if d == bound]

    if not required_l and not required_r:
        return set()

    pair_l = {}
    pair_r = {}
    edge_l = {}

    # Hopcroft-Karp, initially saturating all required left vertices.
    dist = {}

    def bfs():
        q = deque()
        found = False
        for u in required_l:
            if u not in pair_l:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = -1

        while q:
            u = q.popleft()
            nd = dist[u] + 1
            for v, _ in adj_l[u]:
                u2 = pair_r.get(v)
                if u2 is None:
                    found = True
                elif dist.get(u2, -1) == -1:
                    dist[u2] = nd
                    q.append(u2)
        return found

    def dfs_hk(u):
        for v, eid in adj_l[u]:
            u2 = pair_r.get(v)
            if u2 is None or (
                dist.get(u2, -1) == dist[u] + 1 and dfs_hk(u2)
            ):
                pair_l[u] = v
                pair_r[v] = u
                edge_l[u] = eid
                return True
        dist[u] = -1
        return False

    while bfs():
        for u in required_l:
            if u not in pair_l:
                dfs_hk(u)

    # Cover required right vertices while preserving coverage of required left.
    required_r_set = set(required_r)
    seen = {}
    stamp = 0

    def reroute(r):
        nonlocal stamp
        if seen.get(r) == stamp:
            return False
        seen[r] = stamp

        for u, eid in adj_r[r]:
            old_r = pair_l.get(u)

            if old_r is None:
                pair_l[u] = r
                pair_r[r] = u
                edge_l[u] = eid
                return True

            if old_r == r:
                return True

            if old_r not in required_r_set:
                del pair_r[old_r]
                pair_l[u] = r
                pair_r[r] = u
                edge_l[u] = eid
                return True

            if reroute(old_r):
                pair_l[u] = r
                pair_r[r] = u
                edge_l[u] = eid
                return True

        return False

    for r in required_r:
        if r not in pair_r:
            stamp += 1
            reroute(r)

    return set(edge_l.values())


def equitable_split(edges):
    adj = {}
    degree = {}

    for eid in edges:
        u = left[eid]
        v = nL + right[eid]
        adj.setdefault(u, []).append((v, eid))
        adj.setdefault(v, []).append((u, eid))
        degree[u] = degree.get(u, 0) + 1
        degree[v] = degree.get(v, 0) + 1

    odd = [x for x, d in degree.items() if d & 1]
    super_node = nL + nR
    dummy_id = -1

    if odd:
        adj[super_node] = []
        for x in odd:
            adj[super_node].append((x, dummy_id))
            adj[x].append((super_node, dummy_id))
            dummy_id -= 1

    used = set()
    first = []
    second = []

    def traverse(start):
        stack_v = [start]
        stack_e = []
        circuit = []

        while stack_v:
            v = stack_v[-1]
            av = adj.get(v)
            while av and av[-1][1] in used:
                av.pop()

            if av:
                to, eid = av.pop()
                if eid in used:
                    continue
                used.add(eid)
                stack_v.append(to)
                stack_e.append(eid)
            else:
                stack_v.pop()
                if stack_e:
                    circuit.append(stack_e.pop())

        parity = 0
        for eid in reversed(circuit):
            if eid >= 0:
                if parity == 0:
                    first.append(eid)
                else:
                    second.append(eid)
            parity ^= 1

    if odd:
        traverse(super_node)

    for vertex, av in list(adj.items()):
        while av and av[-1][1] in used:
            av.pop()
        if av:
            traverse(vertex)

    return first, second


jobs = [(list(range(m)), Delta, 1)]

while jobs:
    edges, bound, color_start = jobs.pop()

    if not edges:
        continue

    if bound == 1:
        for eid in edges:
            answer[eid] = color_start
        continue

    if bound & 1:
        chosen = covering_matching(edges, bound)
        if chosen:
            for eid in chosen:
                answer[eid] = color_start
            remaining = [eid for eid in edges if eid not in chosen]
        else:
            remaining = edges
        jobs.append((remaining, bound - 1, color_start + 1))
    else:
        a, b = equitable_split(edges)
        half = bound // 2
        jobs.append((b, half, color_start + half))
        jobs.append((a, half, color_start))

sys.stdout.write("YES\n")
sys.stdout.write(" ".join(map(str, answer)) + "\n")