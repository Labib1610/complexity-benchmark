import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adj_bits = [0] * (n + 1)
    adj_lists = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = next(it)
        v = next(it)
        adj_bits[u] |= 1 << (v - 1)
        adj_bits[v] |= 1 << (u - 1)
        adj_lists[u].append(v)
        adj_lists[v].append(u)

    for a in range(1, n + 1):
        lst = adj_lists[a]
        lst.sort()
        for b in lst:
            if b <= a:
                continue
            mask = adj_bits[a] & adj_bits[b]
            shift = b  # remove bits for vertices <= b
            x = mask >> shift
            if x == 0:
                continue
            y = x & -x
            idx = y.bit_length() - 1
            c = shift + 1 + idx
            print(a, b, c)
            return

if __name__ == "__main__":
    main()