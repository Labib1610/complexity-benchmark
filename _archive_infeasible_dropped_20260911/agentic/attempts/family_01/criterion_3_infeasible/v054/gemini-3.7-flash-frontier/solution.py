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
        
    for a in range(1, n - 1):
        mask_a = adj[a]
        if not mask_a:
            continue
        # Check neighbors of a that are greater than a
        neighbors = mask_a >> (a + 1)
        while neighbors:
            lsb = neighbors & -neighbors
            b = lsb.bit_length() + a
            neighbors ^= lsb
            
            common = (adj[a] & adj[b]) >> (b + 1)
            if common:
                c = (common & -common).bit_length() + b
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    main()