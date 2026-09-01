import sys

def solve_component(vertices, global_adj):
    k = len(vertices)
    index = {v: i for i, v in enumerate(vertices)}
    adj = [0] * k

    for i, v in enumerate(vertices):
        mask = global_adj[v]
        local_mask = 0
        while mask:
            b = mask & -mask
            u = b.bit_length() - 1
            j = index.get(u)
            if j is not None:
                local_mask |= 1 << j
            mask ^= b
        adj[i] = local_mask

    degrees = [x.bit_count() for x in adj]
    full_colors = 0b111

    def find_coloring(fixed):
        colors = [-1] * k
        saturation = [0] * k
        counts = [0, 0, 0]
        color_masks = [0, 0, 0]
        uncolored = (1 << k) - 1

        for v, c in enumerate(fixed):
            if c < 0:
                continue
            if adj[v] & color_masks[c]:
                return None
            colors[v] = c
            color_masks[c] |= 1 << v
            counts[c] += 1
            uncolored &= ~(1 << v)

        for v, c in enumerate(colors):
            if c >= 0:
                continue
            mask = adj[v]
            sat = 0
            for col in range(3):
                if mask & color_masks[col]:
                    sat |= 1 << col
            if sat == full_colors:
                return None
            saturation[v] = sat

        result = None

        def dfs(remaining):
            nonlocal result
            if remaining == 0:
                result = colors.copy()
                return True

            selected = -1
            best_sat = -1
            best_degree = -1

            scan = remaining
            while scan:
                bit = scan & -scan
                v = bit.bit_length() - 1
                sat_count = saturation[v].bit_count()
                if sat_count > best_sat or (
                    sat_count == best_sat and degrees[v] > best_degree
                ):
                    selected = v
                    best_sat = sat_count
                    best_degree = degrees[v]
                scan ^= bit

            available = full_colors ^ saturation[selected]
            if available == 0:
                return False

            tried_unused = False
            for c in range(3):
                color_bit = 1 << c
                if not (available & color_bit):
                    continue

                if counts[c] == 0:
                    if tried_unused:
                        continue
                    tried_unused = True

                colors[selected] = c
                counts[c] += 1
                changed = []
                impossible = False

                neighbors = adj[selected] & remaining
                scan_neighbors = neighbors
                while scan_neighbors:
                    bit = scan_neighbors & -scan_neighbors
                    u = bit.bit_length() - 1
                    if not (saturation[u] & color_bit):
                        changed.append(u)
                        saturation[u] |= color_bit
                        if saturation[u] == full_colors:
                            impossible = True
                    scan_neighbors ^= bit

                if not impossible and dfs(remaining & ~(1 << selected)):
                    return True

                for u in changed:
                    saturation[u] ^= color_bit
                counts[c] -= 1
                colors[selected] = -1

            return False

        return result if dfs(uncolored) else None

    fixed = [-1] * k
    fixed[0] = 0
    witness = find_coloring(fixed)
    if witness is None:
        return None

    for i in range(1, k):
        chosen = False
        for c in range(witness[i]):
            conflict = False
            neighbors = adj[i]
            scan = neighbors
            while scan:
                bit = scan & -scan
                u = bit.bit_length() - 1
                if u < i and fixed[u] == c:
                    conflict = True
                    break
                scan ^= bit

            if conflict:
                continue

            fixed[i] = c
            candidate = find_coloring(fixed)
            if candidate is not None:
                witness = candidate
                chosen = True
                break
            fixed[i] = -1

        if not chosen:
            fixed[i] = witness[i]

    return fixed


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

    answer = [-1] * n
    unseen = (1 << n) - 1

    while unseen:
        start_bit = unseen & -unseen
        frontier = start_bit
        component_mask = 0
        unseen ^= start_bit

        while frontier:
            component_mask |= frontier
            next_frontier = 0
            scan = frontier
            while scan:
                bit = scan & -scan
                v = bit.bit_length() - 1
                next_frontier |= adj[v]
                scan ^= bit
            next_frontier &= unseen
            unseen &= ~next_frontier
            frontier = next_frontier

        vertices = []
        scan = component_mask
        while scan:
            bit = scan & -scan
            vertices.append(bit.bit_length() - 1)
            scan ^= bit

        coloring = solve_component(vertices, adj)
        if coloring is None:
            print("NO")
            return

        for i, v in enumerate(vertices):
            answer[v] = coloring[i] + 1

    print("YES")
    print(*answer)


if __name__ == "__main__":
    main()