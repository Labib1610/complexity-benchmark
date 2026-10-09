import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m = data[0], data[1]

    adjacency = [0] * n
    pos = 2
    for _ in range(m):
        u = data[pos] - 1
        v = data[pos + 1] - 1
        pos += 2
        adjacency[u] |= 1 << v
        adjacency[v] |= 1 << u

    for a in range(n):
        adj_a = adjacency[a]
        candidates_b = adj_a >> (a + 1)

        while candidates_b:
            lowest_b = candidates_b & -candidates_b
            b = a + 1 + lowest_b.bit_length() - 1

            common = (adj_a & adjacency[b]) >> (b + 1)
            if common:
                lowest_c = common & -common
                c = b + 1 + lowest_c.bit_length() - 1
                print(a + 1, b + 1, c + 1)
                return

            candidates_b ^= lowest_b

if __name__ == "__main__":
    main()