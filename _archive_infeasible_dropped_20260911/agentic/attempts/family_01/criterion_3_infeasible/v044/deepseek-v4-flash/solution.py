import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); m = int(data[1])
    adj = [0]*(n+1)
    ptr = 2
    for _ in range(m):
        u = int(data[ptr]); v = int(data[ptr+1]); ptr += 2
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    # iterate
    for a in range(1, n+1):
        for b in range(a+1, n+1):
            if (adj[a] >> b) & 1:
                common = adj[a] & adj[b]
                # keep bits > b
                mask = common & ~((1 << (b+1)) - 1)
                if mask:
                    # lowest set bit
                    c = (mask & -mask).bit_length() - 1
                    # Actually bit_length gives index+1
                    # Let's fix:
                    # lowest = mask & -mask  
                    # c = lowest.bit_length() - 1
                    print(a, b, c)
                    return
    # shouldn't happen
if __name__ == "__main__":
    main()