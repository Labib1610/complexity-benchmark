import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj_bit = [0] * (n + 1)
    adj_list = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj_bit[u] |= 1 << v
        adj_bit[v] |= 1 << u
        adj_list[u].append(v)
        adj_list[v].append(u)

    for a in range(1, n - 1):
        for b in sorted(adj_list[a]):
            if b <= a:
                continue
            common = adj_bit[a] & adj_bit[b]
            mask = (1 << (b + 1)) - 1  # clear bits <= b
            common &= ~mask
            if common:
                lowbit = common & -common
                c = lowbit.bit_length() - 1
                print(a, b, c)
                return

if __name__ == "__main__":
    main()