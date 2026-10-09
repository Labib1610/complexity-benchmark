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
        v = int(data[idx + 1])
        idx += 2
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
        neighbors[u].append(v)
        neighbors[v].append(u)
        
    for a in range(1, n + 1):
        neighbors[a].sort()
        for b in neighbors[a]:
            if b <= a:
                continue
            mask = (adj[a] & adj[b]) >> (b + 1)
            if mask:
                lsb = mask & -mask
                c = (b + 1) + lsb.bit_length() - 1
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    main()