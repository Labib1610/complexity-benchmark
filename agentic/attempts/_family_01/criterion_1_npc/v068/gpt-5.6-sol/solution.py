import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

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
        return

    answer = [-1] * n
    unseen = (1 << n) - 1
    components = []

    while unseen:
        start_bit = unseen & -unseen
        component = 0
        frontier = start_bit
        unseen ^= start_bit

        while frontier:
            component |= frontier
            neighbors = 0
            x = frontier
            while x:
                bit = x & -x
                v = bit.bit_length() - 1
                neighbors |= adj[v]
                x ^= bit
            frontier = neighbors & unseen
            unseen ^= frontier

        components.append(component)

    def bipartite_coloring(component):
        side = [-1] * n
        start = (component & -component).bit_length() - 1
        side[start] = 0
        stack = [start]

        while stack:
            v = stack.pop()
            x = adj[v] & component
            while x:
                bit = x & -x
                u = bit.bit_length() - 1
                x ^= bit
                if side[u] == -1:
                    side[u] = side[v] ^ 1
                    stack.append(u)
                elif side[u] == side[v]:
                    return None
        return side

    def three_color(component):
        vertices = []
        x = component
        while x:
            bit = x & -x
            vertices.append(bit.bit_length() - 1)
            x ^= bit

        color = [-1] * n
        forbidden = [0] * n
        counts = [[0] * n for _ in range(3)]
        degree = [(adj[v] & component).bit_count() for v in range(n)]

        def search(uncolored, used_colors):
            if not uncolored:
                return True

            best = -1
            best_key = (-1, -1, -1)
            x = uncolored

            while x:
                bit = x & -x
                v = bit.bit_length() - 1
                x ^= bit

                f = forbidden[v]
                if f == 7:
                    return False

                key = (
                    f.bit_count(),
                    (adj[v] & uncolored).bit_count(),
                    degree[v]
                )
                if key > best_key:
                    best_key = key
                    best = v

            available = (~forbidden[best]) & 7
            limit = min(3, used_colors + 1)
            candidates = [c for c in range(limit) if available & (1 << c)]

            if not candidates:
                return False

            new_uncolored = uncolored & ~(1 << best)

            for c in candidates:
                bit_c = 1 << c
                color[best] = c
                conflict = False

                affected = adj[best] & new_uncolored
                y = affected
                while y:
                    bit = y & -y
                    w = bit.bit_length() - 1
                    y ^= bit

                    if counts[c][w] == 0:
                        forbidden[w] |= bit_c
                    counts[c][w] += 1

                    if forbidden[w] == 7:
                        conflict = True

                next_used = used_colors + 1 if c == used_colors else used_colors
                if not conflict and search(new_uncolored, next_used):
                    return True

                y = affected
                while y:
                    bit = y & -y
                    w = bit.bit_length() - 1
                    y ^= bit

                    counts[c][w] -= 1
                    if counts[c][w] == 0:
                        forbidden[w] &= ~bit_c

                color[best] = -1

            return False

        if search(component, 0):
            return color
        return None

    for component in components:
        coloring = bipartite_coloring(component)
        if coloring is None:
            coloring = three_color(component)
            if coloring is None:
                print("NO")
                return

        x = component
        while x:
            bit = x & -x
            v = bit.bit_length() - 1
            x ^= bit
            answer[v] = coloring[v]

    print("YES")
    print(*[c + 1 for c in answer])

if __name__ == "__main__":
    main()