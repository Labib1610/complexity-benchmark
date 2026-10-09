import sys

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    adj = [0] * (n + 1)
    adj_list = [[] for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    for a in range(1, n + 1):
        adj_list[a].sort()
        for b in adj_list[a]:
            if b <= a:
                continue
            common = (adj[a] & adj[b]) >> (b + 1)
            if common:
                c = b + (common & -common).bit_length()
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    main()