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
        candidates_b = adjacency[a] & (-1 << (a + 1))
        while candidates_b:
            b_bit = candidates_b & -candidates_b
            candidates_b ^= b_bit
            b = b_bit.bit_length() - 1

            common = adjacency[a] & adjacency[b] & (-1 << (b + 1))
            if common:
                c = (common & -common).bit_length() - 1
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    main()