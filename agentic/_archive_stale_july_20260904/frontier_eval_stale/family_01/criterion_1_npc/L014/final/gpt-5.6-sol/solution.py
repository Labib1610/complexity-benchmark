import sys

sys.setrecursionlimit(10000)


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

    full = (1 << k) - 1
    comp_adj = [full & ~(adj[i] | (1 << i)) for i in range(k)]

    def is_bipartite(rem):
        side_a = 0
        side_b = 0
        colored = 0

        while colored != rem:
            root = (rem & ~colored) & -(rem & ~colored)
            side_a |= root
            colored |= root
            queue = root

            while queue:
                bit = queue & -queue
                queue ^= bit
                v = bit.bit_length() - 1
                neighbors = adj[v] & rem

                if side_a & bit:
                    if neighbors & side_a:
                        return False
                    new_bits = neighbors & ~colored
                    side_b |= new_bits
                else:
                    if neighbors & side_b:
                        return False
                    new_bits = neighbors & ~colored
                    side_a |= new_bits

                colored |= new_bits
                queue |= new_bits

        return True

    def lex_better(mask, other):
        if other is None:
            return True
        diff = mask ^ other
        if diff == 0:
            return False
        first = diff & -diff
        return bool(mask & first)

    def can_beat(optimistic, best):
        if best is None:
            return True
        diff = optimistic ^ best
        if diff == 0:
            return False
        first = diff & -diff
        return bool(optimistic & first)

    def greedy_extend(independent):
        result = independent
        for i in range(k):
            bit = 1 << i
            if not (result & bit) and not (adj[i] & result):
                result |= bit
        return result

    best = None

    def bron_kerbosch(r, p, x):
        nonlocal best

        if not can_beat(r | p, best):
            return

        if is_bipartite(full ^ r):
            candidate = greedy_extend(r)
            if lex_better(candidate, best):
                best = candidate
            return

        union = p | x
        if not union:
            return

        pivot = -1
        pivot_score = -1
        temp = union
        while temp:
            bit = temp & -temp
            temp ^= bit
            u = bit.bit_length() - 1
            score = (p & comp_adj[u]).bit_count()
            if score > pivot_score:
                pivot_score = score
                pivot = u

        candidates = p & ~comp_adj[pivot]

        while candidates:
            bit = candidates & -candidates
            candidates ^= bit
            v = bit.bit_length() - 1

            bron_kerbosch(
                r | bit,
                p & comp_adj[v],
                x & comp_adj[v]
            )

            p ^= bit
            x |= bit

            if not can_beat(r | p, best):
                break

    bron_kerbosch(0, full, 0)

    if best is None:
        return None

    colors = [1] * k
    rem = full ^ best
    side_a = 0
    side_b = 0
    colored = 0

    while colored != rem:
        root = (rem & ~colored) & -(rem & ~colored)
        side_a |= root
        colored |= root
        queue = root

        while queue:
            bit = queue & -queue
            queue ^= bit
            v = bit.bit_length() - 1
            neighbors = adj[v] & rem
            new_bits = neighbors & ~colored

            if side_a & bit:
                side_b |= new_bits
            else:
                side_a |= new_bits

            colored |= new_bits
            queue |= new_bits

    for i in range(k):
        bit = 1 << i
        if side_a & bit:
            colors[i] = 2
        elif side_b & bit:
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
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    answer = [0] * n
    unseen = (1 << n) - 1

    while unseen:
        start_bit = unseen & -unseen
        unseen ^= start_bit
        component_mask = start_bit
        queue = start_bit

        while queue:
            bit = queue & -queue
            queue ^= bit
            v = bit.bit_length() - 1
            new_bits = adj[v] & unseen
            unseen ^= new_bits
            component_mask |= new_bits
            queue |= new_bits

        vertices = []
        temp = component_mask
        while temp:
            bit = temp & -temp
            temp ^= bit
            vertices.append(bit.bit_length() - 1)

        component_colors = solve_component(vertices, adj)
        if component_colors is None:
            print("NO")
            return

        for v, color in zip(vertices, component_colors):
            answer[v] = color

    print("YES")
    print(*answer)


if __name__ == "__main__":
    main()