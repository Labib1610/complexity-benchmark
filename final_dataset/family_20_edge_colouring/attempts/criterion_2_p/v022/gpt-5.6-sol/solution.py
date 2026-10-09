import sys
from collections import deque

def cover_required(adj, match_s, match_o, protected):
    while True:
        roots = [s for s in protected if match_s.get(s, -1) == -1]
        if not roots:
            return

        dist = {}
        q = deque()
        for s in roots:
            dist[s] = 0
            q.append(s)

        limit = -1
        while q:
            s = q.popleft()
            d = dist[s]
            if limit != -1 and d + 1 > limit:
                continue
            for o, _ in adj.get(s, ()):
                t = match_o.get(o, -1)
                if t == -1 or t not in protected:
                    if limit == -1:
                        limit = d + 1
                elif limit == -1 or d + 1 < limit:
                    if t not in dist:
                        dist[t] = d + 1
                        q.append(t)

        if limit == -1:
            return

        ptr = {}
        augmented = 0

        for root in roots:
            if match_s.get(root, -1) != -1 or dist.get(root, -1) != 0:
                continue

            stack = [root]
            found_o = -1

            while stack:
                s = stack[-1]
                d = dist.get(s, -1)
                if d < 0:
                    stack.pop()
                    continue

                edges = adj.get(s, ())
                i = ptr.get(s, 0)
                advanced = False

                while i < len(edges):
                    o = edges[i][0]
                    i += 1
                    ptr[s] = i
                    t = match_o.get(o, -1)

                    if t == -1 or t not in protected:
                        if d + 1 == limit:
                            found_o = o
                            advanced = True
                            break
                    elif d + 1 < limit and dist.get(t, -1) == d + 1:
                        stack.append(t)
                        advanced = True
                        break

                if found_o != -1:
                    break
                if not advanced:
                    dist[s] = -1
                    stack.pop()

            if found_o == -1:
                continue

            displaced = match_o.get(found_o, -1)
            if displaced != -1:
                match_s[displaced] = -1

            new_o = found_o
            for s in reversed(stack):
                old_o = match_s.get(s, -1)
                match_s[s] = new_o
                match_o[new_o] = s
                new_o = old_o

            augmented += 1

        if augmented == 0:
            return


def maximum_degree_matching(edge_ids, degree_bound, U, V):
    adj_l = {}
    adj_r = {}
    deg_l = {}
    deg_r = {}

    for eid in edge_ids:
        u = U[eid]
        v = V[eid]
        adj_l.setdefault(u, []).append((v, eid))
        adj_r.setdefault(v, []).append((u, eid))
        deg_l[u] = deg_l.get(u, 0) + 1
        deg_r[v] = deg_r.get(v, 0) + 1

    required_l = {u for u, d in deg_l.items() if d == degree_bound}
    required_r = {v for v, d in deg_r.items() if d == degree_bound}

    match_l = {}
    match_r = {}

    if required_l:
        cover_required(adj_l, match_l, match_r, required_l)
    if required_r:
        cover_required(adj_r, match_r, match_l, required_r)

    selected = []
    used_left = set()
    for eid in edge_ids:
        u = U[eid]
        if u not in used_left and match_l.get(u, -1) == V[eid]:
            selected.append(eid)
            used_left.add(u)

    return selected


def balanced_split(edge_ids, U, V, left_count, right_count):
    if not edge_ids:
        return [], []

    adj = {}
    eu = []
    ev = []
    real = []

    def add_edge(a, b, eid):
        idx = len(eu)
        eu.append(a)
        ev.append(b)
        real.append(eid)
        adj.setdefault(a, []).append(idx)
        adj.setdefault(b, []).append(idx)

    degree = {}
    offset = left_count
    for eid in edge_ids:
        a = U[eid]
        b = offset + V[eid]
        add_edge(a, b, eid)
        degree[a] = degree.get(a, 0) + 1
        degree[b] = degree.get(b, 0) + 1

    dummy_l = left_count + right_count
    dummy_r = dummy_l + 1

    odd_l = []
    odd_r = []
    for x, d in degree.items():
        if d & 1:
            if x < offset:
                odd_l.append(x)
            else:
                odd_r.append(x)

    for x in odd_l:
        add_edge(x, dummy_r, -1)
    for x in odd_r:
        add_edge(x, dummy_l, -1)
    if len(odd_l) & 1:
        add_edge(dummy_l, dummy_r, -1)

    used = bytearray(len(eu))
    first = []
    second = []

    for start in list(adj.keys()):
        while adj[start] and used[adj[start][-1]]:
            adj[start].pop()
        if not adj[start]:
            continue

        stack_v = [start]
        stack_e = [-1]
        circuit = []

        while stack_v:
            x = stack_v[-1]
            lst = adj[x]
            while lst and used[lst[-1]]:
                lst.pop()

            if lst:
                e = lst.pop()
                if used[e]:
                    continue
                used[e] = 1
                y = ev[e] if eu[e] == x else eu[e]
                stack_v.append(y)
                stack_e.append(e)
            else:
                stack_v.pop()
                e = stack_e.pop()
                if e != -1:
                    circuit.append(e)

        for i, e in enumerate(circuit):
            eid = real[e]
            if eid != -1:
                if i & 1:
                    second.append(eid)
                else:
                    first.append(eid)

    return first, second


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    nl, nr, m = data[0], data[1], data[2]
    U = [0] * m
    V = [0] * m
    deg_l = [0] * nl
    deg_r = [0] * nr

    p = 3
    for i in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        U[i] = u
        V[i] = v
        deg_l[u] += 1
        deg_r[v] += 1

    if m == 0:
        sys.stdout.write("YES\n\n")
        return

    delta = max(max(deg_l), max(deg_r))
    answer = [0] * m

    tasks = [(list(range(m)), delta, 1)]

    while tasks:
        edges, d, base = tasks.pop()
        if not edges:
            continue
        if d == 1:
            for eid in edges:
                answer[eid] = base
            continue

        if d & 1:
            matching = maximum_degree_matching(edges, d, U, V)
            chosen = set(matching)
            for eid in matching:
                answer[eid] = base + d - 1
            remaining = [eid for eid in edges if eid not in chosen]
            tasks.append((remaining, d - 1, base))
        else:
            a, b = balanced_split(edges, U, V, nl, nr)
            half = d // 2
            tasks.append((b, half, base + half))
            tasks.append((a, half, base))

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, answer)))
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()