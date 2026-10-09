import sys
from collections import deque

sys.setrecursionlimit(1_000_000)

def read_ints():
    data = sys.stdin.buffer.read()
    num = 0
    in_num = False
    for c in data:
        if 48 <= c <= 57:
            num = num * 10 + c - 48
            in_num = True
        elif in_num:
            yield num
            num = 0
            in_num = False
    if in_num:
        yield num

it = iter(read_ints())
n_left = next(it)
n_right = next(it)
m = next(it)

U = [0] * m
V = [0] * m
deg_left = [0] * n_left
deg_right = [0] * n_right

for i in range(m):
    u = next(it) - 1
    v = next(it) - 1
    U[i] = u
    V[i] = v
    deg_left[u] += 1
    deg_right[v] += 1

if m == 0:
    sys.stdout.write("YES\n\n")
    sys.exit()

Delta = max(max(deg_left), max(deg_right))

def make_bins(degrees, capacity):
    mapping = [0] * len(degrees)
    loads = []
    current = -1
    current_load = 0

    for vertex, degree in enumerate(degrees):
        if degree == 0:
            continue
        if current == -1 or current_load + degree > capacity:
            loads.append(0)
            current += 1
            current_load = 0
        mapping[vertex] = current
        current_load += degree
        loads[current] = current_load

    return mapping, loads

map_left, loads_left = make_bins(deg_left, Delta)
map_right, loads_right = make_bins(deg_right, Delta)

for i in range(m):
    U[i] = map_left[U[i]]
    V[i] = map_right[V[i]]

N = max(len(loads_left), len(loads_right))
loads_left.extend([0] * (N - len(loads_left)))
loads_right.extend([0] * (N - len(loads_right)))

# Add dummy edges to obtain a Delta-regular balanced bipartite multigraph.
i = 0
j = 0
remaining_left = Delta - loads_left[0]
remaining_right = Delta - loads_right[0]

while i < N and j < N:
    take = remaining_left if remaining_left < remaining_right else remaining_right
    if take:
        U.extend([i] * take)
        V.extend([j] * take)
        remaining_left -= take
        remaining_right -= take

    if remaining_left == 0:
        i += 1
        if i < N:
            remaining_left = Delta - loads_left[i]

    if remaining_right == 0:
        j += 1
        if j < N:
            remaining_right = Delta - loads_right[j]

total_edges = len(U)
answer = [0] * m

if N == 1:
    for eid in range(m):
        answer[eid] = eid + 1
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, answer)))
    sys.stdout.write("\n")
    sys.exit()

def perfect_matching(edges):
    adjacency = [[] for _ in range(N)]
    for eid in edges:
        adjacency[U[eid]].append(eid)

    pair_left = [-1] * N
    pair_right = [-1] * N

    # Greedy initialization.
    for eid in edges:
        u = U[eid]
        v = V[eid]
        if pair_left[u] == -1 and pair_right[v] == -1:
            pair_left[u] = eid
            pair_right[v] = eid

    inf = N + 1
    dist = [inf] * N
    ptr = [0] * N

    def bfs():
        q = deque()
        shortest = inf

        for u in range(N):
            if pair_left[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = inf

        while q:
            u = q.popleft()
            if dist[u] + 1 > shortest:
                continue
            for eid in adjacency[u]:
                v = V[eid]
                matched = pair_right[v]
                if matched == -1:
                    shortest = dist[u] + 1
                else:
                    next_u = U[matched]
                    if dist[next_u] == inf:
                        dist[next_u] = dist[u] + 1
                        q.append(next_u)

        return shortest

    def dfs(u, shortest):
        adj_u = adjacency[u]
        while ptr[u] < len(adj_u):
            eid = adj_u[ptr[u]]
            ptr[u] += 1
            v = V[eid]
            matched = pair_right[v]

            if matched == -1:
                if dist[u] + 1 == shortest:
                    pair_left[u] = eid
                    pair_right[v] = eid
                    return True
            else:
                next_u = U[matched]
                if dist[next_u] == dist[u] + 1 and dfs(next_u, shortest):
                    pair_left[u] = eid
                    pair_right[v] = eid
                    return True

        dist[u] = inf
        return False

    while True:
        shortest = bfs()
        if shortest == inf:
            break
        ptr = [0] * N
        for u in range(N):
            if pair_left[u] == -1:
                dfs(u, shortest)

    return pair_left

def split_even(edges):
    size = len(edges)
    mate_left = [-1] * size
    mate_right = [-1] * size
    pending_left = [-1] * N
    pending_right = [-1] * N

    for pos, eid in enumerate(edges):
        u = U[eid]
        previous = pending_left[u]
        if previous == -1:
            pending_left[u] = pos
        else:
            mate_left[pos] = previous
            mate_left[previous] = pos
            pending_left[u] = -1

        v = V[eid]
        previous = pending_right[v]
        if previous == -1:
            pending_right[v] = pos
        else:
            mate_right[pos] = previous
            mate_right[previous] = pos
            pending_right[v] = -1

    state = bytearray(size)
    stack = []
    for start in range(size):
        if state[start]:
            continue
        state[start] = 1
        stack.append(start)
        while stack:
            x = stack.pop()
            next_state = 3 - state[x]

            y = mate_left[x]
            if state[y] == 0:
                state[y] = next_state
                stack.append(y)

            y = mate_right[x]
            if state[y] == 0:
                state[y] = next_state
                stack.append(y)

    first = []
    second = []
    append_first = first.append
    append_second = second.append

    for pos, eid in enumerate(edges):
        if state[pos] == 1:
            append_first(eid)
        else:
            append_second(eid)

    return first, second

def assign_degree_two(edges, first_color):
    first, second = split_even(edges)
    second_color = first_color + 1
    for eid in first:
        if eid < m:
            answer[eid] = first_color
    for eid in second:
        if eid < m:
            answer[eid] = second_color

def factor(edges, degree, first_color):
    if degree == 1:
        for eid in edges:
            if eid < m:
                answer[eid] = first_color
        return

    if degree == 2:
        assign_degree_two(edges, first_color)
        return

    if degree & 1:
        matching = perfect_matching(edges)
        selected = set(matching)

        for eid in matching:
            if eid < m:
                answer[eid] = first_color

        remaining = [eid for eid in edges if eid not in selected]

        if degree - 1 == 2:
            assign_degree_two(remaining, first_color + 1)
        else:
            factor(remaining, degree - 1, first_color + 1)
    else:
        first, second = split_even(edges)
        half = degree // 2
        factor(first, half, first_color)
        factor(second, half, first_color + half)

factor(list(range(total_edges)), Delta, 1)

sys.stdout.write("YES\n")
sys.stdout.write(" ".join(map(str, answer)))
sys.stdout.write("\n")