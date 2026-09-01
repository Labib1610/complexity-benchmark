import sys

sys.setrecursionlimit(10000)


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

    def solve(prefix, hint=None):
        colors = [-1] * n
        used_count = [0, 0, 0]

        for v, c in enumerate(prefix):
            colors[v] = c
            used_count[c] += 1

        for v in range(len(prefix)):
            mask = adj[v] & ((1 << len(prefix)) - 1)
            while mask:
                bit = mask & -mask
                u = bit.bit_length() - 1
                mask -= bit
                if u < v and colors[u] == colors[v]:
                    return None

        counts = [[0, 0, 0] for _ in range(n)]
        for v in range(n):
            if colors[v] == -1:
                mask = adj[v]
                while mask:
                    bit = mask & -mask
                    u = bit.bit_length() - 1
                    mask -= bit
                    c = colors[u]
                    if c != -1:
                        counts[v][c] += 1

        def assign(v, c):
            colors[v] = c
            used_count[c] += 1
            mask = adj[v]
            while mask:
                bit = mask & -mask
                u = bit.bit_length() - 1
                mask -= bit
                if colors[u] == -1:
                    counts[u][c] += 1

        def undo(v, c):
            mask = adj[v]
            while mask:
                bit = mask & -mask
                u = bit.bit_length() - 1
                mask -= bit
                if colors[u] == -1:
                    counts[u][c] -= 1
            used_count[c] -= 1
            colors[v] = -1

        def dfs():
            forced = []

            while True:
                forced_v = -1
                forced_c = -1
                best_v = -1
                best_sat = -1
                best_deg = -1

                for v in range(n):
                    if colors[v] != -1:
                        continue

                    forbidden = 0
                    if counts[v][0]:
                        forbidden |= 1
                    if counts[v][1]:
                        forbidden |= 2
                    if counts[v][2]:
                        forbidden |= 4

                    if forbidden == 7:
                        for x, c in reversed(forced):
                            undo(x, c)
                        return False

                    available = 7 ^ forbidden
                    if available & (available - 1) == 0:
                        forced_v = v
                        forced_c = available.bit_length() - 1
                        break

                    saturation = forbidden.bit_count()
                    if (saturation > best_sat or
                            (saturation == best_sat and degree[v] > best_deg)):
                        best_sat = saturation
                        best_deg = degree[v]
                        best_v = v

                if forced_v != -1:
                    assign(forced_v, forced_c)
                    forced.append((forced_v, forced_c))
                    continue
                break

            if best_v == -1:
                return True

            v = best_v
            available = []
            for c in range(3):
                if counts[v][c] == 0:
                    available.append(c)

            if hint is not None and hint[v] in available:
                hc = hint[v]
                available.remove(hc)
                available.insert(0, hc)

            tried_unused = False
            for c in available:
                if used_count[c] == 0:
                    if tried_unused:
                        continue
                    tried_unused = True

                assign(v, c)
                if dfs():
                    return True
                undo(v, c)

            for x, c in reversed(forced):
                undo(x, c)
            return False

        if dfs():
            return colors[:]
        return None

    # In any colorable graph, worker 1 can be assigned shift 1 by permuting colors.
    solution = solve([0])
    if solution is None:
        print("NO")
        return

    prefix = [0]

    for i in range(1, n):
        current = solution[i]
        chosen = current

        for c in range(current):
            candidate_prefix = prefix + [c]
            candidate_solution = solve(candidate_prefix, solution)
            if candidate_solution is not None:
                solution = candidate_solution
                chosen = c
                break

        prefix.append(chosen)

    print("YES")
    print(*[c + 1 for c in prefix])


if __name__ == "__main__":
    main()