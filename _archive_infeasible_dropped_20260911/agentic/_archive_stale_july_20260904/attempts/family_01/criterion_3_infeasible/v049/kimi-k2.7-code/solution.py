import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj_bits = [0] * (n + 1)
    adj_list = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj_bits[u] |= 1 << v
        adj_bits[v] |= 1 << u
        adj_list[u].append(v)
        adj_list[v].append(u)
    for i in range(1, n + 1):
        adj_list[i].sort()
    result = None
    for a in range(1, n + 1):
        for b in adj_list[a]:
            if b <= a:
                continue
            mask = adj_bits[a] & adj_bits[b]
            mask &= -(1 << (b + 1))
            if mask:
                c = (mask & -mask).bit_length() - 1
                result = (a, b, c)
                break
        if result:
            break
    if result:
        sys.stdout.write(f"{result[0]} {result[1]} {result[2]}")

if __name__ == "__main__":
    solve()