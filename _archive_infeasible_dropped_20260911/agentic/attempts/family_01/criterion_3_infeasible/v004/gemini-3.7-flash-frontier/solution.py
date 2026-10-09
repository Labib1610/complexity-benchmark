import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [0] * (n + 1)
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
        
    for a in range(1, n + 1):
        adj_a = adj[a]
        for b in range(a + 1, n + 1):
            if (adj_a >> b) & 1:
                common = (adj_a & adj[b]) >> (b + 1)
                if common:
                    lsb = common & -common
                    c = b + lsb.bit_length()
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    main()