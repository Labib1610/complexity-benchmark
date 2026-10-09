import sys

# Increase recursion depth just in case
sys.setrecursionlimit(10000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])

    edges = []
    adj_v = [[] for _ in range(n + 1)]

    idx = 2
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        edges.append((u, v))
        adj_v[u].append(i)
        adj_v[v].append(i)

    # For each edge, find its 4 neighboring edges in the line graph
    adj_e = [[] for _ in range(m)]
    for i in range(m):
        u, v = edges[i]
        neighbors = set()
        for e in adj_v[u]:
            if e != i:
                neighbors.add(e)
        for e in adj_v[v]:
            if e != i:
                neighbors.add(e)
        adj_e[i] = list(neighbors)

    mask = [7] * m  # bitmask of available colors: 1 (shift 1), 2 (shift 2), 4 (shift 3)

    trail = []

    def set_mask(e, new_m):
        old_m = mask[e]
        if old_m == new_m:
            return True
        if (old_m & new_m) != new_m:
            new_m = old_m & new_m
        if new_m == 0:
            return False
        mask[e] = new_m
        trail.append((e, old_m))
        return True

    def propagate():
        # Queue of edges to process
        head = len(trail)
        # We process from the current point in trail
        prop_idx = head - 1  # will process newly added constraints
        # But wait, initially trail is empty.
        # Let's keep a queue of forced decisions.
        return True

    # A more systematic constraint propagation with trail:
    def assign(edge, color_bit):
        trail_start = len(trail)
        queue = [(edge, color_bit)]

        while queue:
            e, c_bit = queue.pop()
            if mask[e] & c_bit == 0:
                return False, trail_start
            if mask[e] != c_bit:
                if not set_mask(e, c_bit):
                    return False, trail_start

            # For all neighbors in line graph, remove c_bit
            for ne in adj_e[e]:
                if mask[ne] & c_bit:
                    new_m = mask[ne] & (~c_bit)
                    if new_m == 0:
                        return False, trail_start
                    if not set_mask(ne, new_m):
                        return False, trail_start
                    # If ne is forced to a single color
                    if new_m in (1, 2, 4):
                        queue.append((ne, new_m))

            # Also check vertices: for vertex u of e, the three edges must have colors 1, 2, 4
            u, v = edges[e]
            for vertex in (u, v):
                # For each color bit in 1, 2, 4:
                # Count how many edges at `vertex` can have it
                inc_edges = adj_v[vertex]
                for cb in (1, 2, 4):
                    possible = [ie for ie in inc_edges if (mask[ie] & cb)]
                    if len(possible) == 0:
                        return False, trail_start
                    if len(possible) == 1:
                        ie = possible[0]
                        if mask[ie] != cb:
                            if not set_mask(ie, cb):
                                return False, trail_start
                            queue.append((ie, cb))

        return True, trail_start

    def backtrack(trail_start):
        while len(trail) > trail_start:
            e, old_m = trail.pop()
            mask[e] = old_m

    # Symmetry breaking: find first unassigned edge, assign it color 1 (bit 1)
    # in the first connected component, etc.

    def solve_search():
        # Find unassigned edge with minimum remaining values > 1
        best_e = -1
        min_choices = 4

        for e in range(m):
            m_val = mask[e]
            if m_val in (1, 2, 4):
                continue
            cnt = (m_val & 1) + ((m_val >> 1) & 1) + ((m_val >> 2) & 1)
            if cnt < min_choices:
                min_choices = cnt
                best_e = e
                if cnt == 2:
                    break

        if best_e == -1:
            return True  # All edges assigned

        cur_mask = mask[best_e]
        choices = []
        for bit in (1, 2, 4):
            if cur_mask & bit:
                choices.append(bit)

        for bit in choices:
            ok, trail_start = assign(best_e, bit)
            if ok:
                if solve_search():
                    return True
            backtrack(trail_start)

        return False

    # Try to solve
    if solve_search():
        bit_to_color = {1: 1, 2: 2, 4: 3}
        ans = [bit_to_color[mask[i]] for i in range(m)]
        print("YES")
        print(*(ans))
    else:
        print("NO")


if __name__ == "__main__":
    solve()