import sys

sys.setrecursionlimit(1000000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]
adj = [0] * n

pos = 2
for _ in range(m):
    u = data[pos] - 1
    v = data[pos + 1] - 1
    pos += 2
    if u != v:
        adj[u] |= 1 << v
        adj[v] |= 1 << u

answer = [-1] * n


def bipartite(mask):
    side0 = 0
    side1 = 0
    unseen = mask

    while unseen:
        root = unseen & -unseen
        unseen ^= root
        side0 |= root
        queue = root

        while queue:
            vb = queue & -queue
            queue ^= vb
            v = vb.bit_length() - 1

            if side0 & vb:
                if adj[v] & side0:
                    return None
                new_vertices = adj[v] & unseen
                side1 |= new_vertices
            else:
                if adj[v] & side1:
                    return None
                new_vertices = adj[v] & unseen
                side0 |= new_vertices

            unseen &= ~new_vertices
            queue |= new_vertices

    return side0, side1


def greedy_three_color(component):
    colors = [-1] * n
    uncolored = component

    while uncolored:
        best_v = -1
        best_sat = -1
        best_degree = -1
        best_forbidden = 0

        bits = uncolored
        while bits:
            vb = bits & -bits
            bits ^= vb
            v = vb.bit_length() - 1

            forbidden = 0
            neighbors = adj[v] & component
            while neighbors:
                ub = neighbors & -neighbors
                neighbors ^= ub
                u = ub.bit_length() - 1
                c = colors[u]
                if c >= 0:
                    forbidden |= 1 << c

            saturation = forbidden.bit_count()
            degree = (adj[v] & uncolored).bit_count()

            if saturation > best_sat or (
                saturation == best_sat and degree > best_degree
            ):
                best_v = v
                best_sat = saturation
                best_degree = degree
                best_forbidden = forbidden

        chosen = -1
        for c in range(3):
            if not (best_forbidden >> c) & 1:
                chosen = c
                break

        if chosen == -1:
            return None

        colors[best_v] = chosen
        uncolored &= ~(1 << best_v)

    return colors


def solve_component(component):
    bp = bipartite(component)
    if bp is not None:
        a, b = bp
        bits = a
        while bits:
            vb = bits & -bits
            bits ^= vb
            answer[vb.bit_length() - 1] = 0
        bits = b
        while bits:
            vb = bits & -bits
            bits ^= vb
            answer[vb.bit_length() - 1] = 1
        return True

    greedy = greedy_three_color(component)
    if greedy is not None:
        bits = component
        while bits:
            vb = bits & -bits
            bits ^= vb
            v = vb.bit_length() - 1
            answer[v] = greedy[v]
        return True

    nonadj = [0] * n
    bits = component
    while bits:
        vb = bits & -bits
        bits ^= vb
        v = vb.bit_length() - 1
        nonadj[v] = component & ~adj[v] & ~vb

    found = None

    def search(selected, candidates, excluded):
        nonlocal found

        if candidates == 0:
            if excluded:
                return False
            remainder = component & ~selected
            partition = bipartite(remainder)
            if partition is None:
                return False
            found = (selected, partition[0], partition[1])
            return True

        forced_out = component & ~(selected | candidates)
        if forced_out.bit_count() >= 3 and bipartite(forced_out) is None:
            return False

        union = candidates | excluded
        pivot = -1
        pivot_score = -1
        temp = union
        while temp:
            ub = temp & -temp
            temp ^= ub
            u = ub.bit_length() - 1
            score = (candidates & nonadj[u]).bit_count()
            if score > pivot_score:
                pivot = u
                pivot_score = score

        if pivot == -1:
            branch = candidates
        else:
            branch = candidates & ~nonadj[pivot]

        while branch:
            vb = branch & -branch
            branch ^= vb
            v = vb.bit_length() - 1

            if search(
                selected | vb,
                candidates & nonadj[v],
                excluded & nonadj[v]
            ):
                return True

            candidates &= ~vb
            excluded |= vb

        return False

    if not search(0, component, 0):
        return False

    selected, a, b = found

    bits = selected
    while bits:
        vb = bits & -bits
        bits ^= vb
        answer[vb.bit_length() - 1] = 2

    bits = a
    while bits:
        vb = bits & -bits
        bits ^= vb
        answer[vb.bit_length() - 1] = 0

    bits = b
    while bits:
        vb = bits & -bits
        bits ^= vb
        answer[vb.bit_length() - 1] = 1

    return True


all_vertices = (1 << n) - 1
remaining = all_vertices
possible = True

while remaining and possible:
    root = remaining & -remaining
    component = 0
    frontier = root
    remaining ^= root

    while frontier:
        vb = frontier & -frontier
        frontier ^= vb
        v = vb.bit_length() - 1
        component |= vb

        new_vertices = adj[v] & remaining
        remaining &= ~new_vertices
        frontier |= new_vertices

    if not solve_component(component):
        possible = False

if not possible:
    print("NO")
else:
    print("YES")
    print(*[c + 1 for c in answer])