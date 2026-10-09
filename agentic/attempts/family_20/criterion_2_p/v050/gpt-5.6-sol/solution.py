import sys
from collections import deque

sys.setrecursionlimit(1_000_000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n_left, n_right, m = data[0], data[1], data[2]
U = [0] * m
V = [0] * m

degrees_left = [0] * n_left
degrees_right = [0] * n_right

p = 3
for i in range(m):
    u = data[p] - 1
    v = data[p + 1] - 1
    p += 2
    U[i] = u
    V[i] = v
    degrees_left[u] += 1
    degrees_right[v] += 1

K = max(max(degrees_left, default=0), max(degrees_right, default=0))

if m == 0:
    sys.stdout.write("YES\n\n")
    sys.exit()

answer = [0] * m
match_left = [-1] * n_left
match_right = [-1] * n_right
mate_left = [-1] * m
mate_right = [-1] * m
seen_edge = [0] * m
seen_token = 0


def cover_required(required, adjacency, match_a, match_b, opposite, protected):
    """Modify the matching so every vertex in required is matched."""
    protected_set = set(protected)

    # Cheap direct matches first.
    for a in required:
        if match_a[a] != -1:
            continue
        for e in adjacency[a]:
            b = opposite[e]
            if match_b[b] == -1:
                match_a[a] = e
                match_b[b] = e
                break

    while True:
        roots = [a for a in required if match_a[a] == -1]
        if not roots:
            return

        dist = {}
        q = deque()
        for a in roots:
            dist[a] = 0
            q.append(a)

        terminal_exists = False

        while q:
            a = q.popleft()
            nd = dist[a] + 1
            for e in adjacency[a]:
                b = opposite[e]
                old = match_b[b]
                if old == -1:
                    terminal_exists = True
                else:
                    a2 = U[old] if match_a is match_left else V[old]
                    if a2 not in protected_set:
                        terminal_exists = True
                    elif a2 not in dist:
                        dist[a2] = nd
                        q.append(a2)

        if not terminal_exists:
            return

        def dfs(a):
            da = dist[a]
            for e in adjacency[a]:
                b = opposite[e]
                old = match_b[b]

                if old == -1:
                    match_a[a] = e
                    match_b[b] = e
                    return True

                a2 = U[old] if match_a is match_left else V[old]
                if a2 not in protected_set:
                    match_a[a2] = -1
                    match_a[a] = e
                    match_b[b] = e
                    return True

                if dist.get(a2) == da + 1 and dfs(a2):
                    match_a[a] = e
                    match_b[b] = e
                    return True

            dist[a] = -1
            return False

        progress = False
        for a in roots:
            if match_a[a] == -1 and dfs(a):
                progress = True

        if not progress:
            return


def find_covering_matching(inc_left, inc_right, degree_limit):
    required_left = [u for u, edges in inc_left.items()
                     if len(edges) == degree_limit]
    required_right = [v for v, edges in inc_right.items()
                      if len(edges) == degree_limit]

    touched_left = list(inc_left.keys())
    touched_right = list(inc_right.keys())

    for u in touched_left:
        match_left[u] = -1
    for v in touched_right:
        match_right[v] = -1

    cover_required(
        required_left,
        inc_left,
        match_left,
        match_right,
        V,
        required_left
    )

    cover_required(
        required_right,
        inc_right,
        match_right,
        match_left,
        U,
        required_right
    )

    selected = set()
    for u in touched_left:
        e = match_left[u]
        if e != -1:
            selected.add(e)

    for u in touched_left:
        match_left[u] = -1
    for v in touched_right:
        match_right[v] = -1

    return selected


def balanced_split(edges, inc_left, inc_right):
    global seen_token
    seen_token += 1
    token = seen_token

    starts = []

    for e in edges:
        mate_left[e] = -1
        mate_right[e] = -1

    for incident in inc_left.values():
        ln = len(incident)
        for i in range(0, ln - 1, 2):
            a = incident[i]
            b = incident[i + 1]
            mate_left[a] = b
            mate_left[b] = a
        if ln & 1:
            starts.append((incident[-1], 0))

    for incident in inc_right.values():
        ln = len(incident)
        for i in range(0, ln - 1, 2):
            a = incident[i]
            b = incident[i + 1]
            mate_right[a] = b
            mate_right[b] = a
        if ln & 1:
            starts.append((incident[-1], 1))

    first = []
    second = []

    def walk(start_edge, departure_side):
        e = start_edge
        side = departure_side
        parity = 0

        while seen_edge[e] != token:
            seen_edge[e] = token
            if parity == 0:
                first.append(e)
            else:
                second.append(e)
            parity ^= 1

            arrival_side = 1 - side
            if arrival_side == 0:
                nxt = mate_left[e]
            else:
                nxt = mate_right[e]

            if nxt == -1:
                break

            e = nxt
            side = arrival_side

    for e, side in starts:
        if seen_edge[e] != token:
            walk(e, side)

    for e in edges:
        if seen_edge[e] != token:
            walk(e, 0)

    return first, second


def color_edges(edges, capacity, color_start):
    if not edges:
        return

    inc_left = {}
    inc_right = {}
    actual_max = 0

    for e in edges:
        u = U[e]
        v = V[e]

        lst = inc_left.get(u)
        if lst is None:
            inc_left[u] = [e]
        else:
            lst.append(e)

        lst = inc_right.get(v)
        if lst is None:
            inc_right[v] = [e]
        else:
            lst.append(e)

    for lst in inc_left.values():
        if len(lst) > actual_max:
            actual_max = len(lst)
    for lst in inc_right.values():
        if len(lst) > actual_max:
            actual_max = len(lst)

    capacity = min(capacity, actual_max)

    if capacity == 1:
        for e in edges:
            answer[e] = color_start
        return

    if capacity & 1:
        chosen = find_covering_matching(inc_left, inc_right, capacity)
        remaining = []
        special_color = color_start + capacity - 1

        for e in edges:
            if e in chosen:
                answer[e] = special_color
            else:
                remaining.append(e)

        del inc_left, inc_right, chosen
        color_edges(remaining, capacity - 1, color_start)
        return

    first, second = balanced_split(edges, inc_left, inc_right)
    half = capacity // 2

    del inc_left, inc_right
    color_edges(first, half, color_start)
    color_edges(second, half, color_start + half)


color_edges(list(range(m)), K, 1)

sys.stdout.write("YES\n")
sys.stdout.write(" ".join(map(str, answer)))
sys.stdout.write("\n")