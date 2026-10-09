import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # suffix[b] has bits with index > b set
    suffix = [0] * (n + 1)
    for b in range(n + 1):
        suffix[b] = ~((1 << (b + 1)) - 1)

    for a in range(1, n + 1):
        bits = adj[a] & suffix[a]   # neighbors of a that are greater than a
        while bits:
            lsb = bits & -bits
            b = lsb.bit_length() - 1
            common = adj[a] & adj[b]
            t = common & suffix[b]   # common neighbors greater than b
            if t:
                c = (t & -t).bit_length() - 1
                sys.stdout.write(f"{a} {b} {c}")
                return
            bits ^= lsb

if __name__ == "__main__":
    solve()