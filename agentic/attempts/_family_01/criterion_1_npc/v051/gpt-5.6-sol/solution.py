import sys

sys.setrecursionlimit(1_000_000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]
adj = [0] * n
invalid = False

p = 2
for _ in range(m):
    u = data[p] - 1
    v = data[p + 1] - 1
    p += 2
    if u == v:
        invalid = True
    else:
        adj[u] |= 1 << v
        adj[v] |= 1 << u

if invalid:
    print("NO")
    sys.exit()

all_mask = (1 << n) - 1


def greedy_coloring():
    colors = [0] * n
    remaining = all_mask

    while remaining:
        best_v = -1
        best_sat = -1
        best_deg = -1

        q = remaining
        while q:
            bit = q & -q
            q ^= bit
            v = bit.bit_length() - 1

            used = 0
            neighbors = adj[v]
            while neighbors:
                nb = neighbors & -neighbors
                neighbors ^= nb
                c = colors[nb.bit_length() - 1]
                if c:
                    used |= 1 << (c - 1)

            sat = used.bit_count()
            deg = (adj[v] & remaining).bit_count()
            if sat > best_sat or (sat == best_sat and deg > best_deg):
                best_sat = sat
                best_deg = deg
                best_v = v

        used = 0
        neighbors = adj[best_v]
        while neighbors:
            nb = neighbors & -neighbors
            neighbors ^= nb
            c = colors[nb.bit_length() - 1]
            if c:
                used |= 1 << (c - 1)

        chosen = 0
        for c in range(1, 4):
            if not (used & (1 << (c - 1))):
                chosen = c
                break

        if chosen == 0:
            return None

        colors[best_v] = chosen
        remaining ^= 1 << best_v

    return colors


greedy = greedy_coloring()
if greedy is not None:
    print("YES")
    print(*greedy)
    sys.exit()


def bipartite(mask):
    remaining = mask
    side0 = 0
    side1 = 0

    while remaining:
        root = remaining & -remaining
        remaining ^= root
        side0 |= root
        stack = [root]

        while stack:
            bit = stack.pop()
            v = bit.bit_length() - 1
            neighbors = adj[v] & mask

            if side0 & bit:
                if neighbors & side0:
                    return None
                new_vertices = neighbors & remaining
                side1 |= new_vertices
            else:
                if neighbors & side1:
                    return None
                new_vertices = neighbors & remaining
                side0 |= new_vertices

            remaining &= ~new_vertices
            while new_vertices:
                nb = new_vertices & -new_vertices
                new_vertices ^= nb
                stack.append(nb)

    return side0, side1


colors = [0] * n
unseen = all_mask
components = []

while unseen:
    start = unseen & -unseen
    unseen ^= start
    component = start
    stack = [start]

    while stack:
        bit = stack.pop()
        v = bit.bit_length() - 1
        new_vertices = adj[v] & unseen
        unseen &= ~new_vertices
        component |= new_vertices

        while new_vertices:
            nb = new_vertices & -new_vertices
            new_vertices ^= nb
            stack.append(nb)

    components.append(component)


def color_component(component):
    direct = bipartite(component)
    if direct is not None:
        a, b = direct
        return a, b, 0

    q = component
    root = -1
    root_degree = -1
    while q:
        bit = q & -q
        q ^= bit
        v = bit.bit_length() - 1
        degree = (adj[v] & component).bit_count()
        if degree > root_degree:
            root_degree = degree
            root = v

    root_bit = 1 << root
    nonadj = [0] * n
    q = component
    while q:
        bit = q & -q
        q ^= bit
        v = bit.bit_length() - 1
        nonadj[v] = component & ~(adj[v] | bit)

    initial_remaining = component & ~root_bit
    direct = bipartite(initial_remaining)
    if direct is not None:
        return direct[0], direct[1], root_bit

    initial_p = nonadj[root]
    answer = None

    def bron_kerbosch(independent, candidates, excluded):
        nonlocal answer

        if not candidates and not excluded:
            result = bipartite(component & ~independent)
            if result is not None:
                answer = (result[0], result[1], independent)
                return True
            return False

        union = candidates | excluded
        pivot = -1
        best_count = -1
        q2 = union
        while q2:
            bit = q2 & -q2
            q2 ^= bit
            v = bit.bit_length() - 1
            count = (candidates & nonadj[v]).bit_count()
            if count > best_count:
                best_count = count
                pivot = v

        if pivot == -1:
            choices = candidates
        else:
            choices = candidates & ~nonadj[pivot]

        while choices:
            bit = choices & -choices
            choices ^= bit
            v = bit.bit_length() - 1

            if bron_kerbosch(
                independent | bit,
                candidates & nonadj[v],
                excluded & nonadj[v]
            ):
                return True

            candidates &= ~bit
            excluded |= bit

        return False

    bron_kerbosch(root_bit, initial_p, 0)
    return answer


for component in components:
    result = color_component(component)
    if result is None:
        print("NO")
        sys.exit()

    side0, side1, side2 = result

    q = side0
    while q:
        bit = q & -q
        q ^= bit
        colors[bit.bit_length() - 1] = 1

    q = side1
    while q:
        bit = q & -q
        q ^= bit
        colors[bit.bit_length() - 1] = 2

    q = side2
    while q:
        bit = q & -q
        q ^= bit
        colors[bit.bit_length() - 1] = 3

print("YES")
print(*colors)