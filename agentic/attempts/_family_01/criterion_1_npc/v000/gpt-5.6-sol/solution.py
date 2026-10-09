import sys

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

    all_mask = (1 << n) - 1
    compatible = [
        all_mask & ~(adj[v] | (1 << v))
        for v in range(n)
    ]

    answer = None

    def analyze(selected, allowed):
        active = all_mask ^ selected
        color = [-1] * n
        parent = [-1] * n
        depth = [0] * n
        side0 = 0
        side1 = 0
        best_cycle = 0
        best_count = n + 1
        best_length = n + 1

        remaining = active
        while remaining:
            start_bit = remaining & -remaining
            start = start_bit.bit_length() - 1
            color[start] = 0
            side0 |= start_bit
            remaining ^= start_bit

            queue = [start]
            head = 0

            while head < len(queue):
                u = queue[head]
                head += 1

                neighbors = adj[u] & active
                bits = neighbors
                while bits:
                    vb = bits & -bits
                    bits ^= vb
                    v = vb.bit_length() - 1

                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        parent[v] = u
                        depth[v] = depth[u] + 1
                        if color[v] == 0:
                            side0 |= vb
                        else:
                            side1 |= vb
                        if remaining & vb:
                            remaining ^= vb
                        queue.append(v)
                    elif v > u and color[v] == color[u]:
                        x, y = u, v
                        cycle = 0

                        while depth[x] > depth[y]:
                            cycle |= 1 << x
                            x = parent[x]
                        while depth[y] > depth[x]:
                            cycle |= 1 << y
                            y = parent[y]
                        while x != y:
                            cycle |= (1 << x) | (1 << y)
                            x = parent[x]
                            y = parent[y]
                        cycle |= 1 << x

                        count = (cycle & allowed).bit_count()
                        if count == 0:
                            return False, cycle, 0
                        length = cycle.bit_count()
                        if count < best_count or (
                            count == best_count and length < best_length
                        ):
                            best_count = count
                            best_length = length
                            best_cycle = cycle

        if best_cycle == 0:
            return True, side0, side1
        return False, best_cycle, 0

    def search(selected, allowed):
        nonlocal answer

        bipartite, first, second = analyze(selected, allowed)
        if bipartite:
            answer = (selected, first, second)
            return True

        cycle = first
        candidates_mask = cycle & allowed
        if candidates_mask == 0:
            return False

        active = all_mask ^ selected
        candidates = []
        bits = candidates_mask
        while bits:
            bit = bits & -bits
            bits ^= bit
            v = bit.bit_length() - 1
            candidates.append(v)

        candidates.sort(
            key=lambda v: (adj[v] & active).bit_count(),
            reverse=True
        )

        remaining_allowed = allowed
        for v in candidates:
            bit = 1 << v
            new_allowed = (remaining_allowed & ~bit) & compatible[v]

            if search(selected | bit, new_allowed):
                return True

            remaining_allowed &= ~bit

        return False

    if not search(0, all_mask):
        print("NO")
        return

    selected, side0, side1 = answer
    shifts = []
    for i in range(n):
        bit = 1 << i
        if selected & bit:
            shifts.append("1")
        elif side0 & bit:
            shifts.append("2")
        else:
            shifts.append("3")

    print("YES")
    print(" ".join(shifts))

if __name__ == "__main__":
    main()