import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [set() for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].add(v)
        adj[v].add(u)
    
    for u in range(1, n+1):
        # neighbors sorted
        neigh = sorted(adj[u])
        for i in range(len(neigh)):
            v = neigh[i]
            if v <= u:
                continue
            for j in range(i+1, len(neigh)):
                w = neigh[j]
                if w <= v:
                    continue
                if w in adj[v]:
                    print(u, v, w)
                    return

if __name__ == "__main__":
    main()