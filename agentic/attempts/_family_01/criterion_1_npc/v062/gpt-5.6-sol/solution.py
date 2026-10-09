import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

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

    degree = [x.bit_count() for x in adj]
    alive = [True] * n
    q = deque(i for i in range(n) if degree[i] <= 2)
    removed = []

    while q:
        v = q.popleft()
        if not alive[v] or degree[v] > 2:
            continue
        alive[v] = False
        removed.append(v)

        mask = adj[v]
        while mask:
            bit = mask & -mask
            u = bit.bit_length() - 1
            mask -= bit
            if alive[u]:
                degree[u] -= 1
                if degree[u] <= 2:
                    q.append(u)

    core_mask = 0
    for v in range(n):
        if alive[v]:
            core_mask |= 1 << v

    components = []
    unseen = core_mask
    while unseen:
        start_bit = unseen & -unseen
        unseen ^= start_bit
        comp_mask = start_bit
        frontier = start_bit

        while frontier:
            bit = frontier & -frontier
            frontier -= bit
            v = bit.bit_length() - 1
            nxt = adj[v] & unseen
            unseen ^= nxt
            frontier |= nxt
            comp_mask |= nxt

        components.append(comp_mask)

    answer = [0] * n

    def solve_component(comp_mask):
        vertices = []
        mask = comp_mask
        while mask:
            bit = mask & -mask
            vertices.append(bit.bit_length() - 1)
            mask -= bit

        dom = [7] * n
        static_degree = [(adj[v] & comp_mask).bit_count() for v in range(n)]

        anchor = max(vertices, key=lambda x: static_degree[x])
        neighbor_mask = adj[anchor] & comp_mask
        if not neighbor_mask:
            dom[anchor] = 1
            return dom

        neighbor = max(
            (i for i in vertices if (neighbor_mask >> i) & 1),
            key=lambda x: static_degree[x]
        )

        dom[anchor] = 1
        dom[neighbor] = 2
        trail = []

        def propagate(queue):
            head = 0
            while head < len(queue):
                v = queue[head]
                head += 1
                color_bit = dom[v]

                mask2 = adj[v] & comp_mask
                while mask2:
                    b = mask2 & -mask2
                    u = b.bit_length() - 1
                    mask2 -= b

                    old = dom[u]
                    if old & color_bit:
                        new = old & ~color_bit
                        if new == old:
                            continue
                        trail.append((u, old))
                        dom[u] = new
                        if new == 0:
                            return False
                        if new & (new - 1) == 0:
                            queue.append(u)
            return True

        if not propagate([anchor, neighbor]):
            return None

        failed = set()

        def encode_state():
            key = 0
            shift = 0
            for v in vertices:
                key |= dom[v] << shift
                shift += 3
            return key

        def dfs():
            chosen = -1
            best_size = 4
            best_dynamic = -1
            best_static = -1
            unresolved_mask = 0

            for v in vertices:
                if dom[v] & (dom[v] - 1):
                    unresolved_mask |= 1 << v

            if unresolved_mask == 0:
                return True

            for v in vertices:
                size = dom[v].bit_count()
                if size <= 1:
                    continue
                dynamic_degree = (adj[v] & unresolved_mask).bit_count()
                sd = static_degree[v]
                if (size < best_size or
                    (size == best_size and dynamic_degree > best_dynamic) or
                    (size == best_size and dynamic_degree == best_dynamic and sd > best_static)):
                    chosen = v
                    best_size = size
                    best_dynamic = dynamic_degree
                    best_static = sd

            state = encode_state()
            if state in failed:
                return False

            options = []
            bits = dom[chosen]
            while bits:
                color_bit = bits & -bits
                bits -= color_bit
                impact = 0
                neighbors = adj[chosen] & unresolved_mask
                while neighbors:
                    b = neighbors & -neighbors
                    u = b.bit_length() - 1
                    neighbors -= b
                    if dom[u] & color_bit:
                        impact += 1
                options.append((impact, color_bit))
            options.sort()

            for _, color_bit in options:
                mark = len(trail)
                old = dom[chosen]
                trail.append((chosen, old))
                dom[chosen] = color_bit

                if propagate([chosen]) and dfs():
                    return True

                while len(trail) > mark:
                    u, old_domain = trail.pop()
                    dom[u] = old_domain

            if len(failed) >= 300000:
                failed.clear()
            failed.add(state)
            return False

        if dfs():
            return dom
        return None

    for comp_mask in components:
        result = solve_component(comp_mask)
        if result is None:
            print("NO")
            return

        mask = comp_mask
        while mask:
            bit = mask & -mask
            v = bit.bit_length() - 1
            mask -= bit
            answer[v] = result[v].bit_length()

    for v in reversed(removed):
        used = 0
        mask = adj[v]
        while mask:
            bit = mask & -mask
            u = bit.bit_length() - 1
            mask -= bit
            if answer[u]:
                used |= 1 << (answer[u] - 1)

        for color in range(1, 4):
            if not (used & (1 << (color - 1))):
                answer[v] = color
                break

    print("YES")
    print(*answer)

if __name__ == "__main__":
    main()