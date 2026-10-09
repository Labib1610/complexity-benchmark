import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    adj = [set() for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        idx += 2
        adj[u].add(v)
        adj[v].add(u)
    
    # Iterate over triples in lexicographic order
    for a in range(n):
        for b in range(a+1, n):
            if b not in adj[a]:
                continue
            for c in range(b+1, n):
                if c in adj[a] and c in adj[b]:
                    print(a+1, b+1, c+1)
                    return

if __name__ == "__main__":
    main()