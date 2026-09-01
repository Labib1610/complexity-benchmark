import sys

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    adj = [0] * (n + 1)
    neighbors = [[] for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
        if u < v:
            neighbors[u].append(v)
        else:
            neighbors[v].append(u)
            
    for u in range(1, n + 1):
        neighbors[u].sort()
        
    for a in range(1, n + 1):
        adj_a = adj[a]
        for b in neighbors[a]:
            common = (adj_a & adj[b]) >> (b + 1)
            if common:
                lsb = common & -common
                c = lsb.bit_length() + b
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    main()