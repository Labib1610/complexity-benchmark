import sys
from array import array

sys.setrecursionlimit(1_000_000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n_left, n_right, m = data[0], data[1], data[2]

U = array('i', [0]) * m
V = array('i', [0]) * m

deg_left = array('i', [0]) * n_left
deg_right = array('i', [0]) * n_right

p = 3
for i in range(m):
    u = data[p] - 1
    v = data[p + 1] - 1
    p += 2
    U[i] = u
    V[i] = v
    deg_left[u] += 1
    deg_right[v] += 1

if m == 0:
    sys.stdout.write("YES\n\n")
    sys.exit()

max_degree = max(max(deg_left), max(deg_right))

next_left = array('i', [-1]) * m
next_right = array('i', [-1]) * m
link_left = array('i', [-1]) * m
link_right = array('i', [-1]) * m
selected = bytearray(m)
seen = bytearray(m)
answer = array('i', [0]) * m

match_left = array('i', [-1]) * n_left
match_right = array('i', [-1]) * n_right
match_edge_left = array('i', [-1]) * n_left
match_edge_right = array('i', [-1]) * n_right

dist_left = array('i', [-1]) * n_left
dist_right = array('i', [-1]) * n_right

color_counter = 0


def build_adjacency(edges):
    head_l = {}
    head_r = {}
    degree_l = {}
    degree_r = {}

    for e in edges:
        u = U[e]
        v = V[e]

        next_left[e] = head_l.get(u, -1)
        head_l[u] = e
        degree_l[u] = degree_l.get(u, 0) + 1

        next_right[e] = head_r.get(v, -1)
        head_r[v] = e
        degree_r[v] = degree_r.get(v, 0) + 1

    return head_l, head_r, degree_l, degree_r


def augment_hopcroft_karp(roots, head, nxt, opposite, pair_a, pair_b,
                          edge_a, edge_b, dist):
    roots = [x for x in roots if pair_a[x] == -1]
    while roots:
        for x in head:
            dist[x] = -1

        queue = []
        for x in roots:
            if pair_a[x] == -1:
                dist[x] = 0
                queue.append(x)

        shortest = 1 << 30
        qi = 0
        while qi < len(queue):
            a = queue[qi]
            qi += 1
            da = dist[a]
            if da + 1 > shortest:
                continue

            e = head.get(a, -1)
            while e != -1:
                b = opposite[e]
                a2 = pair_b[b]
                if a2 == -1:
                    if da + 1 < shortest:
                        shortest = da + 1
                elif da + 1 < shortest and dist[a2] == -1:
                    dist[a2] = da + 1
                    queue.append(a2)
                e = nxt[e]

        if shortest == (1 << 30):
            break

        ptr = head.copy()

        def dfs(a):
            e = ptr.get(a, -1)
            while e != -1:
                ptr[a] = nxt[e]
                b = opposite[e]
                a2 = pair_b[b]

                if a2 == -1:
                    if dist[a] + 1 == shortest:
                        pair_a[a] = b
                        pair_b[b] = a
                        edge_a[a] = e
                        edge_b[b] = e
                        return True
                elif dist[a2] == dist[a] + 1 and dfs(a2):
                    pair_a[a] = b
                    pair_b[b] = a
                    edge_a[a] = e
                    edge_b[b] = e
                    return True

                e = ptr.get(a, -1)

            dist[a] = -1
            return False

        changed = False
        for a in roots:
            if pair_a[a] == -1 and dist[a] == 0:
                if dfs(a):
                    changed = True

        if not changed:
            break

        roots = [x for x in roots if pair_a[x] == -1]


def extract_matching(edges, degree_bound):
    head_l, head_r, degree_l, degree_r = build_adjacency(edges)

    touched_l = list(head_l.keys())
    touched_r = list(head_r.keys())

    for u in touched_l:
        match_left[u] = -1
        match_edge_left[u] = -1
    for v in touched_r:
        match_right[v] = -1
        match_edge_right[v] = -1

    required_l = [u for u, d in degree_l.items() if d == degree_bound]
    required_r = [v for v, d in degree_r.items() if d == degree_bound]

    augment_hopcroft_karp(
        required_l, head_l, next_left, V,
        match_left, match_right,
        match_edge_left, match_edge_right,
        dist_left
    )

    augment_hopcroft_karp(
        required_r, head_r, next_right, U,
        match_right, match_left,
        match_edge_right, match_edge_left,
        dist_right
    )

    matching = []
    for u in touched_l:
        e = match_edge_left[u]
        if e != -1 and not selected[e]:
            selected[e] = 1
            matching.append(e)

    remainder = []
    for e in edges:
        if selected[e]:
            selected[e] = 0
        else:
            remainder.append(e)

    return matching, remainder


def balanced_split(edges):
    head_l = {}
    head_r = {}

    for e in edges:
        link_left[e] = -1
        link_right[e] = -1
        seen[e] = 0

        u = U[e]
        v = V[e]

        next_left[e] = head_l.get(u, -1)
        head_l[u] = e

        next_right[e] = head_r.get(v, -1)
        head_r[v] = e

    for first in head_l.values():
        e = first
        while e != -1:
            e2 = next_left[e]
            if e2 == -1:
                break
            link_left[e] = e2
            link_left[e2] = e
            e = next_left[e2]

    for first in head_r.values():
        e = first
        while e != -1:
            e2 = next_right[e]
            if e2 == -1:
                break
            link_right[e] = e2
            link_right[e2] = e
            e = next_right[e2]

    part_a = []
    part_b = []

    def traverse(start):
        previous = -1
        current = start
        parity = 0

        while current != -1 and not seen[current]:
            seen[current] = 1
            if parity == 0:
                part_a.append(current)
            else:
                part_b.append(current)
            parity ^= 1

            a = link_left[current]
            b = link_right[current]
            if a != -1 and a != previous:
                nxt_edge = a
            elif b != -1 and b != previous:
                nxt_edge = b
            else:
                nxt_edge = -1

            previous, current = current, nxt_edge

    for e in edges:
        if not seen[e] and (link_left[e] == -1 or link_right[e] == -1):
            traverse(e)

    for e in edges:
        if not seen[e]:
            traverse(e)

    return part_a, part_b


def solve(edges, degree_bound):
    global color_counter

    if not edges:
        return

    if degree_bound == 1:
        color_counter += 1
        c = color_counter
        for e in edges:
            answer[e] = c
        return

    if degree_bound & 1:
        matching, remainder = extract_matching(edges, degree_bound)

        color_counter += 1
        c = color_counter
        for e in matching:
            answer[e] = c

        solve(remainder, degree_bound - 1)
    else:
        first, second = balanced_split(edges)
        half = degree_bound // 2
        solve(first, half)
        solve(second, half)


solve(list(range(m)), max_degree)

sys.stdout.write("YES\n")
sys.stdout.write(" ".join(map(str, answer)))
sys.stdout.write("\n")