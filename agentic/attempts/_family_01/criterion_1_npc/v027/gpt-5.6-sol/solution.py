import sys
from collections import deque
from itertools import permutations

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]
adj = [0] * n
edges = []
p = 2

for _ in range(m):
    u = data[p] - 1
    v = data[p + 1] - 1
    p += 2
    if u == v:
        print("NO")
        sys.exit()
    if not ((adj[u] >> v) & 1):
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        edges.append((u, v))

# Find biconnected blocks. Different blocks can be colored independently,
# with color permutations used at articulation vertices.
disc = [-1] * n
low = [0] * n
timer = 0
edge_stack = []
blocks = []

def tarjan(u, parent):
    global timer
    disc[u] = low[u] = timer
    timer += 1

    neighbors = adj[u]
    while neighbors:
        vb = neighbors & -neighbors
        neighbors ^= vb
        v = vb.bit_length() - 1

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

def bipartite_coloring(mask):
    unseen = mask
    first = 0
    second = 0

    while unseen:
        start = unseen & -unseen
        unseen ^= start
        first |= start
        queue = [start.bit_length() - 1]

        while queue:
            u = queue.pop()
            ub = 1 << u
            neighbors = adj[u] & mask

            if first & ub:
                if neighbors & first:
                    return None
                new_vertices = neighbors & unseen
                second |= new_vertices
            else:
                if neighbors & second:
                    return None
                new_vertices = neighbors & unseen
                first |= new_vertices

            unseen ^= new_vertices
            while new_vertices:
                vb = new_vertices & -new_vertices
                new_vertices ^= vb
                queue.append(vb.bit_length() - 1)

    return first, second

def solve_block(mask):
    direct = bipartite_coloring(mask)
    if direct is not None:
        return direct[0], direct[1], 0

    complement_adj = [0] * n
    vertices = mask
    while vertices:
        vb = vertices & -vertices
        vertices ^= vb
        v = vb.bit_length() - 1
        complement_adj[v] = (mask ^ vb) & ~adj[v]

    result = None

    # Enumerate maximal independent sets as maximal cliques in the complement.
    # If the graph is 3-colorable, one color class can be extended to a
    # maximal independent set while the remaining graph stays bipartite.
    def bron_kerbosch(chosen, possible, excluded):
        nonlocal result

        if possible == 0:
            if excluded == 0:
                rest = mask ^ chosen
                coloring = bipartite_coloring(rest)
                if coloring is not None:
                    result = (coloring[0], coloring[1], chosen)
                    return True
            return False

        union = possible | excluded
        pivot = -1
        best_score = -1
        temp = union

        while temp:
            ub = temp & -temp
            temp ^= ub
            u = ub.bit_length() - 1
            score = (possible & complement_adj[u]).bit_count()
            if score > best_score:
                best_score = score
                pivot = u

        candidates = possible & ~complement_adj[pivot] & mask

        while candidates:
            vb = candidates & -candidates
            candidates ^= vb
            v = vb.bit_length() - 1

            if bron_kerbosch(
                chosen | vb,
                possible & complement_adj[v],
                excluded & complement_adj[v]
            ):
                return True

            possible ^= vb
            excluded |= vb

        return False

    bron_kerbosch(0, mask, 0)
    return result

# Isolated vertices do not occur in any block.
answer = [0] * n
vertex_blocks = [[] for _ in range(n)]

for i, mask in enumerate(blocks):
    temp = mask
    while temp:
        vb = temp & -temp
        temp ^= vb
        vertex_blocks[vb.bit_length() - 1].append(i)

done = [False] * len(blocks)

for start in range(len(blocks)):
    if done[start]:
        continue

    queue = deque([start])

    while queue:
        bi = queue.popleft()
        if done[bi]:
            continue

        mask = blocks[bi]
        local = solve_block(mask)
        if local is None:
            print("NO")
            sys.exit()

        local_colors = {}
        for color_index, color_mask in enumerate(local, 1):
            temp = color_mask
            while temp:
                vb = temp & -temp
                temp ^= vb
                local_colors[vb.bit_length() - 1] = color_index

        chosen_permutation = None
        for perm in permutations((1, 2, 3)):
            valid = True
            temp = mask
            while temp:
                vb = temp & -temp
                temp ^= vb
                v = vb.bit_length() - 1
                if answer[v] and perm[local_colors[v] - 1] != answer[v]:
                    valid = False
                    break
            if valid:
                chosen_permutation = perm
                break

        if chosen_permutation is None:
            print("NO")
            sys.exit()

        temp = mask
        while temp:
            vb = temp & -temp
            temp ^= vb
            v = vb.bit_length() - 1
            answer[v] = chosen_permutation[local_colors[v] - 1]

        done[bi] = True

        temp = mask
        while temp:
            vb = temp & -temp
            temp ^= vb
            v = vb.bit_length() - 1
            for other in vertex_blocks[v]:
                if not done[other]:
                    queue.append(other)

for i in range(n):
    if answer[i] == 0:
        answer[i] = 1

print("YES")
print(*answer)