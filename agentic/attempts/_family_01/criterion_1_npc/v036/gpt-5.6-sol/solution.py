import sys
from itertools import permutations

sys.setrecursionlimit(10000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]
adj_mask = [0] * n

p = 2
for _ in range(m):
    u = data[p] - 1
    v = data[p + 1] - 1
    p += 2
    if u != v:
        adj_mask[u] |= 1 << v
        adj_mask[v] |= 1 << u

adj_list = [[] for _ in range(n)]
for i in range(n):
    mask = adj_mask[i]
    while mask:
        b = mask & -mask
        j = b.bit_length() - 1
        adj_list[i].append(j)
        mask ^= b

# Split the graph into biconnected blocks.
disc = [-1] * n
low = [0] * n
timer = 0
edge_stack = []
blocks = []

def tarjan(u, parent):
    global timer
    disc[u] = low[u] = timer
    timer += 1

    for v in adj_list[u]:
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

for root in range(n):
    if disc[root] == -1:
        tarjan(root, -1)
        edge_stack.clear()

def solve_block(vertices):
    k = len(vertices)
    if k == 1:
        return [0]

    index = {v: i for i, v in enumerate(vertices)}
    local_adj = [0] * k

    for i, v in enumerate(vertices):
        mask = adj_mask[v]
        for u, j in index.items():
            if mask & (1 << u):
                local_adj[i] |= 1 << j

    # Fast path for bipartite blocks.
    bip_color = [-1] * k
    bipartite = True
    for start in range(k):
        if bip_color[start] != -1:
            continue
        bip_color[start] = 0
        stack = [start]
        while stack and bipartite:
            x = stack.pop()
            mask = local_adj[x]
            while mask:
                b = mask & -mask
                y = b.bit_length() - 1
                mask ^= b
                if bip_color[y] == -1:
                    bip_color[y] = bip_color[x] ^ 1
                    stack.append(y)
                elif bip_color[y] == bip_color[x]:
                    bipartite = False
                    break

    if bipartite:
        return bip_color

    colors = [-1] * k
    domains = [7] * k
    assigned_order = []
    trail = []

    def rollback(trail_mark, assigned_mark):
        while len(trail) > trail_mark:
            v, old_domain = trail.pop()
            domains[v] = old_domain
        while len(assigned_order) > assigned_mark:
            v = assigned_order.pop()
            colors[v] = -1

    def assign(v, c):
        bit = 1 << c
        if colors[v] != -1 or not (domains[v] & bit):
            return False

        colors[v] = c
        assigned_order.append(v)

        mask = local_adj[v]
        while mask:
            b = mask & -mask
            u = b.bit_length() - 1
            mask ^= b
            if colors[u] == -1 and (domains[u] & bit):
                old = domains[u]
                trail.append((u, old))
                domains[u] = old & ~bit
                if domains[u] == 0:
                    return False
        return True

    def dfs():
        entry_trail = len(trail)
        entry_assigned = len(assigned_order)

        while True:
            forced = -1
            for v in range(k):
                if colors[v] == -1:
                    count = domains[v].bit_count()
                    if count == 0:
                        rollback(entry_trail, entry_assigned)
                        return False
                    if count == 1:
                        forced = v
                        break
            if forced == -1:
                break
            c = (domains[forced] & -domains[forced]).bit_length() - 1
            if not assign(forced, c):
                rollback(entry_trail, entry_assigned)
                return False

        best = -1
        best_key = None
        uncolored_mask = 0
        for v in range(k):
            if colors[v] == -1:
                uncolored_mask |= 1 << v

        if uncolored_mask == 0:
            return True

        for v in range(k):
            if colors[v] == -1:
                domain_size = domains[v].bit_count()
                uncolored_degree = (local_adj[v] & uncolored_mask).bit_count()
                key = (domain_size, -uncolored_degree, -local_adj[v].bit_count())
                if best_key is None or key < best_key:
                    best_key = key
                    best = v

        choices = []
        mask = domains[best]
        while mask:
            b = mask & -mask
            c = b.bit_length() - 1
            mask ^= b
            impact = 0
            nbrs = local_adj[best] & uncolored_mask
            while nbrs:
                nb = nbrs & -nbrs
                u = nb.bit_length() - 1
                nbrs ^= nb
                if domains[u] & b:
                    impact += 1
            choices.append((impact, c))
        choices.sort()

        for _, c in choices:
            branch_trail = len(trail)
            branch_assigned = len(assigned_order)
            if assign(best, c) and dfs():
                return True
            rollback(branch_trail, branch_assigned)

        rollback(entry_trail, entry_assigned)
        return False

    root = max(range(k), key=lambda x: local_adj[x].bit_count())
    root_neighbors = local_adj[root]
    if root_neighbors == 0:
        colors[root] = 0
    else:
        neighbor_candidates = []
        mask = root_neighbors
        while mask:
            b = mask & -mask
            v = b.bit_length() - 1
            mask ^= b
            neighbor_candidates.append(v)
        neighbor = max(neighbor_candidates, key=lambda x: local_adj[x].bit_count())

        if not assign(root, 0) or not assign(neighbor, 1):
            return None

    if dfs():
        return colors
    return None

block_solutions = []
for block in blocks:
    solution = solve_block(block)
    if solution is None:
        print("NO")
        sys.exit()
    block_solutions.append(solution)

answer = [-1] * n

# Isolated vertices.
for v in range(n):
    if not adj_list[v]:
        answer[v] = 0

vertex_blocks = [[] for _ in range(n)]
for bi, block in enumerate(blocks):
    for v in block:
        vertex_blocks[v].append(bi)

visited_blocks = [False] * len(blocks)
perms = list(permutations(range(3)))

for start in range(len(blocks)):
    if visited_blocks[start]:
        continue

    visited_blocks[start] = True
    queue = [start]
    head = 0

    while head < len(queue):
        bi = queue[head]
        head += 1
        block = blocks[bi]
        local = block_solutions[bi]

        chosen_perm = None
        for perm in perms:
            valid = True
            for i, v in enumerate(block):
                if answer[v] != -1 and perm[local[i]] != answer[v]:
                    valid = False
                    break
            if valid:
                chosen_perm = perm
                break

        if chosen_perm is None:
            print("NO")
            sys.exit()

        for i, v in enumerate(block):
            answer[v] = chosen_perm[local[i]]

        for v in block:
            for nb in vertex_blocks[v]:
                if not visited_blocks[nb]:
                    visited_blocks[nb] = True
                    queue.append(nb)

for v in range(n):
    if answer[v] == -1:
        answer[v] = 0

print("YES")
print(*(c + 1 for c in answer))