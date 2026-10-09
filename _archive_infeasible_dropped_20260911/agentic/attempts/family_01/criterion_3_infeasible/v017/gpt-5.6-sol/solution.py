import sys

def main():
    data = map(int, sys.stdin.buffer.read().split())
    it = iter(data)
    n = next(it)
    m = next(it)

    adjacency = [0] * n

    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        adjacency[u] |= 1 << v
        adjacency[v] |= 1 << u

    full_mask = (1 << n) - 1
    higher = [full_mask ^ ((1 << (i + 1)) - 1) for i in range(n)]

    for a in range(n - 2):
        candidates = adjacency[a] & higher[a]

        while candidates:
            lowest = candidates & -candidates
            b = lowest.bit_length() - 1
            candidates ^= lowest

            common = adjacency[a] & adjacency[b] & higher[b]
            if common:
                c = (common & -common).bit_length() - 1
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    main()