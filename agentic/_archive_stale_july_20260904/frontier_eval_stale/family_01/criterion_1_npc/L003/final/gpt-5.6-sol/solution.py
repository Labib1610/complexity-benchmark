import sys

sys.setrecursionlimit(1_000_000)


def solve_component(vertices, global_adj):
    k = len(vertices)
    if k == 1:
        return [1]

    index = {v: i for i, v in enumerate(vertices)}
    adj = [0] * k

    for i, v in enumerate(vertices):
        mask = global_adj[v]
        local_mask = 0
        while mask:
            bit = mask & -mask
            u = bit.bit_length() - 1
            j = index.get(u)
            if j is not None:
                local_mask |= 1 << j
            mask ^= bit
        adj[i] = local_mask

    all_mask = (1 << k) - 1
    suffix = [0] * (k + 1)
    for i in range(k - 1, -1, -1):
        suffix[i] = suffix[i + 1] | (1 << i)

    def bipartite_coloring(independent):
        remaining = all_mask ^ independent
        color_a = 0
        color_b = 0
        colored = 0

        while True:
            uncolored = remaining & ~colored
            if not uncolored:
                return color_a, color_b

            root_bit = uncolored & -uncolored
            root = root_bit.bit_length() - 1
            color_a |= root_bit
            colored |= root_bit
            stack = [root]

            while stack:
                v = stack.pop()
                neighbors = adj[v] & remaining

                if (color_a >> v) & 1:
                    if neighbors & color_a:
                        return None
                    new_vertices = neighbors & ~colored
                    color_b |= new_vertices
                else:
                    if neighbors & color_b:
                        return None
                    new_vertices = neighbors & ~colored
                    color_a |= new_vertices

                colored |= new_vertices
                while new_vertices:
                    bit = new_vertices & -new_vertices
                    stack.append(bit.bit_length() - 1)
                    new_vertices ^= bit

    def dfs(i, chosen, blocked, need):
        while i < k and ((blocked >> i) & 1):
            i += 1

        if i == k:
            if need:
                return None
            coloring = bipartite_coloring(chosen)
            if coloring is None:
                return None
            return chosen, coloring[0], coloring[1]

        available = suffix[i] & ~blocked
        pending = need
        while pending:
            bit = pending & -pending
            v = bit.bit_length() - 1
            if not (adj[v] & available):
                return None
            pending ^= bit

        bit = 1 << i

        result = dfs(
            i + 1,
            chosen | bit,
            blocked | adj[i],
            need & ~adj[i]
        )
        if result is not None:
            return result

        return dfs(
            i + 1,
            chosen,
            blocked,
            need | bit
        )

    result = dfs(0, 0, 0, 0)
    if result is None:
        return None

    chosen, color_a, color_b = result
    colors = [0] * k
    for i in range(k):
        bit = 1 << i
        if chosen & bit:
            colors[i] = 1
        elif color_a & bit:
            colors[i] = 2
        else:
            colors[i] = 3
    return colors


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    adj = [0] * n
    pos = 2

    for _ in range(m):
        u = data[pos] - 1
        v = data[pos + 1] - 1
        pos += 2
        if u == v:
            print("NO")
            return
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    unseen = (1 << n) - 1
    components = []

    while unseen:
        root_bit = unseen & -unseen
        unseen ^= root_bit
        component_mask = root_bit
        frontier = root_bit

        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            v = bit.bit_length() - 1
            new_vertices = adj[v] & unseen
            unseen ^= new_vertices
            component_mask |= new_vertices
            frontier |= new_vertices

        vertices = []
        while component_mask:
            bit = component_mask & -component_mask
            vertices.append(bit.bit_length() - 1)
            component_mask ^= bit
        components.append(vertices)

    answer = [0] * n

    for vertices in components:
        colors = solve_component(vertices, adj)
        if colors is None:
            print("NO")
            return
        for v, color in zip(vertices, colors):
            answer[v] = color

    print("YES")
    print(*answer)


if __name__ == "__main__":
    main()