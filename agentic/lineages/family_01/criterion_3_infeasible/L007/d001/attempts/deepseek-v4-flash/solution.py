import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [set() for _ in range(n)]
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    best = None
    # Sort edges for deterministic order if needed, but we'll just compare lexicographically
    for u, v in edges:
        # find common neighbors
        if len(adj[u]) > len(adj[v]):
            u, v = v, u
        for w in adj[u]:
            if w in adj[v]:
                # triangle found
                triple = sorted([u, v, w])
                if best is None or triple < best:
                    best = triple
    # Output 1-based indexing
    print(best[0]+1, best[1]+1, best[2]+1)

if __name__ == "__main__":
    main()