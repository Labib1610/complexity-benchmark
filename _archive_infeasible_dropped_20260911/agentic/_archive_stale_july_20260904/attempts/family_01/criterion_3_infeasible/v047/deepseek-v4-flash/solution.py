import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    for a in range(n):
        # neighbors of a with index > a
        neigh = []
        mask = adj[a] >> (a+1)
        while mask:
            lsb = mask & -mask
            b = (lsb.bit_length() - 1) + (a+1)
            neigh.append(b)
            mask -= lsb
        # neigh is already sorted because we go from low to high bits
        for b in neigh:
            # common neighbors of a and b that are > b
            common = adj[a] & adj[b] & ~((1 << (b+1)) - 1)
            if common:
                c = (common & -common).bit_length() - 1
                print(a+1, b+1, c+1)
                return

if __name__ == "__main__":
    main()