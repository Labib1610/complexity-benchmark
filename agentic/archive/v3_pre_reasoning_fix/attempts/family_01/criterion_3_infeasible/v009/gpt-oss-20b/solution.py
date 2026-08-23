import sys

def solve() -> None:
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj_bits = [0] * n
    adj_list = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj_bits[u] |= 1 << v
        adj_bits[v] |= 1 << u
        adj_list[u].append(v)
        adj_list[v].append(u)

    for lst in adj_list:
        lst.sort()

    for a in range(n):
        for b in adj_list[a]:
            if b <= a:
                continue
            common = adj_bits[a] & adj_bits[b]
            mask = (~0) << (b + 1)
            common_masked = common & mask
            if common_masked:
                c = (common_masked & -common_masked).bit_length() - 1
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()