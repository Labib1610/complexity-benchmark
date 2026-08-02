import sys

def solve() -> None:
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    adj = [0] * (n + 1)
    idx = 2
    for _ in range(m):
        u, v = data[idx], data[idx + 1]
        idx += 2
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    for a in range(1, n - 1):
        mask_a = adj[a]
        # consider only neighbors greater than a
        neigh_mask = mask_a >> a
        while neigh_mask:
            low = neigh_mask & -neigh_mask
            offset = low.bit_length() - 1
            b = a + offset + 1  # vertex number
            common = adj[a] & adj[b]
            mask_c = common >> b
            if mask_c:
                lowc = mask_c & -mask_c
                c = b + lowc.bit_length()
                print(a, b, c)
                return
            neigh_mask ^= low

if __name__ == "__main__":
    solve()