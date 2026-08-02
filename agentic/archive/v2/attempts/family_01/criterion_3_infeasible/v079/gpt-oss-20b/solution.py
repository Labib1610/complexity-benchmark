import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    adjacency = [0] * n
    neighbors = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = data[idx] - 1
        v = data[idx + 1] - 1
        idx += 2
        adjacency[u] |= 1 << v
        adjacency[v] |= 1 << u
        neighbors[u].append(v)
        neighbors[v].append(u)

    for i in range(n):
        neighbors[i].sort()

    for a in range(n):
        for b in neighbors[a]:
            if b <= a:
                continue
            common = adjacency[a] & adjacency[b]
            mask = common >> (b + 1)          # vertices greater than b
            if mask:
                lowbit = mask & -mask
                k = lowbit.bit_length() - 1
                w = b + 1 + k
                print(a + 1, b + 1, w + 1)
                return

if __name__ == "__main__":
    solve()