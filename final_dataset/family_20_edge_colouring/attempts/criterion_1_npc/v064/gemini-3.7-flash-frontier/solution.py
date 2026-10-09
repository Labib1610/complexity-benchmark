import sys

# Increase recursion depth just in case
sys.setrecursionlimit(20000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    adj_edges = [[] for _ in range(n + 1)]
    edges = []

    idx = 2
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        edges.append((u, v))
        adj_edges[u].append(i)
        adj_edges[v].append(i)

    # Edge color domain bitmasks: bit 0 -> color 1, bit 1 -> color 2, bit 2 -> color 3
    # Initial mask is 7 (111 in binary)
    mask = [7] * m
    color_assigned = [0] * m

    # Unit propagation queue
    def propagate():
        # Queue of forced edge assignments or reductions
        changed = True
        while changed:
            changed = False
            # Check edge domains
            for i in range(m):
                m_i = mask[i]
                if m_i == 0:
                    return False
                # If single color possible and not fixed
                if (m_i & (m_i - 1)) == 0:
                    c = m_i.bit_length() - 1  # 0, 1, or 2
                    u, v = edges[i]
                    for nu in (u, v):
                        for e in adj_edges[nu]:
                            if e != i:
                                if mask[e] & (1 << c):
                                    mask[e] &= ~(1 << c)
                                    if mask[e] == 0:
                                        return False
                                    changed = True

            # Check vertex-color constraints: each color must appear on exactly one incident edge
            for u in range(1, n + 1):
                inc = adj_edges[u]
                for c in range(3):
                    c_bit = 1 << c
                    possible = [e for e in inc if (mask[e] & c_bit)]
                    if len(possible) == 0:
                        return False
                    if len(possible) == 1:
                        e = possible[0]
                        if mask[e] != c_bit:
                            mask[e] = c_bit
                            changed = True
        return True

    def backtrack():
        # Find unassigned edge with minimum remaining values > 1
        best_e = -1
        best_count = 4
        for i in range(m):
            m_i = mask[i]
            count = bin(m_i).count("1")
            if count > 1:
                if count < best_count:
                    best_count = count
                    best_e = i
                    if count == 2:
                        break

        if best_e == -1:
            return True

        saved_mask = list(mask)
        m_e = saved_mask[best_e]

        # Try possible colors for best_e
        for c in range(3):
            if m_e & (1 << c):
                mask[:] = saved_mask
                mask[best_e] = 1 << c
                if propagate():
                    if backtrack():
                        return True

        mask[:] = saved_mask
        return False

    if not propagate():
        print("NO")
        return

    if backtrack():
        print("YES")
        ans = [(mask[i].bit_length()) for i in range(m)]
        print(*(ans))
    else:
        print("NO")


if __name__ == "__main__":
    solve()