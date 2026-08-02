import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    edges = data[2:]

    mask = [0] * n          # bitmask of neighbors for each vertex
    adj = [[] for _ in range(n)]  # adjacency lists

    for i in range(0, 2 * m, 2):
        u = edges[i] - 1
        v = edges[i + 1] - 1
        mask[u] |= 1 << v
        mask[v] |= 1 << u
        adj[u].append(v)
        adj[v].append(u)

    for i in range(n):
        adj[i].sort()

    for a in range(n):
        for b in adj[a]:
            if b <= a:
                continue
            intersection = mask[a] & mask[b]
            shifted = intersection >> (b + 1)
            if shifted:
                lowbit = shifted & -shifted
                pos = lowbit.bit_length() - 1
                c = pos + b + 1
                sys.stdout.write(f"{a+1} {b+1} {c+1}\n")
                return

if __name__ == "__main__":
    solve()