import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    neigh = [0] * n
    idx = 2
    for _ in range(m):
        u = data[idx] - 1
        v = data[idx + 1] - 1
        idx += 2
        neigh[u] |= 1 << v
        neigh[v] |= 1 << u

    for a in range(n - 2):
        na = neigh[a]
        for b in range(a + 1, n - 1):
            if (na >> b) & 1:  # edge a-b exists
                inter = na & neigh[b]
                mask = inter >> (b + 1)  # only consider nodes > b
                if mask:
                    pos = (mask & -mask).bit_length() - 1
                    c = b + 1 + pos
                    print(a + 1, b + 1, c + 1)
                    return

if __name__ == "__main__":
    main()