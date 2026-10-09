import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])

    adj = [0] * n
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # Check for self-loops
    for i in range(n):
        if (adj[i] >> i) & 1:
            print("NO")
            return

    assignment = [0] * n
    deg = [bin(adj[i]).count("1") for i in range(n)]
    avail = [7] * n
    pc = [0, 1, 1, 2, 1, 2, 2, 3]

    def backtrack(uncolored_count):
        if uncolored_count == 0:
            return True

        best_v = -1
        min_c = 4
        max_d = -1

        for i in range(n):
            if assignment[i] == 0:
                c = pc[avail[i]]
                if c == 0:
                    return False
                if c < min_c or (c == min_c and deg[i] > max_d):
                    min_c = c
                    max_d = deg[i]
                    best_v = i
                    if min_c == 1:
                        break

        v = best_v
        mask = avail[v]

        for color_idx in range(3):
            c_bit = 1 << color_idx
            if mask & c_bit:
                assignment[v] = color_idx + 1

                changed = []
                valid = True
                nbrs = adj[v]
                while nbrs:
                    lsb = nbrs & -nbrs
                    u = lsb.bit_length() - 1
                    nbrs ^= lsb
                    if assignment[u] == 0:
                        if avail[u] & c_bit:
                            avail[u] ^= c_bit
                            changed.append(u)
                            if avail[u] == 0:
                                valid = False

                if valid and backtrack(uncolored_count - 1):
                    return True

                for u in changed:
                    avail[u] |= c_bit

                assignment[v] = 0

        return False

    if backtrack(n):
        print("YES")
        print(*(assignment[i] for i in range(n)))
    else:
        print("NO")


if __name__ == "__main__":
    solve()