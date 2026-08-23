import sys
import bisect

def solve():
    data = sys.stdin.buffer.read().split()
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
    for i in range(n):
        adj_list[i].sort()
    for a in range(n):
        bits_a = adj_bits[a]
        lst = adj_list[a]
        idx = bisect.bisect_right(lst, a)
        for b in lst[idx:]:
            common = bits_a & adj_bits[b] & (-1 << (b + 1))
            if common:
                c = (common & -common).bit_length() - 1
                sys.stdout.write(f"{a + 1} {b + 1} {c + 1}\n")
                return

if __name__ == "__main__":
    solve()