import sys

def solve_component(vertices, global_adj):
    k = len(vertices)
    index = {v: i for i, v in enumerate(vertices)}
    adj = [0] * k

    for i, v in enumerate(vertices):
        mask = global_adj[v]
        local_mask = 0
        while mask:
            bit = mask & -mask
            u = bit.bit_length() - 1
            if u in index:
                local_mask |= 1 << index[u]
            mask ^= bit
        adj[i] = local_mask

    # Bipartite components need only two colors.
    bip_color = [-1] * k
    bipartite = True
    for start in range(k):
        if bip_color[start] != -1:
            continue
        bip_color[start] = 0
        stack = [start]
        while stack and bipartite:
            v = stack.pop()
            mask = adj[v]
            while mask:
                bit = mask & -mask
                u = bit.bit_length() - 1
                mask ^= bit
                if bip_color[u] == -1:
                    bip_color[u] = bip_color[v] ^ 1
                    stack.append(u)
                elif bip_color[u] == bip_color[v]:
                    bipartite = False
                    break
        if not bipartite:
            break

    if bipartite:
        return bip_color

    colors = [-1] * k
    available = [7] * k
    usage = [0, 0, 0]
    color_masks = [0, 0, 0]
    uncolored = (1 << k) - 1

    assigned_log = []
    changed_log = []
    failed = set()
    cache_limit = 500000

    def rollback(a_len, c_len):
        nonlocal uncolored
        while len(changed_log) > c_len:
            v, old = changed_log.pop()
            available[v] = old
        while len(assigned_log) > a_len:
            v, c = assigned_log.pop()
            colors[v] = -1
            usage[c] -= 1
            color_masks[c] ^= 1 << v
            uncolored |= 1 << v

    def apply_color(start, initial_color):
        nonlocal uncolored
        queue = [(start, initial_color)]
        qpos = 0

        while qpos < len(queue):
            v, requested = queue[qpos]
            qpos += 1

            if colors[v] != -1:
                if colors[v] != requested:
                    return False
                continue

            if not (available[v] & (1 << requested)):
                return False

            colors[v] = requested
            usage[requested] += 1
            color_masks[requested] |= 1 << v
            uncolored &= ~(1 << v)
            assigned_log.append((v, requested))

            mask = adj[v] & uncolored
            remove_bit = 1 << requested
            while mask:
                bit = mask & -mask
                u = bit.bit_length() - 1
                mask ^= bit

                old = available[u]
                new = old & ~remove_bit
                if new == old:
                    continue

                changed_log.append((u, old))
                available[u] = new

                if new == 0:
                    return False
                if new & (new - 1) == 0:
                    queue.append((u, new.bit_length() - 1))

        return True

    def low_degree_solve():
        start_a = len(assigned_log)
        start_c = len(changed_log)
        remaining = uncolored
        plans = []

        while remaining:
            seed_bit = remaining & -remaining
            seed = seed_bit.bit_length() - 1

            comp = 0
            frontier = seed_bit
            remaining ^= seed_bit
            while frontier:
                bit = frontier & -frontier
                frontier ^= bit
                v = bit.bit_length() - 1
                comp |= bit
                nxt = adj[v] & remaining
                remaining ^= nxt
                frontier |= nxt

            size = comp.bit_count()
            endpoint = -1
            tmp = comp
            while tmp:
                bit = tmp & -tmp
                v = bit.bit_length() - 1
                tmp ^= bit
                if (adj[v] & comp).bit_count() <= 1:
                    endpoint = v
                    break

            is_cycle = endpoint == -1 and size >= 3
            current = endpoint if endpoint != -1 else (comp & -comp).bit_length() - 1

            order = []
            visited = 0
            prev = -1
            while True:
                order.append(current)
                visited |= 1 << current
                candidates = adj[current] & comp & ~visited
                if prev != -1:
                    candidates &= ~(1 << prev)
                if not candidates:
                    break
                nxt = (candidates & -candidates).bit_length() - 1
                prev, current = current, nxt

            if len(order) != size:
                rollback(start_a, start_c)
                return False

            chosen_plan = None
            first_options = available[order[0]]

            for first_color in range(3):
                if not (first_options & (1 << first_color)):
                    continue

                possible = {first_color}
                parents = [None] * len(order)
                valid = True

                for i in range(1, len(order)):
                    parent = [-1, -1, -1]
                    new_possible = set()
                    opts = available[order[i]]

                    for c in range(3):
                        if not (opts & (1 << c)):
                            continue
                        for p in possible:
                            if p != c:
                                parent[c] = p
                                new_possible.add(c)
                                break

                    if not new_possible:
                        valid = False
                        break
                    parents[i] = parent
                    possible = new_possible

                if not valid:
                    continue

                last_color = -1
                for c in possible:
                    if not is_cycle or c != first_color:
                        last_color = c
                        break

                if last_color == -1:
                    continue

                plan = [0] * len(order)
                plan[-1] = last_color
                for i in range(len(order) - 1, 0, -1):
                    plan[i - 1] = parents[i][plan[i]]
                chosen_plan = plan
                break

            if chosen_plan is None:
                rollback(start_a, start_c)
                return False

            plans.append((order, chosen_plan))

        for order, plan in plans:
            for v, c in zip(order, plan):
                if colors[v] != -1:
                    if colors[v] != c:
                        rollback(start_a, start_c)
                        return False
                elif not apply_color(v, c):
                    rollback(start_a, start_c)
                    return False

        return True

    def dfs():
        if uncolored == 0:
            return True

        m1, m2 = color_masks[1], color_masks[2]
        if m1 > m2:
            m1, m2 = m2, m1
        key = color_masks[0] | (m1 << k) | (m2 << (2 * k))
        if key in failed:
            return False

        best = -1
        best_score = (-1, -1, -1)
        max_uncolored_degree = 0

        mask = uncolored
        while mask:
            bit = mask & -mask
            v = bit.bit_length() - 1
            mask ^= bit

            degree = (adj[v] & uncolored).bit_count()
            if degree > max_uncolored_degree:
                max_uncolored_degree = degree

            saturation = 3 - available[v].bit_count()
            score = (saturation, degree, adj[v].bit_count())
            if score > best_score:
                best_score = score
                best = v

        if max_uncolored_degree <= 2:
            if low_degree_solve():
                return True
            if len(failed) < cache_limit:
                failed.add(key)
            return False

        options = []
        opts = available[best]
        for c in range(3):
            if not (opts & (1 << c)):
                continue
            if c == 2 and usage[1] == 0 and usage[2] == 0:
                continue

            impact = 0
            neighbors = adj[best] & uncolored
            while neighbors:
                bit = neighbors & -neighbors
                u = bit.bit_length() - 1
                neighbors ^= bit
                if available[u] & (1 << c):
                    impact += 1

            options.append((usage[c] == 0, impact, c))

        options.sort()

        for _, _, c in options:
            a_len = len(assigned_log)
            c_len = len(changed_log)

            if apply_color(best, c) and dfs():
                return True

            rollback(a_len, c_len)

        if len(failed) < cache_limit:
            failed.add(key)
        return False

    anchor = max(range(k), key=lambda v: adj[v].bit_count())
    if not apply_color(anchor, 0):
        return None

    if dfs():
        return colors
    return None


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

    answer = [0] * n
    remaining = (1 << n) - 1

    while remaining:
        seed_bit = remaining & -remaining
        remaining ^= seed_bit
        frontier = seed_bit
        comp_mask = 0

        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            v = bit.bit_length() - 1
            comp_mask |= bit
            nxt = adj[v] & remaining
            remaining ^= nxt
            frontier |= nxt

        vertices = []
        mask = comp_mask
        while mask:
            bit = mask & -mask
            vertices.append(bit.bit_length() - 1)
            mask ^= bit

        result = solve_component(vertices, adj)
        if result is None:
            print("NO")
            return

        for i, v in enumerate(vertices):
            answer[v] = result[i] + 1

    print("YES")
    print(*answer)


if __name__ == "__main__":
    main()