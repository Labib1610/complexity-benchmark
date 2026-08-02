import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj_bits = [0] * n
    adj_list = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj_bits[u] |= 1 << v
        adj_bits[v] |= 1 << u
        adj_list[u].append(v)
        adj_list[v].append(u)

    # sort neighbor lists to ensure ascending order
    for lst in adj_list:
        lst.sort()

    for a in range(n):
        a_bits = adj_bits[a]
        for b in adj_list[a]:
            if b <= a:
                continue
            # intersection of neighbors of a and b
            common = a_bits & adj_bits[b]
            # mask out bits <= b
            mask = common >> (b + 1)
            if mask:
                # isolate lowest set bit
                lowbit = mask & -mask
                # position of that bit relative to shifted mask
                offset = lowbit.bit_length() - 1
                c = offset + (b + 1)
                # output 1-indexed
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()