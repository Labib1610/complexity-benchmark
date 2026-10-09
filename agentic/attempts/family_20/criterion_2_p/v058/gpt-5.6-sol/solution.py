import sys
from array import array
from collections import deque

sys.setrecursionlimit(1_000_000)

data = list(map(int, sys.stdin.buffer.read().split()))
nL, nR, m = data[0], data[1], data[2]

if m == 0:
    sys.stdout.write("YES\n\n")
    raise SystemExit

degL = [0] * nL
degR = [0] * nR
orig_u = array('i')
orig_v = array('i')

p = 3
for _ in range(m):
    u = data[p] - 1
    v = data[p + 1] - 1
    p += 2
    orig_u.append(u)
    orig_v.append(v)
    degL[u] += 1
    degR[v] += 1

D = max(max(degL), max(degR))


def pack_vertices(deg, capacity):
    mapping = array('i', [-1]) * len(deg)
    bin_count = 0
    current_load = 0

    for vertex, d in enumerate(deg):
        if d == 0:
            continue
        if current_load and current_load + d > capacity:
            bin_count += 1
            current_load = 0
        mapping[vertex] = bin_count
        current_load += d

    if current_load:
        bin_count += 1
    return mapping, bin_count


mapL, binsL = pack_vertices(degL, D)
mapR, binsR = pack_vertices(degR, D)
N = max(binsL, binsR)

U = array('i')
V = array('i')
degree_packed_L = [0] * N
degree_packed_R = [0] * N

for i in range(m):
    u = mapL[orig_u[i]]
    v = mapR[orig_v[i]]
    U.append(u)
    V.append(v)
    degree_packed_L[u] += 1
    degree_packed_R[v] += 1

i = j = 0
left_need = D - degree_packed_L[0] if N else 0
right_need = D - degree_packed_R[0] if N else 0

while i < N and j < N:
    if left_need == 0:
        i += 1
        if i < N:
            left_need = D - degree_packed_L[i]
        continue
    if right_need == 0:
        j += 1
        if j < N:
            right_need = D - degree_packed_R[j]
        continue

    take = left_need if left_need < right_need else right_need
    if take:
        U.extend(array('i', [i]) * take)
        V.extend(array('i', [j]) * take)
        left_need -= take
        right_need -= take

E = len(U)
answer = array('i', [0]) * m


def direct_decomposition():
    counts = [[0] * N for _ in range(N)]
    originals = [[None] * N for _ in range(N)]

    for e in range(E):
        counts[U[e]][V[e]] += 1

    for e in range(m):
        u = U[e]
        v = V[e]
        lst = originals[u][v]
        if lst is None:
            lst = []
            originals[u][v] = lst
        lst.append(e)

    color_base = 1
    seen = [0] * N
    seen_token = 0

    while color_base <= D:
        match_r = [-1] * N

        def augment(u):
            nonlocal seen_token
            row = counts[u]
            for v in range(N):
                if row[v] and seen[v] != seen_token:
                    seen[v] = seen_token
                    old = match_r[v]
                    if old == -1 or augment(old):
                        match_r[v] = u
                        return True
            return False

        for u in range(N):
            seen_token += 1
            augment(u)

        match_l = [-1] * N
        for v, u in enumerate(match_r):
            match_l[u] = v

        take = D - color_base + 1
        for u, v in enumerate(match_l):
            if counts[u][v] < take:
                take = counts[u][v]

        for u, v in enumerate(match_l):
            counts[u][v] -= take
            lst = originals[u][v]
            if lst:
                k = min(take, len(lst))
                for offset in range(k):
                    answer[lst.pop()] = color_base + offset

        color_base += take


if N <= 30:
    direct_decomposition()
else:
    next_left = array('i', [-1]) * E
    next_right = array('i', [-1]) * E
    marks = array('I', [0]) * E
    mark_token = 0

    def perfect_matching(edges):
        head = [-1] * N
        for e in edges:
            u = U[e]
            next_left[e] = head[u]
            head[u] = e

        match_l = [-1] * N
        match_r = [-1] * N
        dist = [-1] * N
        ptr = [-1] * N
        matched = 0

        def dfs(u):
            e = ptr[u]
            while e != -1:
                ptr[u] = next_left[e]
                v = V[e]
                old_edge = match_r[v]
                if old_edge == -1:
                    match_l[u] = e
                    match_r[v] = e
                    return True

                old_u = U[old_edge]
                if dist[old_u] == dist[u] + 1 and dfs(old_u):
                    match_l[u] = e
                    match_r[v] = e
                    return True
                e = ptr[u]

            dist[u] = -1
            return False

        while matched < N:
            q = deque()
            for u in range(N):
                if match_l[u] == -1:
                    dist[u] = 0
                    q.append(u)
                else:
                    dist[u] = -1

            while q:
                u = q.popleft()
                e = head[u]
                while e != -1:
                    old_edge = match_r[V[e]]
                    if old_edge != -1:
                        old_u = U[old_edge]
                        if dist[old_u] == -1:
                            dist[old_u] = dist[u] + 1
                            q.append(old_u)
                    e = next_left[e]

            ptr[:] = array('i', head)
            gained = 0
            for u in range(N):
                if match_l[u] == -1 and dfs(u):
                    gained += 1
            matched += gained

        return match_l

    def split_even(edges):
        nonlocal_dummy = None
        global mark_token
        mark_token += 1
        token = mark_token

        head_l = [-1] * N
        head_r = [-1] * N

        for e in edges:
            u = U[e]
            v = V[e]
            next_left[e] = head_l[u]
            head_l[u] = e
            next_right[e] = head_r[v]
            head_r[v] = e

        first = array('i')
        second = array('i')

        for start_edge in edges:
            if marks[start_edge] == token:
                continue

            side = 0
            vertex = U[start_edge]
            parity = 0

            while True:
                if side == 0:
                    e = head_l[vertex]
                    while e != -1 and marks[e] == token:
                        e = next_left[e]
                    head_l[vertex] = e
                    if e == -1:
                        break
                    head_l[vertex] = next_left[e]
                    next_vertex = V[e]
                else:
                    e = head_r[vertex]
                    while e != -1 and marks[e] == token:
                        e = next_right[e]
                    head_r[vertex] = e
                    if e == -1:
                        break
                    head_r[vertex] = next_right[e]
                    next_vertex = U[e]

                marks[e] = token
                if parity == 0:
                    first.append(e)
                else:
                    second.append(e)
                parity ^= 1
                side ^= 1
                vertex = next_vertex

        return first, second

    all_edges = array('i', range(E))
    tasks = [(all_edges, D, 1)]

    while tasks:
        edges, degree, base_color = tasks.pop()

        if degree == 1:
            for e in edges:
                if e < m:
                    answer[e] = base_color
            continue

        if degree & 1:
            matching = perfect_matching(edges)
            mark_token += 1
            token = mark_token

            for e in matching:
                marks[e] = token
                if e < m:
                    answer[e] = base_color

            remaining = array('i')
            for e in edges:
                if marks[e] != token:
                    remaining.append(e)

            tasks.append((remaining, degree - 1, base_color + 1))
        else:
            first, second = split_even(edges)
            half = degree // 2

            if half == 1:
                for e in first:
                    if e < m:
                        answer[e] = base_color
                for e in second:
                    if e < m:
                        answer[e] = base_color + 1
            else:
                tasks.append((second, half, base_color + half))
                tasks.append((first, half, base_color))

sys.stdout.write("YES\n")
sys.stdout.write(" ".join(map(str, answer)))
sys.stdout.write("\n")