import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m = data[0], data[1]
    adj = [0] * n

    idx = 2
    for _ in range(m):
        u = data[idx] - 1
        v = data[idx + 1] - 1
        idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for a in range(n - 2):
        candidates_b = adj[a] >> (a + 1)

        while candidates_b:
            lowest = candidates_b & -candidates_b
            b = a + 1 + (lowest.bit_length() - 1)
            candidates_b ^= lowest

            candidates_c = (adj[a] & adj[b]) >> (b + 1)
            if candidates_c:
                lowest_c = candidates_c & -candidates_c
                c = b + 1 + (lowest_c.bit_length() - 1)
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    main()