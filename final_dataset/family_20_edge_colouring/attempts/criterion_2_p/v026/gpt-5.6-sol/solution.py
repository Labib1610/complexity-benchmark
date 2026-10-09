import sys
from collections import deque

sys.setrecursionlimit(1_000_000)

data = list(map(int, sys.stdin.buffer.read().split()))
n_left, n_right, m = data[0], data[1], data[2]

U = [0] * m
V = [0] * m
deg_left = [0] * n_left
deg_right = [0] * n_right

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
    raise SystemExit

delta = max(max(deg_left), max(deg_right))
answer = [0] * m

mate_left = [-1] * n_left
mate_right = [-1] * n_right
match_edge_left = [-1] * n_left
match_edge_right = [-1] * n_right


def extract_matching(edges, degree_limit):
    adj_left = {}
    adj_right = {}

    for e in edges:
        u = U[e]
        v = V[e]
        if u in adj_left:
            adj_left[u].append(e)
        else:
            adj_left[u] = [e]
        if v in adj_right:
            adj_right[v].append(e)
        else:
            adj_right[v] = [e]

    touched_left = list(adj_left)
    touched_right = list(adj_right)

    for u in touched_left:
        mate_left[u] = -1
        match_edge_left[u] = -1
    for v in touched_right:
        mate_right[v] = -1
        match_edge_right[v] = -1

    target_left = [u for u, a in adj_left.items() if len(a) == degree_limit]
    target_right = [v for v, a in adj_right.items() if len(a) == degree_limit]

    def augment_left(sources):
        while True:
            active = [x for x in sources if mate_left[x] == -1]
            if not active:
                return

            dist = {}
            q = deque()
            for x in active:
                dist[x] = 0
                q.append(x)

            shortest = -1
            while q:
                x = q.popleft()
                dx = dist[x]
                if shortest != -1 and dx >= shortest:
                    continue
                for e in adj_left[x]:
                    y_opp = V[e]
                    matched = mate_right[y_opp]
                    if matched == -1:
                        shortest = dx + 1
                    elif matched not in dist:
                        dist[matched] = dx + 1
                        q.append(matched)

            if shortest == -1:
                return

            ptr = {x: 0 for x in dist}

            def dfs(x):
                a = adj_left[x]
                i = ptr[x]
                while i < len(a):
                    e = a[i]
                    i += 1
                    ptr[x] = i
                    y_opp = V[e]
                    matched = mate_right[y_opp]

                    if matched == -1:
                        if dist[x] + 1 != shortest:
                            continue
                        mate_left[x] = y_opp
                        mate_right[y_opp] = x
                        match_edge_left[x] = e
                        match_edge_right[y_opp] = e
                        return True

                    if dist.get(matched, -1) == dist[x] + 1 and dfs(matched):
                        mate_left[x] = y_opp
                        mate_right[y_opp] = x
                        match_edge_left[x] = e
                        match_edge_right[y_opp] = e
                        return True

                dist[x] = -1
                return False

            changed = False
            for x in active:
                if mate_left[x] == -1 and x in dist and dfs(x):
                    changed = True
            if not changed:
                return

    def augment_right(sources):
        while True:
            active = [x for x in sources if mate_right[x] == -1]
            if not active:
                return

            dist = {}
            q = deque()
            for x in active:
                dist[x] = 0
                q.append(x)

            shortest = -1
            while q:
                x = q.popleft()
                dx = dist[x]
                if shortest != -1 and dx >= shortest:
                    continue
                for e in adj_right[x]:
                    y_opp = U[e]
                    matched = mate_left[y_opp]
                    if matched == -1:
                        shortest = dx + 1
                    elif matched not in dist:
                        dist[matched] = dx + 1
                        q.append(matched)

            if shortest == -1:
                return

            ptr = {x: 0 for x in dist}

            def dfs(x):
                a = adj_right[x]
                i = ptr[x]
                while i < len(a):
                    e = a[i]
                    i += 1
                    ptr[x] = i
                    y_opp = U[e]
                    matched = mate_left[y_opp]

                    if matched == -1:
                        if dist[x] + 1 != shortest:
                            continue
                        mate_right[x] = y_opp
                        mate_left[y_opp] = x
                        match_edge_right[x] = e
                        match_edge_left[y_opp] = e
                        return True

                    if dist.get(matched, -1) == dist[x] + 1 and dfs(matched):
                        mate_right[x] = y_opp
                        mate_left[y_opp] = x
                        match_edge_right[x] = e
                        match_edge_left[y_opp] = e
                        return True

                dist[x] = -1
                return False

            changed = False
            for x in active:
                if mate_right[x] == -1 and x in dist and dfs(x):
                    changed = True
            if not changed:
                return

    augment_left(target_left)
    augment_right(target_right)

    selected = set()
    for u in touched_left:
        if match_edge_left[u] != -1:
            selected.add(match_edge_left[u])

    matching = []
    remaining = []
    for e in edges:
        if e in selected:
            matching.append(e)
        else:
            remaining.append(e)

    return matching, remaining


def split_even(edges):
    count = len(edges)
    endpoints_a = [0] * count
    endpoints_b = [0] * count
    original = list(edges)
    adjacency = {}

    for i, e in enumerate(edges):
        a = U[e]
        b = n_left + V[e]
        endpoints_a[i] = a
        endpoints_b[i] = b
        adjacency.setdefault(a, []).append(i)
        adjacency.setdefault(b, []).append(i)

    odd_vertices = [x for x, a in adjacency.items() if len(a) & 1]
    super_vertex = n_left + n_right
    original_count = count

    if odd_vertices:
        adjacency[super_vertex] = []
        for x in odd_vertices:
            idx = len(endpoints_a)
            endpoints_a.append(x)
            endpoints_b.append(super_vertex)
            original.append(-1)
            adjacency[x].append(idx)
            adjacency[super_vertex].append(idx)

    total_edges = len(endpoints_a)
    used = bytearray(total_edges)
    ptr = {x: len(a) - 1 for x, a in adjacency.items()}

    first = []
    second = []

    starts = []
    if odd_vertices:
        starts.append(super_vertex)
    starts.extend(adjacency.keys())

    for start in starts:
        astart = adjacency.get(start)
        if not astart:
            continue
        pos = ptr[start]
        while pos >= 0 and used[astart[pos]]:
            pos -= 1
        ptr[start] = pos
        if pos < 0:
            continue

        vertex_stack = [start]
        edge_stack = []
        tour = []

        while vertex_stack:
            x = vertex_stack[-1]
            ax = adjacency[x]
            i = ptr[x]
            while i >= 0 and used[ax[i]]:
                i -= 1
            ptr[x] = i

            if i < 0:
                vertex_stack.pop()
                if edge_stack:
                    tour.append(edge_stack.pop())
                continue

            le = ax[i]
            ptr[x] = i - 1
            if used[le]:
                continue
            used[le] = 1
            y = endpoints_b[le] if endpoints_a[le] == x else endpoints_a[le]
            vertex_stack.append(y)
            edge_stack.append(le)

        parity = 0
        for le in reversed(tour):
            if le >= original_count:
                parity = 0
            else:
                e = original[le]
                if parity == 0:
                    first.append(e)
                else:
                    second.append(e)
                parity ^= 1

    return first, second


stack = [(list(range(m)), delta, 0)]

while stack:
    edges, d, offset = stack.pop()
    if not edges:
        continue

    if d == 1:
        color = offset + 1
        for e in edges:
            answer[e] = color
        continue

    if d & 1:
        matching, remaining = extract_matching(edges, d)
        color = offset + d
        for e in matching:
            answer[e] = color
        if remaining:
            stack.append((remaining, d - 1, offset))
    else:
        a, b = split_even(edges)
        half = d // 2
        if b:
            stack.append((b, half, offset + half))
        if a:
            stack.append((a, half, offset))

sys.stdout.write("YES\n")
sys.stdout.write(" ".join(map(str, answer)))
sys.stdout.write("\n")