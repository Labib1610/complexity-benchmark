import sys
from collections import deque

sys.setrecursionlimit(10000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

it = iter(data)
n = next(it)
m = next(it)

adj = [0] * n
for _ in range(m):
    u = next(it) - 1
    v = next(it) - 1
    if u != v:
        adj[u] |= 1 << v
        adj[v] |= 1 << u

# Remove vertices of degree at most two. Any coloring of the remaining
# graph can be extended in reverse removal order.
alive = [True] * n
degree = [adj[v].bit_count() for v in range(n)]
queue = deque(v for v in range(n) if degree[v] <= 2)
removed = []

while queue:
    v = queue.popleft()
    if not alive[v] or degree[v] > 2:
        continue
    alive[v] = False
    removed.append(v)

    mask = adj[v]
    while mask:
        bit = mask & -mask
        mask -= bit
        u = bit.bit_length() - 1
        if alive[u]:
            degree[u] -= 1
            if degree[u] <= 2:
                queue.append(u)

core_mask = 0
for v in range(n):
    if alive[v]:
        core_mask |= 1 << v

# Split the remaining graph into biconnected blocks.
disc = [-1] * n
low = [0] * n
timer = 0
edge_stack = []
blocks = []

def tarjan(u, parent):
    global timer
    disc[u] = low[u] = timer
    timer += 1

    mask = adj[u] & core_mask
    while mask:
        bit = mask & -mask
        mask -= bit
        v = bit.bit_length() - 1

        if disc[v] == -1:
            edge_stack.append((u, v))
            tarjan(v, u)
            low[u] = min(low[u], low[v])

            if low[v] >= disc[u]:
                vertices = set()
                while True:
                    a, b = edge_stack.pop()
                    vertices.add(a)
                    vertices.add(b)
                    if a == u and b == v:
                        break
                blocks.append(list(vertices))
        elif v != parent and disc[v] < disc[u]:
            edge_stack.append((u, v))
            low[u] = min(low[u], disc[v])

mask = core_mask
while mask:
    bit = mask & -mask
    mask -= bit
    root = bit.bit_length() - 1
    if disc[root] == -1:
        tarjan(root, -1)


def solve_block(vertices):
    k = len(vertices)
    index = {v: i for i, v in enumerate(vertices)}
    ladj = [0] * k

    for i, v in enumerate(vertices):
        mask = adj[v]
        while mask:
            bit = mask & -mask
            mask -= bit
            u = bit.bit_length() - 1
            j = index.get(u)
            if j is not None:
                ladj[i] |= 1 << j

    # Fast path for bipartite blocks.
    bip_color = [0] * k
    bipartite = True
    for start in range(k):
        if bip_color[start]:
            continue
        bip_color[start] = 1
        q = deque([start])
        while q and bipartite:
            u = q.popleft()
            mask = ladj[u]
            while mask:
                bit = mask & -mask
                mask -= bit
                v = bit.bit_length() - 1
                if bip_color[v] == 0:
                    bip_color[v] = 3 - bip_color[u]
                    q.append(v)
                elif bip_color[v] == bip_color[u]:
                    bipartite = False
                    break
        if not bipartite:
            break

    if bipartite:
        return bip_color

    full = (1 << k) - 1
    cache = set()
    cache_limit = 300000

    def apply_forced(dom, assigned, forced):
        q = []
        for v, color_bit in forced:
            if not (dom[v] & color_bit):
                return None
            dom[v] = color_bit
            q.append(v)

        while q:
            v = q.pop()
            vb = 1 << v
            if assigned & vb:
                continue

            color_bit = dom[v]
            if color_bit == 0 or color_bit & (color_bit - 1):
                continue

            assigned |= vb
            mask = ladj[v] & (full ^ assigned)

            while mask:
                bit = mask & -mask
                mask -= bit
                u = bit.bit_length() - 1
                new_domain = dom[u] & ~color_bit

                if new_domain != dom[u]:
                    if new_domain == 0:
                        return None
                    dom[u] = new_domain
                    if new_domain & (new_domain - 1) == 0:
                        q.append(u)

        return assigned

    def dfs(dom, assigned):
        if assigned == full:
            return dom

        key = bytes(dom)
        if key in cache:
            return None

        unassigned = full ^ assigned
        chosen = -1
        best = None

        mask = unassigned
        while mask:
            bit = mask & -mask
            mask -= bit
            v = bit.bit_length() - 1
            domain_size = dom[v].bit_count()
            remaining_degree = (ladj[v] & unassigned).bit_count()
            score = (domain_size, -remaining_degree, -ladj[v].bit_count())
            if best is None or score < best:
                best = score
                chosen = v

        choices = []
        color_mask = dom[chosen]
        while color_mask:
            color_bit = color_mask & -color_mask
            color_mask -= color_bit
            impact = 0
            neighbors = ladj[chosen] & unassigned
            while neighbors:
                bit = neighbors & -neighbors
                neighbors -= bit
                u = bit.bit_length() - 1
                if dom[u] & color_bit:
                    impact += 1
            choices.append((impact, color_bit))

        choices.sort()
        for _, color_bit in choices:
            next_dom = dom.copy()
            next_assigned = apply_forced(
                next_dom, assigned, [(chosen, color_bit)]
            )
            if next_assigned is not None:
                result = dfs(next_dom, next_assigned)
                if result is not None:
                    return result

        if len(cache) < cache_limit:
            cache.add(key)
        return None

    fixed = None
    best_triangle_score = -1

    for i in range(k):
        neighbors = ladj[i]
        while neighbors:
            bit = neighbors & -neighbors
            neighbors -= bit
            j = bit.bit_length() - 1
            if j <= i:
                continue
            common = ladj[i] & ladj[j]
            while common:
                cbit = common & -common
                common -= cbit
                t = cbit.bit_length() - 1
                if t <= j:
                    continue
                score = (
                    ladj[i].bit_count()
                    + ladj[j].bit_count()
                    + ladj[t].bit_count()
                )
                if score > best_triangle_score:
                    best_triangle_score = score
                    fixed = [(i, 1), (j, 2), (t, 4)]

    if fixed is None:
        best_edge = None
        best_score = -1
        for i in range(k):
            mask = ladj[i]
            while mask:
                bit = mask & -mask
                mask -= bit
                j = bit.bit_length() - 1
                if i < j:
                    score = ladj[i].bit_count() + ladj[j].bit_count()
                    if score > best_score:
                        best_score = score
                        best_edge = (i, j)
        if best_edge is None:
            fixed = [(0, 1)]
        else:
            fixed = [(best_edge[0], 1), (best_edge[1], 2)]

    domains = [7] * k
    assigned = apply_forced(domains, 0, fixed)
    if assigned is None:
        return None

    result = dfs(domains, assigned)
    if result is None:
        return None

    return [domain.bit_length() for domain in result]


block_solutions = []
for block in blocks:
    solution = solve_block(block)
    if solution is None:
        print("NO")
        sys.exit()
    block_solutions.append(solution)

# Build the block-cut forest and merge block colorings by permuting colors.
memberships = [[] for _ in range(n)]
for b, block in enumerate(blocks):
    for v in block:
        memberships[v].append(b)

answer = [0] * n
visited_blocks = [False] * len(blocks)

def place_block(b, parent_vertex):
    visited_blocks[b] = True
    block = blocks[b]
    local = block_solutions[b]

    if parent_vertex is None:
        mapping = {1: 1, 2: 2, 3: 3}
    else:
        pos = block.index(parent_vertex)
        source_color = local[pos]
        target_color = answer[parent_vertex]

        mapping = {source_color: target_color}
        remaining_sources = [c for c in (1, 2, 3) if c != source_color]
        remaining_targets = [c for c in (1, 2, 3) if c != target_color]
        mapping[remaining_sources[0]] = remaining_targets[0]
        mapping[remaining_sources[1]] = remaining_targets[1]

    for v, color in zip(block, local):
        mapped = mapping[color]
        if answer[v] == 0:
            answer[v] = mapped

    for v in block:
        for child in memberships[v]:
            if not visited_blocks[child]:
                place_block(child, v)

for b in range(len(blocks)):
    if not visited_blocks[b]:
        place_block(b, None)

# Extend the coloring through the peeled vertices.
for v in reversed(removed):
    used = 0
    mask = adj[v]
    while mask:
        bit = mask & -mask
        mask -= bit
        u = bit.bit_length() - 1
        if answer[u]:
            used |= 1 << (answer[u] - 1)

    for color in (1, 2, 3):
        if not (used & (1 << (color - 1))):
            answer[v] = color
            break

print("YES")
print(*answer)