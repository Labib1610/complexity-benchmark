import sys

def main():
    data = sys.stdin.read().strip().split()
    n, m = int(data[0]), int(data[1])
    adj = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        adj[u].add(v)
        adj[v].add(u)
    
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if b in adj[a]:
                # Find smallest c > b that is connected to both a and b
                for c in range(b + 1, n + 1):
                    if c in adj[a] and c in adj[b]:
                        print(a, b, c)
                        return

if __name__ == "__main__":
    main()