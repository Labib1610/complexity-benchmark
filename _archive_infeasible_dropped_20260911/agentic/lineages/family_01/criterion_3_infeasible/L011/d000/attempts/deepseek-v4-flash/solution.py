import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [set() for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))

    best = None
    for u, v in edges:
        # Check common neighbors of u and v
        if len(adj[u]) > len(adj[v]):
            small, large = v, u
        else:
            small, large = u, v
        for w in adj[small]:
            if w in adj[large]:
                tri = tuple(sorted((u, v, w)))
                if best is None or tri < best:
                    best = tri
        if best is not None and best[0] == 1:
            # Early exit if we found smallest possible a
            pass

    print(*best)

if __name__ == "__main__":
    main()