import sys
from collections import deque

sys.setrecursionlimit(10000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]
adj_sets = [set() for _ in range(n)]

p = 2
for _ in range(m):
    u = data[p] - 1
    v = data[p + 1] - 1
    p += 2
    if u != v:
        adj_sets[u].add(v)
        adj_sets[v].add(u)

adj = [list(s) for s in adj_sets]

# Find biconnected components (blocks).
disc = [-1] * n
low = [0] * n
timer = 0
edge_stack = []
blocks = []

def dfs_bcc(u, parent):
    global timer
    disc[u] = low[u] = timer
    timer += 1

    for v in adj[u]:
        if disc[v] == -1:
            edge_stack.append((u, v))
            dfs_bcc(v, u)
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

for start in range(n):
    if disc[start] == -1:
        dfs_bcc(start, -1)
        edge_stack.clear()

def solve_block(vertices):
    k = len(vertices)
    index = {v: i for i, v in enumerate(vertices)}
    local_adj = [0] * k

    for i, u in enumerate(vertices):
        mask = 0
        for v in adj[u]:
            j = index.get(v)
            if j is not None:
                mask |= 1 << j
        local_adj[i] = mask

    all_mask = (1 << k) - 1

    def bipartite(mask):
        unvisited = mask
        side_a = 0
        side_b = 0

        while unvisited:
            seed = unvisited & -unvisited
            unvisited ^= seed
            side_a |= seed
            frontier = seed
            parity = 0

            while frontier:
                neighbors = 0
                x = frontier
                while x:
                    bit = x & -x
                    x ^= bit
                    neighbors |= local_adj[bit.bit_length() - 1]
                neighbors &= mask

                same_side = side_a if parity == 0 else side_b
                if neighbors & same_side:
                    return None

                nxt = neighbors & unvisited
                if not nxt:
                    break

                unvisited ^= nxt
                if parity == 0:
                    side_b |= nxt
                else:
                    side_a |= nxt

                frontier = nxt
                parity ^= 1

        return side_a, side_b

    initial = bipartite(all_mask)
    if initial is not None:
        a, b = initial
        colors = [0] * k
        for i in range(k):
            bit = 1 << i
            colors[i] = 0 if a & bit else 1
        return colors

    # Maximal independent sets in the original graph are maximal cliques
    # in its complement.
    complement_adj = [
        all_mask ^ (1 << i) ^ local_adj[i]
        for i in range(k)
    ]

    answer = None

    def bron_kerbosch(chosen, candidates, excluded):
        nonlocal answer

        if candidates == 0:
            if excluded != 0:
                return False

            remaining = all_mask ^ chosen
            result = bipartite(remaining)
            if result is None:
                return False

            a, b = result
            colors = [0] * k
            for i in range(k):
                bit = 1 << i
                if chosen & bit:
                    colors[i] = 0
                elif a & bit:
                    colors[i] = 1
                else:
                    colors[i] = 2
            answer = colors
            return True

        pivot_set = candidates | excluded
        pivot = -1
        best_count = -1
        x = pivot_set
        while x:
            bit = x & -x
            x ^= bit
            u = bit.bit_length() - 1
            count = (candidates & complement_adj[u]).bit_count()
            if count > best_count:
                best_count = count
                pivot = u

        if pivot == -1:
            branch_vertices = candidates
        else:
            branch_vertices = candidates & ~complement_adj[pivot] & all_mask

        while branch_vertices:
            bit = branch_vertices & -branch_vertices
            branch_vertices ^= bit
            v = bit.bit_length() - 1

            if bron_kerbosch(
                chosen | bit,
                candidates & complement_adj[v],
                excluded & complement_adj[v]
            ):
                return True

            candidates ^= bit
            excluded |= bit

        return False

    bron_kerbosch(0, all_mask, 0)
    return answer

block_colors = []
for block in blocks:
    colors = solve_block(block)
    if colors is None:
        print("NO")
        sys.exit()
    block_colors.append(colors)

# Build the block-cut forest and merge independently found colorings.
vertex_blocks = [[] for _ in range(n)]
for bi, block in enumerate(blocks):
    for v in block:
        vertex_blocks[v].append(bi)

final_colors = [-1] * n
visited_blocks = [False] * len(blocks)

for root in range(len(blocks)):
    if visited_blocks[root]:
        continue

    visited_blocks[root] = True
    for i, v in enumerate(blocks[root]):
        final_colors[v] = block_colors[root][i]

    queue = deque([root])

    while queue:
        bi = queue.popleft()

        for articulation in blocks[bi]:
            for nb in vertex_blocks[articulation]:
                if visited_blocks[nb]:
                    continue

                visited_blocks[nb] = True
                child_vertices = blocks[nb]
                child_colors = block_colors[nb]
                anchor_index = child_vertices.index(articulation)

                local_anchor = child_colors[anchor_index]
                global_anchor = final_colors[articulation]

                mapping = [-1, -1, -1]
                mapping[local_anchor] = global_anchor

                remaining_local = [c for c in range(3) if c != local_anchor]
                remaining_global = [c for c in range(3) if c != global_anchor]
                mapping[remaining_local[0]] = remaining_global[0]
                mapping[remaining_local[1]] = remaining_global[1]

                for i, v in enumerate(child_vertices):
                    mapped = mapping[child_colors[i]]
                    if final_colors[v] == -1:
                        final_colors[v] = mapped

                queue.append(nb)

# Isolated vertices belong to no block.
for i in range(n):
    if final_colors[i] == -1:
        final_colors[i] = 0

print("YES")
print(*(c + 1 for c in final_colors))