import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    
    # We'll store for each registry a bitmask of pulses it participates in
    masks = [0] * (n + 1)
    
    for k in range(m):
        u, v = map(int, input().split())
        masks[u] |= (1 << k)
        masks[v] |= (1 << k)
    
    # Build adjacency bitsets: adj[i] has bit j set if dot(i,j) > 0
    adj = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if masks[i] & masks[j]:
                adj[i] |= (1 << j)
                adj[j] |= (1 << i)
    
    # Now find lexicographically smallest triple
    for x1 in range(1, n + 1):
        # Get neighbors of x1 with index > x1
        neigh = adj[x1] & ~((1 << (x1 + 1)) - 1)  # clear bits <= x1
        while neigh:
            # get smallest set bit
            lsb = neigh & -neigh
            x2 = lsb.bit_length()  # position of bit (1-indexed)
            # common neighbors of x1 and x2 with index > x2
            common = adj[x1] & adj[x2] & ~((1 << (x2 + 1)) - 1)
            if common:
                lsb2 = common & -common
                x3 = lsb2.bit_length()
                print(x1, x2, x3)
                return
            neigh ^= lsb

if __name__ == "__main__":
    main()