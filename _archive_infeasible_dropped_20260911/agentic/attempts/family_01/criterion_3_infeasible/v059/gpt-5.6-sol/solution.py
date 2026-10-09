import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m = data[0], data[1]

    adjacency = [0] * n
    bits = [1 << i for i in range(n)]

    pos = 2
    for _ in range(m):
        u = data[pos] - 1
        v = data[pos + 1] - 1
        pos += 2
        adjacency[u] |= bits[v]
        adjacency[v] |= bits[u]

    higher = [(-1) << (i + 1) for i in range(n)]

    for a in range(n - 2):
        neighbors = adjacency[a] & higher[a]

        while neighbors:
            lowest = neighbors & -neighbors
            b = lowest.bit_length() - 1

            common = adjacency[a] & adjacency[b] & higher[b]
            if common:
                c = (common & -common).bit_length()
                print(a + 1, b + 1, c)
                return

            neighbors ^= lowest

if __name__ == "__main__":
    main()