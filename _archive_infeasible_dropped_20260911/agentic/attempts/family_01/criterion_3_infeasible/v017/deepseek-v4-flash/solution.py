import sys

def main():
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
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    
    for a in range(1, n+1):
        for b in range(a+1, n+1):
            if (adj[a] >> b) & 1:
                common = adj[a] & adj[b]
                # remove bits <= b
                common &= ~((1 << (b+1)) - 1)
                if common:
                    # find lowest set bit
                    c = (common & -common).bit_length() - 1
                    # Actually: lowbit = common & -common; c = lowbit.bit_length() - 1
                    low = common & -common
                    c = low.bit_length() - 1
                    print(a, b, c)
                    return

if __name__ == "__main__":
    main()