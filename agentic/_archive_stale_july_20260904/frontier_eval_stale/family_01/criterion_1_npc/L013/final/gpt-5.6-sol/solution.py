import sys

sys.setrecursionlimit(1000000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]
adj_bits = [0] * n
p = 2

for _ in range(m):
    u = data[p] - 1
    v = data[p + 1] - 1
    p += 2
    if u != v:
        adj_bits[u] |= 1 << v
        adj_bits[v] |= 1 << u

adj = []
for v in range(n):
    bits = adj_bits[v]
    vertices = []
    while bits:
        b = bits & -bits
        vertices.append(b.bit_length() - 1)
        bits -= b
    adj.append(vertices)

popcount = (0, 1, 1, 2, 1, 2, 2, 3)
single = (False, True, True, False, True, False, False, False)

def normalize(domains):
    d = list(domains)
    queue = [v for v in range(n) if single[d[v]]]
    processed = [False] * n

    while queue:
        v = queue.pop()
        if processed[v]:
            continue
        processed[v] = True
        color = d[v]

        for u in adj[v]:
            if d[u] & color:
                nd = d[u] & ~color
                if nd == 0:
                    return None
                d[u] = nd
                if single[nd]:
                    queue.append(u)

    return tuple(d)

def two_sat_feasible(state, unresolved):
    k = len(unresolved)
    index = [-1] * n
    options = [None] * n

    for i, v in enumerate(unresolved):
        index[v] = i
        mask = state[v]
        a = mask & -mask
        b = mask ^ a
        options[v] = (a, b)

    size = 2 * k
    graph = [[] for _ in range(size)]
    reverse = [[] for _ in range(size)]

    def add_edge(a, b):
        graph[a].append(b)
        reverse[b].append(a)

    for u in unresolved:
        iu = index[u]
        ou = options[u]
        for v in adj[u]:
            if v <= u or index[v] < 0:
                continue
            iv = index[v]
            ov = options[v]

            for au in range(2):
                color = ou[au]
                if ov[0] == color:
                    av = 0
                elif ov[1] == color:
                    av = 1
                else:
                    continue

                lu = 2 * iu + au
                lv = 2 * iv + av
                add_edge(lu, lv ^ 1)
                add_edge(lv, lu ^ 1)

    visited = [False] * size
    order = []

    for start in range(size):
        if visited[start]:
            continue
        visited[start] = True
        stack = [(start, 0)]

        while stack:
            v, i = stack[-1]
            if i < len(graph[v]):
                u = graph[v][i]
                stack[-1] = (v, i + 1)
                if not visited[u]:
                    visited[u] = True
                    stack.append((u, 0))
            else:
                order.append(v)
                stack.pop()

    component = [-1] * size
    cid = 0

    for start in reversed(order):
        if component[start] != -1:
            continue
        component[start] = cid
        stack = [start]

        while stack:
            v = stack.pop()
            for u in reverse[v]:
                if component[u] == -1:
                    component[u] = cid
                    stack.append(u)
        cid += 1

    for i in range(k):
        if component[2 * i] == component[2 * i + 1]:
            return False
    return True

cache = {}
CACHE_LIMIT = 120000

def feasible(state):
    cached = cache.get(state)
    if cached is not None:
        return cached

    unresolved = []
    has_three = False

    for v, mask in enumerate(state):
        pc = popcount[mask]
        if pc > 1:
            unresolved.append(v)
            if pc == 3:
                has_three = True

    if not unresolved:
        result = True
    elif not has_three:
        result = two_sat_feasible(state, unresolved)
    else:
        best = -1
        best_key = None

        for v in unresolved:
            mask = state[v]
            residual_degree = 0
            for u in adj[v]:
                if popcount[state[u]] > 1:
                    residual_degree += 1

            key = (-popcount[mask], residual_degree, len(adj[v]))
            if best_key is None or key > best_key:
                best_key = key
                best = v

        mask = state[best]

        if mask == 7 and all(popcount[state[v]] == 3 for v in unresolved):
            colors = [1]
        else:
            colors = []
            bits = mask
            while bits:
                color = bits & -bits
                bits -= color
                impact = 0
                for u in adj[best]:
                    if popcount[state[u]] > 1 and state[u] & color:
                        impact += 1
                colors.append((impact, color))
            colors.sort()
            colors = [color for _, color in colors]

        result = False
        for color in colors:
            child = list(state)
            child[best] = color
            child = normalize(child)
            if child is not None and feasible(child):
                result = True
                break

    if len(cache) < CACHE_LIMIT:
        cache[state] = result
    return result

base = normalize((7,) * n)
answer = [0] * n

for i in range(n):
    chosen = False
    for color_number, color_bit in ((1, 1), (2, 2), (3, 4)):
        if not (base[i] & color_bit):
            continue

        candidate = list(base)
        candidate[i] = color_bit
        candidate = normalize(candidate)

        if candidate is not None and feasible(candidate):
            base = candidate
            answer[i] = color_number
            chosen = True
            break

    if not chosen:
        print("NO")
        sys.exit()

print("YES")
print(*answer)