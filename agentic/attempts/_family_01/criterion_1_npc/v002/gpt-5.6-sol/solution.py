import sys

sys.setrecursionlimit(100000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]
adj = [0] * n

p = 2
for _ in range(m):
    u = data[p] - 1
    v = data[p + 1] - 1
    p += 2
    if u != v:
        adj[u] |= 1 << v
        adj[v] |= 1 << u

def bipartite(mask):
    side0 = 0
    side1 = 0
    uncolored = mask

    while uncolored:
        start = uncolored & -uncolored
        side0 |= start
        uncolored ^= start
        queue = start

        while queue:
            b = queue & -queue
            queue ^= b
            v = b.bit_length() - 1
            neighbors = adj[v] & mask

            if side0 & b:
                if neighbors & side0:
                    return None
                new_vertices = neighbors & uncolored
                side1 |= new_vertices
            else:
                if neighbors & side1:
                    return None
                new_vertices = neighbors & uncolored
                side0 |= new_vertices

            uncolored &= ~new_vertices
            queue |= new_vertices

    return side0, side1

def solve_component(vertices):
    initial_bipartition = bipartite(vertices)
    if initial_bipartition is not None:
        a, b = initial_bipartition
        return 0, a, b

    complement_neighbors = [0] * n
    bits = vertices
    while bits:
        b = bits & -bits
        bits ^= b
        v = b.bit_length() - 1
        complement_neighbors[v] = vertices & ~(adj[v] | b)

    answer = None

    def search(independent, candidates, excluded):
        nonlocal answer

        fixed_outside = vertices & ~(independent | candidates)
        fixed_parts = bipartite(fixed_outside)
        if fixed_parts is None:
            return False

        if candidates == 0:
            if excluded == 0:
                answer = (independent, fixed_parts[0], fixed_parts[1])
                return True
            return False

        union = candidates | excluded
        pivot = -1
        best = -1
        temp = union
        while temp:
            b = temp & -temp
            temp ^= b
            v = b.bit_length() - 1
            score = (candidates & complement_neighbors[v]).bit_count()
            if score > best:
                best = score
                pivot = v

        branch_vertices = candidates & ~complement_neighbors[pivot]

        while branch_vertices:
            b = branch_vertices & -branch_vertices
            branch_vertices ^= b
            v = b.bit_length() - 1

            if search(
                independent | b,
                candidates & complement_neighbors[v],
                excluded & complement_neighbors[v]
            ):
                return True

            candidates ^= b
            excluded |= b

        return False

    if search(0, vertices, 0):
        return answer
    return None

all_vertices = (1 << n) - 1
remaining = all_vertices
components = []

while remaining:
    start = remaining & -remaining
    remaining ^= start
    component = start
    queue = start

    while queue:
        b = queue & -queue
        queue ^= b
        v = b.bit_length() - 1
        new_vertices = adj[v] & remaining
        remaining &= ~new_vertices
        component |= new_vertices
        queue |= new_vertices

    components.append(component)

colors = [0] * n

for component in components:
    result = solve_component(component)
    if result is None:
        print("NO")
        sys.exit()

    silo1, silo2, silo3 = result

    bits = silo1
    while bits:
        b = bits & -bits
        bits ^= b
        colors[b.bit_length() - 1] = 1

    bits = silo2
    while bits:
        b = bits & -bits
        bits ^= b
        colors[b.bit_length() - 1] = 2

    bits = silo3
    while bits:
        b = bits & -bits
        bits ^= b
        colors[b.bit_length() - 1] = 3

print("YES")
print(*colors)