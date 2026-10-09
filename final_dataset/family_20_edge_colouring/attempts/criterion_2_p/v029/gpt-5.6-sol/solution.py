import sys
from collections import deque

sys.setrecursionlimit(1_000_000)

input = sys.stdin.buffer.readline

nA, nB, m = map(int, input().split())

U = [0] * m
V = [0] * m
degree_a = [0] * nA
degree_b = [0] * nB

for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    U[i] = u
    V[i] = v
    degree_a[u] += 1
    degree_b[v] += 1

D = max(max(degree_a, default=0), max(degree_b, default=0))

if m == 0:
    sys.stdout.write("YES\n\n")
    sys.exit()

answer = [0] * m

pair_a = [-1] * m
pair_b = [-1] * m
temporary_color = bytearray(m)
chosen = bytearray(m)

match_a = [-1] * nA
match_b = [-1] * nB

dist_a = [0] * nA
dist_b = [0] * nB
stamp_a = [0] * nA
stamp_b = [0] * nB
phase_counter = 0


def hopcroft_karp(sources, adjacency, source_is_a):
    global phase_counter

    if source_is_a:
        match_s, match_t = match_a, match_b
        dist, stamp = dist_a, stamp_a
        source_endpoint, target_endpoint = U, V
    else:
        match_s, match_t = match_b, match_a
        dist, stamp = dist_b, stamp_b
        source_endpoint, target_endpoint = V, U

    while True:
        phase_counter += 1
        phase = phase_counter
        q = deque()

        for s in sources:
            if match_s[s] == -1:
                stamp[s] = phase
                dist[s] = 0
                q.append(s)

        if not q:
            return

        shortest = 1 << 60

        while q:
            s = q.popleft()
            ds = dist[s]
            if ds + 1 > shortest:
                continue

            for e in adjacency[s]:
                t = target_endpoint[e]
                matched_edge = match_t[t]
                if matched_edge == -1:
                    shortest = ds + 1
                else:
                    ns = source_endpoint[matched_edge]
                    if stamp[ns] != phase:
                        stamp[ns] = phase
                        dist[ns] = ds + 1
                        q.append(ns)

        if shortest == 1 << 60:
            return

        def dfs(s):
            ds = dist[s]
            for e in adjacency[s]:
                t = target_endpoint[e]
                matched_edge = match_t[t]

                if matched_edge == -1:
                    if ds + 1 != shortest:
                        continue
                else:
                    ns = source_endpoint[matched_edge]
                    if (
                        stamp[ns] != phase
                        or dist[ns] != ds + 1
                        or not dfs(ns)
                    ):
                        continue

                match_s[s] = e
                match_t[t] = e
                return True

            dist[s] = -1
            return False

        for s in sources:
            if match_s[s] == -1 and stamp[s] == phase:
                dfs(s)


def extract_matching(edges, degree_bound):
    adjacency_a = {}
    adjacency_b = {}

    for e in edges:
        u = U[e]
        v = V[e]

        lst = adjacency_a.get(u)
        if lst is None:
            adjacency_a[u] = [e]
        else:
            lst.append(e)

        lst = adjacency_b.get(v)
        if lst is None:
            adjacency_b[v] = [e]
        else:
            lst.append(e)

    required_a = []
    required_b = []

    for u, lst in adjacency_a.items():
        match_a[u] = -1
        if len(lst) == degree_bound:
            required_a.append(u)

    for v, lst in adjacency_b.items():
        match_b[v] = -1
        if len(lst) == degree_bound:
            required_b.append(v)

    if required_a:
        hopcroft_karp(required_a, adjacency_a, True)

    if required_b:
        hopcroft_karp(required_b, adjacency_b, False)

    selected = []
    for u in adjacency_a:
        e = match_a[u]
        if e != -1:
            selected.append(e)
            chosen[e] = 1

    return selected


def balanced_split(edges):
    pending_a = {}
    pending_b = {}

    for e in edges:
        pair_a[e] = -1
        pair_b[e] = -1
        temporary_color[e] = 0

        u = U[e]
        previous = pending_a.pop(u, None)
        if previous is None:
            pending_a[u] = e
        else:
            pair_a[e] = previous
            pair_a[previous] = e

        v = V[e]
        previous = pending_b.pop(v, None)
        if previous is None:
            pending_b[v] = e
        else:
            pair_b[e] = previous
            pair_b[previous] = e

    first = []
    second = []

    for start in edges:
        if temporary_color[start]:
            continue

        temporary_color[start] = 1
        stack = [start]

        while stack:
            e = stack.pop()
            color = temporary_color[e]

            if color == 1:
                first.append(e)
            else:
                second.append(e)

            x = pair_a[e]
            if x != -1 and temporary_color[x] == 0:
                temporary_color[x] = 3 - color
                stack.append(x)

            x = pair_b[e]
            if x != -1 and temporary_color[x] == 0:
                temporary_color[x] = 3 - color
                stack.append(x)

    return first, second


tasks = [(list(range(m)), D, 0)]

while tasks:
    edges, degree_bound, offset = tasks.pop()

    if not edges:
        continue

    if degree_bound <= 1:
        color = offset + 1
        for e in edges:
            answer[e] = color
        continue

    if degree_bound & 1:
        matching = extract_matching(edges, degree_bound)
        matching_color = offset + degree_bound

        for e in matching:
            answer[e] = matching_color

        remaining = []
        for e in edges:
            if chosen[e]:
                chosen[e] = 0
            else:
                remaining.append(e)

        if remaining:
            tasks.append((remaining, degree_bound - 1, offset))
    else:
        first, second = balanced_split(edges)
        half = degree_bound // 2

        if second:
            tasks.append((second, half, offset + half))
        if first:
            tasks.append((first, half, offset))

sys.stdout.write("YES\n")
sys.stdout.write(" ".join(map(str, answer)))
sys.stdout.write("\n")