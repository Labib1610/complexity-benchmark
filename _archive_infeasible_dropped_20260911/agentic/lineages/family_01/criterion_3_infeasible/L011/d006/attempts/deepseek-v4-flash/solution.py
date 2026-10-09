import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [0] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if (adj[a] >> b) & 1:
                common = adj[a] & adj[b]
                # remove bits <= b
                mask = ((1 << (b + 1)) - 1)
                common &= ~mask
                if common:
                    # find lowest set bit
                    c = (common & -common).bit_length() - 1
                    print(a, b, c)
                    return

if __name__ == "__main__":
    main()