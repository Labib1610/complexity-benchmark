import sys

def solve():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    adj = [0] * (n + 1)
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        adj[u] |= (1 << (v - 1))
        adj[v] |= (1 << (u - 1))
    
    for a in range(1, n + 1):
        mask_a = adj[a]
        # Check neighbors b > a
        nbrs = mask_a & ~((1 << a) - 1)  # only > a
        while nbrs:
            lsb = nbrs & -nbrs
            b = lsb.bit_length()  # b = index + 1
            intersection = adj[a] & adj[b]
            if intersection:
                c_bit = intersection & -intersection
                c = c_bit.bit_length()
                print(a, b, c)
                return
            nbrs ^= lsb

if __name__ == "__main__":
    solve()