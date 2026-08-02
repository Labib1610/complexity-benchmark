import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    neighbors = [0] * n
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        neighbors[u] |= 1 << v
        neighbors[v] |= 1 << u
        adj[u].append(v)
        adj[v].append(u)

    for a in range(n):
        for b in adj[a]:
            if b <= a:
                continue
            inter = neighbors[a] & neighbors[b]
            temp = inter >> (b + 1)
            if temp:
                pos = (temp & -temp).bit_length() - 1
                c = b + 1 + pos
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()