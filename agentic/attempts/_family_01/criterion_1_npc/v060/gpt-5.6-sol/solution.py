import sys

sys.setrecursionlimit(1_000_000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]
old_adj = [0] * n
p = 2
for _ in range(m):
    u = data[p] - 1
    v = data[p + 1] - 1
    p += 2
    if u != v:
        old_adj[u] |= 1 << v
        old_adj[v] |= 1 << u

order = sorted(range(n), key=lambda x: old_adj[x].bit_count(), reverse=True)
pos = [0] * n
for i, v in enumerate(order):
    pos[v] = i

adj = [0] * n
for i, old_v in enumerate(order):
    mask = old_adj[old_v]
    new_mask = 0
    while mask:
        b = mask & -mask
        old_u = b.bit_length() - 1
        new_mask |= 1 << pos[old_u]
        mask ^= b
    adj[i] = new_mask

all_vertices = (1 << n) - 1

components = []
unseen = all_vertices
while unseen:
    root = unseen & -unseen
    comp = 0
    frontier = root
    unseen ^= root
    while frontier:
        b = frontier & -frontier
        frontier ^= b
        v = b.bit_length() - 1
        comp |= b
        new_vertices = adj[v] & unseen
        unseen ^= new_vertices
        frontier |= new_vertices
    components.append(comp)

answer = [0] * n


def dsatur_solve(component, limit=20000):
    color = [-1] * n
    color_masks = [0, 0, 0]
    nodes = 0
    solution = None

    def dfs(rem, used):
        nonlocal nodes, solution
        nodes += 1
        if nodes > limit:
            return -1
        if rem == 0:
            solution = color[:]
            return 1

        best_v = -1
        best_sat = -1
        best_deg = -1
        q = rem
        while q:
            b = q & -q
            q ^= b
            v = b.bit_length() - 1
            sat = 0
            for c in range(used):
                if adj[v] & color_masks[c]:
                    sat += 1
            deg = (adj[v] & rem).bit_count()
            if sat > best_sat or (sat == best_sat and deg > best_deg):
                best_sat = sat
                best_deg = deg
                best_v = v

        vb = 1 << best_v
        had_abort = False
        max_color = used + (1 if used < 3 else 0)

        for c in range(max_color):
            if adj[best_v] & color_masks[c]:
                continue
            color[best_v] = c
            color_masks[c] |= vb
            new_used = used + 1 if c == used else used
            status = dfs(rem ^ vb, new_used)
            color_masks[c] ^= vb
            color[best_v] = -1

            if status == 1:
                return 1
            if status == -1:
                had_abort = True

        return -1 if had_abort else 0

    status = dfs(component, 0)
    return status, solution


def bipartite(mask):
    side_a = 0
    side_b = 0
    colored = 0

    while colored != mask:
        root = (mask & ~colored) & -(mask & ~colored)
        side_a |= root
        colored |= root
        queue = root

        while queue:
            b = queue & -queue
            queue ^= b
            v = b.bit_length() - 1
            neighbors = adj[v] & mask

            if side_a & b:
                if neighbors & side_a:
                    return None
                new_nodes = neighbors & ~colored
                side_b |= new_nodes
            else:
                if neighbors & side_b:
                    return None
                new_nodes = neighbors & ~colored
                side_a |= new_nodes

            colored |= new_nodes
            queue |= new_nodes

    return side_a, side_b


def maximal_independent_solve(component):
    compatible = [0] * n
    for v in range(n):
        compatible[v] = component & ~(adj[v] | (1 << v))

    result = None

    def bron_kerbosch(chosen, candidates, excluded):
        nonlocal result

        if candidates == 0:
            if excluded == 0:
                rest = component ^ chosen
                parts = bipartite(rest)
                if parts is not None:
                    result = (chosen, parts[0], parts[1])
                    return True
            return False

        union = candidates | excluded
        pivot = -1
        best = -1
        q = union
        while q:
            b = q & -q
            q ^= b
            u = b.bit_length() - 1
            score = (candidates & compatible[u]).bit_count()
            if score > best:
                best = score
                pivot = u

        branch = candidates & ~compatible[pivot]

        while branch:
            vb = branch & -branch
            branch ^= vb
            v = vb.bit_length() - 1

            if bron_kerbosch(
                chosen | vb,
                candidates & compatible[v],
                excluded & compatible[v]
            ):
                return True

            candidates ^= vb
            excluded |= vb

        return False

    bron_kerbosch(0, component, 0)
    return result


for component in components:
    status, solution = dsatur_solve(component)

    if status == 0:
        print("NO")
        sys.exit()

    if status == 1:
        q = component
        while q:
            b = q & -q
            q ^= b
            v = b.bit_length() - 1
            answer[v] = solution[v] + 1
        continue

    result = maximal_independent_solve(component)
    if result is None:
        print("NO")
        sys.exit()

    first, second, third = result
    q = first
    while q:
        b = q & -q
        q ^= b
        answer[b.bit_length() - 1] = 1
    q = second
    while q:
        b = q & -q
        q ^= b
        answer[b.bit_length() - 1] = 2
    q = third
    while q:
        b = q & -q
        q ^= b
        answer[b.bit_length() - 1] = 3

old_answer = [0] * n
for new_v, old_v in enumerate(order):
    old_answer[old_v] = answer[new_v]

print("YES")
print(*old_answer)