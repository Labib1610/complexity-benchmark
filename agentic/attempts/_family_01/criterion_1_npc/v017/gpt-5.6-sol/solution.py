import sys

sys.setrecursionlimit(10000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]
adj = [0] * n
graph = [[] for _ in range(n)]

p = 2
for _ in range(m):
    u = data[p] - 1
    v = data[p + 1] - 1
    p += 2
    if u == v or ((adj[u] >> v) & 1):
        continue
    adj[u] |= 1 << v
    adj[v] |= 1 << u
    graph[u].append(v)
    graph[v].append(u)

# Find vertex-biconnected blocks using an edge stack.
disc = [-1] * n
low = [0] * n
timer = 0
edge_stack = []
blocks = []

def tarjan(u, parent):
    global timer
    disc[u] = low[u] = timer
    timer += 1

    for v in graph[u]:
        if disc[v] == -1:
            edge_stack.append((u, v))
            tarjan(v, u)
            low[u] = min(low[u], low[v])

            if low[v] >= disc[u]:
                mask = 0
                while True:
                    a, b = edge_stack.pop()
                    mask |= (1 << a) | (1 << b)
                    if a == u and b == v:
                        break
                blocks.append(mask)
        elif v != parent and disc[v] < disc[u]:
            edge_stack.append((u, v))
            low[u] = min(low[u], disc[v])

for i in range(n):
    if disc[i] == -1:
        tarjan(i, -1)
        edge_stack.clear()

def bipartite(mask):
    left = 0
    right = 0
    unseen = mask

    while unseen:
        root = unseen & -unseen
        left |= root
        unseen ^= root
        queue = root

        while queue:
            bit = queue & -queue
            queue ^= bit
            v = bit.bit_length() - 1
            neighbors = adj[v] & mask

            if left & bit:
                if neighbors & left:
                    return None
                new_vertices = neighbors & ~(left | right)
                right |= new_vertices
            else:
                if neighbors & right:
                    return None
                new_vertices = neighbors & ~(left | right)
                left |= new_vertices

            unseen &= ~new_vertices
            queue |= new_vertices

    return left, right

def color_block(mask):
    simple = bipartite(mask)
    if simple is not None:
        return simple[0], simple[1], 0

    size = mask.bit_count()
    required = (size + 2) // 3

    comp_adj = [0] * n
    vertices = mask
    while vertices:
        bit = vertices & -vertices
        vertices ^= bit
        v = bit.bit_length() - 1
        comp_adj[v] = mask & ~(adj[v] | bit)

    def search(independent, independent_size, possible, excluded):
        if independent_size + possible.bit_count() < required:
            return None

        if possible == 0:
            if excluded != 0 or independent_size < required:
                return None
            rest = mask & ~independent
            result = bipartite(rest)
            if result is not None:
                return result[0], result[1], independent
            return None

        union = possible | excluded
        pivot = -1
        best = -1
        q = union
        while q:
            bit = q & -q
            q ^= bit
            v = bit.bit_length() - 1
            score = (possible & comp_adj[v]).bit_count()
            if score > best:
                best = score
                pivot = v

        candidates = possible if pivot == -1 else possible & ~comp_adj[pivot]

        while candidates:
            bit = candidates & -candidates
            candidates ^= bit
            v = bit.bit_length() - 1

            result = search(
                independent | bit,
                independent_size + 1,
                possible & comp_adj[v],
                excluded & comp_adj[v]
            )
            if result is not None:
                return result

            possible ^= bit
            excluded |= bit

            if independent_size + possible.bit_count() < required:
                break

        return None

    return search(0, 0, mask, 0)

block_solutions = [None] * len(blocks)

# Larger blocks are usually the most restrictive, so solve them first.
order = sorted(range(len(blocks)), key=lambda i: blocks[i].bit_count(), reverse=True)
for block_id in order:
    solution = color_block(blocks[block_id])
    if solution is None:
        print("NO")
        sys.exit()
    block_solutions[block_id] = solution

vertex_blocks = [[] for _ in range(n)]
for block_id, mask in enumerate(blocks):
    q = mask
    while q:
        bit = q & -q
        q ^= bit
        vertex_blocks[bit.bit_length() - 1].append(block_id)

answer = [0] * n
visited_blocks = [False] * len(blocks)

for root in range(len(blocks)):
    if visited_blocks[root]:
        continue

    visited_blocks[root] = True
    queue = [(root, -1)]
    head = 0

    while head < len(queue):
        block_id, shared_vertex = queue[head]
        head += 1

        mask = blocks[block_id]
        color1, color2, color3 = block_solutions[block_id]

        if shared_vertex == -1:
            mapping = [0, 1, 2, 3]
        else:
            bit = 1 << shared_vertex
            if color1 & bit:
                local_shared = 1
            elif color2 & bit:
                local_shared = 2
            else:
                local_shared = 3

            global_shared = answer[shared_vertex]
            mapping = [0, 0, 0, 0]
            mapping[local_shared] = global_shared

            local_remaining = [c for c in (1, 2, 3) if c != local_shared]
            global_remaining = [c for c in (1, 2, 3) if c != global_shared]
            mapping[local_remaining[0]] = global_remaining[0]
            mapping[local_remaining[1]] = global_remaining[1]

        q = mask
        while q:
            bit = q & -q
            q ^= bit
            v = bit.bit_length() - 1

            if color1 & bit:
                local_color = 1
            elif color2 & bit:
                local_color = 2
            else:
                local_color = 3

            mapped_color = mapping[local_color]
            if answer[v] == 0:
                answer[v] = mapped_color

            for next_block in vertex_blocks[v]:
                if not visited_blocks[next_block]:
                    visited_blocks[next_block] = True
                    queue.append((next_block, v))

for i in range(n):
    if answer[i] == 0:
        answer[i] = 1

print("YES")
print(*answer)