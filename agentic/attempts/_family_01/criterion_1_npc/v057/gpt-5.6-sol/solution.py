import sys
from itertools import permutations

sys.setrecursionlimit(1_000_000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

it = iter(data)
n = next(it)
m = next(it)

adj = [0] * n
neighbors = [[] for _ in range(n)]

for _ in range(m):
    u = next(it) - 1
    v = next(it) - 1
    if u == v:
        print("NO")
        sys.exit()
    if not ((adj[u] >> v) & 1):
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        neighbors[u].append(v)
        neighbors[v].append(u)

# Decompose the graph into vertex-biconnected blocks.
disc = [-1] * n
low = [0] * n
timer = 0
edge_stack = []
blocks = []

def tarjan(u, parent):
    global timer
    disc[u] = low[u] = timer
    timer += 1

    for v in neighbors[u]:
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

for start in range(n):
    if disc[start] == -1:
        tarjan(start, -1)

def bipartition(mask):
    side0 = 0
    side1 = 0
    uncolored = mask

    while uncolored:
        seed = uncolored & -uncolored
        uncolored ^= seed
        side0 |= seed
        queue = seed

        while queue:
            bit = queue & -queue
            queue ^= bit
            v = bit.bit_length() - 1
            nei = adj[v] & mask

            if side0 & bit:
                if nei & side0:
                    return None
                new_vertices = nei & uncolored
                side1 |= new_vertices
            else:
                if nei & side1:
                    return None
                new_vertices = nei & uncolored
                side0 |= new_vertices

            uncolored &= ~new_vertices
            queue |= new_vertices

    return side0, side1

def contains_k4(mask):
    vertices = mask
    while vertices:
        ub = vertices & -vertices
        vertices ^= ub
        u = ub.bit_length() - 1
        vs = adj[u] & vertices

        while vs:
            vb = vs & -vs
            vs ^= vb
            v = vb.bit_length() - 1
            common = adj[u] & adj[v] & mask
            xs = common

            while xs:
                xb = xs & -xs
                xs ^= xb
                x = xb.bit_length() - 1
                if adj[x] & common & ~xb:
                    return True
    return False

def color_block(mask):
    initial = bipartition(mask)
    if initial is not None:
        a, b = initial
        colors = {}
        x = a
        while x:
            bit = x & -x
            x ^= bit
            colors[bit.bit_length() - 1] = 1
        x = b
        while x:
            bit = x & -x
            x ^= bit
            colors[bit.bit_length() - 1] = 2
        return colors

    if contains_k4(mask):
        return None

    complement_adj = [0] * n
    vertices = mask
    while vertices:
        bit = vertices & -vertices
        vertices ^= bit
        v = bit.bit_length() - 1
        complement_adj[v] = mask & ~(adj[v] | bit)

    solution = None

    def bron_kerbosch(chosen, candidates, excluded):
        nonlocal solution
        if solution is not None:
            return

        if candidates == 0:
            if excluded == 0:
                remaining = mask & ~chosen
                parts = bipartition(remaining)
                if parts is not None:
                    solution = (chosen, parts[0], parts[1])
            return

        union = candidates | excluded
        pivot = -1
        best = -1
        temp = union

        while temp:
            bit = temp & -temp
            temp ^= bit
            v = bit.bit_length() - 1
            score = (candidates & complement_adj[v]).bit_count()
            if score > best:
                best = score
                pivot = v

        branch = candidates if pivot == -1 else candidates & ~complement_adj[pivot]

        while branch and solution is None:
            bit = branch & -branch
            branch ^= bit
            v = bit.bit_length() - 1

            bron_kerbosch(
                chosen | bit,
                candidates & complement_adj[v],
                excluded & complement_adj[v]
            )

            candidates ^= bit
            excluded |= bit

    bron_kerbosch(0, mask, 0)

    if solution is None:
        return None

    chosen, a, b = solution
    colors = {}

    x = a
    while x:
        bit = x & -x
        x ^= bit
        colors[bit.bit_length() - 1] = 1

    x = b
    while x:
        bit = x & -x
        x ^= bit
        colors[bit.bit_length() - 1] = 2

    x = chosen
    while x:
        bit = x & -x
        x ^= bit
        colors[bit.bit_length() - 1] = 3

    return colors

local_colors = []
for block in blocks:
    coloring = color_block(block)
    if coloring is None:
        print("NO")
        sys.exit()
    local_colors.append(coloring)

vertex_blocks = [[] for _ in range(n)]
for i, mask in enumerate(blocks):
    x = mask
    while x:
        bit = x & -x
        x ^= bit
        vertex_blocks[bit.bit_length() - 1].append(i)

answer = [0] * n
visited_blocks = [False] * len(blocks)
all_permutations = list(permutations((1, 2, 3)))

def merge_block(block_index):
    visited_blocks[block_index] = True
    local = local_colors[block_index]
    mask = blocks[block_index]

    selected = None
    for perm in all_permutations:
        valid = True
        x = mask
        while x:
            bit = x & -x
            x ^= bit
            v = bit.bit_length() - 1
            if answer[v] and perm[local[v] - 1] != answer[v]:
                valid = False
                break
        if valid:
            selected = perm
            break

    if selected is None:
        return False

    x = mask
    while x:
        bit = x & -x
        x ^= bit
        v = bit.bit_length() - 1
        answer[v] = selected[local[v] - 1]

    x = mask
    while x:
        bit = x & -x
        x ^= bit
        v = bit.bit_length() - 1
        for nxt in vertex_blocks[v]:
            if not visited_blocks[nxt]:
                if not merge_block(nxt):
                    return False
    return True

for i in range(len(blocks)):
    if not visited_blocks[i]:
        if not merge_block(i):
            print("NO")
            sys.exit()

for i in range(n):
    if answer[i] == 0:
        answer[i] = 1

print("YES")
print(*answer)