import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [set() for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    best = None
    for u, v in edges:
        # find smallest w > v connected to both u and v
        # iterate over neighbors of u that are > v
        for w in sorted(adj[u]):
            if w > v and w in adj[v]:
                if best is None or (u, v, w) < best:
                    best = (u, v, w)
                break  # since sorted, first found is smallest for this edge
        if best is not None and u > best[0]:
            # can't improve x anymore
            break
    
    print(*best)

if __name__ == "__main__":
    main()