import sys

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    adj = [0] * (n + 1)
    edges = []
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)

    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if (adj[a] >> b) & 1:
                common = adj[a] & adj[b]
                common &= ~((1 << (b + 1)) - 1)
                if common:
                    c = (common & -common).bit_length() - 1
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    main()