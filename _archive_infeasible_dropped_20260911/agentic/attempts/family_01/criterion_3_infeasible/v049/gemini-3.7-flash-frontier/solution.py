import sys

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    adj = [0] * (n + 1)
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
        
    for a in range(1, n + 1):
        adj_a = adj[a]
        # Iterate over all b > a that are neighbors of a
        # To iterate over neighbors efficiently:
        mask_neighbors = adj_a >> (a + 1)
        while mask_neighbors:
            lsb = mask_neighbors & -mask_neighbors
            b = a + 1 + lsb.bit_length() - 1
            mask_neighbors ^= lsb
            
            common = adj_a & adj[b]
            # We need c > b
            common_c = common >> (b + 1)
            if common_c:
                c_lsb = common_c & -common_c
                c = b + 1 + c_lsb.bit_length() - 1
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    main()