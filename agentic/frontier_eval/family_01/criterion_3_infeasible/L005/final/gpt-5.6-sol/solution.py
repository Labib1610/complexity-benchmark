import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m = data[0], data[1]

    adjacency = [0] * n
    p = 2
    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        adjacency[u] |= 1 << v
        adjacency[v] |= 1 << u

    full_mask = (1 << n) - 1
    suffix = [full_mask ^ ((1 << (i + 1)) - 1) for i in range(n)]

    for a in range(n):
        candidates_b = adjacency[a] & suffix[a]
        while candidates_b:
            bit_b = candidates_b & -candidates_b
            candidates_b ^= bit_b
            b = bit_b.bit_length() - 1

            candidates_c = adjacency[a] & adjacency[b] & suffix[b]
            if candidates_c:
                bit_c = candidates_c & -candidates_c
                c = bit_c.bit_length() - 1
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    main()