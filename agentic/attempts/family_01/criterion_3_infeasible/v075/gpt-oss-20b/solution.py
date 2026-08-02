import sys

def solve() -> None:
    input = sys.stdin.readline
    n, m = map(int, input().split())
    bitset = [0] * (n + 1)
    neighbors = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        bitset[u] |= 1 << (v - 1)
        bitset[v] |= 1 << (u - 1)
        neighbors[u].append(v)
        neighbors[v].append(u)

    for i in range(1, n + 1):
        neighbors[i].sort()

    for a in range(1, n + 1):
        for b in neighbors[a]:
            if b <= a:
                continue
            common = bitset[a] & bitset[b]
            mask = ~((1 << b) - 1)          # zero bits <= b-1
            common_masked = common & mask
            if common_masked:
                pos = (common_masked & -common_masked).bit_length() - 1
                c = pos + 1
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()