import sys

sys.setrecursionlimit(10000)


def solve_component(vertices, global_adj):
    vertices = sorted(vertices, key=lambda v: global_adj[v].bit_count(), reverse=True)
    k = len(vertices)
    index = {v: i for i, v in enumerate(vertices)}
    adj = [0] * k

    for i, v in enumerate(vertices):
        mask = global_adj[v]
        local = 0
        while mask:
            bit = mask & -mask
            u = bit.bit_length() - 1
            if u in index:
                local |= 1 << index[u]
            mask ^= bit
        adj[i] = local

    all_mask = (1 << k) - 1
    compatible = [all_mask ^ (1 << i) ^ adj[i] for i in range(k)]

    def bipartite(mask):
        side0 = 0
        side1 = 0
        unseen = mask

        while unseen:
            seed = unseen & -unseen
            unseen ^= seed
            side0 |= seed
            queue = seed

            while queue:
                bit = queue & -queue
                queue ^= bit
                v = bit.bit_length() - 1

                if side0 & bit:
                    if adj[v] & side0:
                        return None
                    new_vertices = adj[v] & unseen
                    unseen &= ~new_vertices
                    side1 |= new_vertices
                else:
                    if adj[v] & side1:
                        return None
                    new_vertices = adj[v] & unseen
                    unseen &= ~new_vertices
                    side0 |= new_vertices

                queue |= new_vertices

        return side0, side1

    initial = bipartite(all_mask)
    if initial is not None:
        a, b = initial
        colors = [0] * k
        for i in range(k):
            colors[i] = 2 if (a >> i) & 1 else 3
        return vertices, colors

    answer = None

    def dfs(selected, candidates, excluded):
        nonlocal answer

        fixed = all_mask & ~(selected | candidates)

        if fixed.bit_count() >= 3 and bipartite(fixed) is None:
            return False

        if candidates == 0:
            parts = bipartite(fixed)
            if parts is None:
                return False
            a, b = parts
            answer = (selected, a, b)
            return True

        union = candidates | excluded
        pivot = -1
        best = -1
        temp = union

        while temp:
            bit = temp & -temp
            temp ^= bit
            u = bit.bit_length() - 1
            score = (candidates & compatible[u]).bit_count()
            if score > best:
                best = score
                pivot = u

        branch = candidates if pivot < 0 else candidates & ~compatible[pivot]

        while branch:
            bit = branch & -branch
            branch ^= bit
            v = bit.bit_length() - 1

            if dfs(
                selected | bit,
                candidates & compatible[v],
                excluded & compatible[v]
            ):
                return True

            candidates ^= bit
            excluded |= bit

        return False

    if not dfs(0, all_mask, 0):
        return None

    selected, a, b = answer
    colors = [0] * k
    for i in range(k):
        bit = 1 << i
        if selected & bit:
            colors[i] = 1
        elif a & bit:
            colors[i] = 2
        else:
            colors[i] = 3

    return vertices, colors


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    global_adj = [0] * n

    pos = 2
    for _ in range(m):
        u = data[pos] - 1
        v = data[pos + 1] - 1
        pos += 2
        if u != v:
            global_adj[u] |= 1 << v
            global_adj[v] |= 1 << u

    unseen = (1 << n) - 1
    components = []

    while unseen:
        seed = unseen & -unseen
        unseen ^= seed
        stack = seed
        component_mask = 0

        while stack:
            bit = stack & -stack
            stack ^= bit
            v = bit.bit_length() - 1
            component_mask |= bit

            new_vertices = global_adj[v] & unseen
            unseen &= ~new_vertices
            stack |= new_vertices

        vertices = []
        mask = component_mask
        while mask:
            bit = mask & -mask
            mask ^= bit
            vertices.append(bit.bit_length() - 1)
        components.append(vertices)

    result = [0] * n

    for component in components:
        solved = solve_component(component, global_adj)
        if solved is None:
            print("NO")
            return

        vertices, colors = solved
        for v, color in zip(vertices, colors):
            result[v] = color

    print("YES")
    print(*result)


if __name__ == "__main__":
    main()