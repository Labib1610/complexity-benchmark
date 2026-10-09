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

    # Try to find triangle with small lexicographic order
    found = None
    for u in range(n):
        for v in adj[u]:
            if v < u:
                continue
            common = adj[u] & adj[v]
            if common:
                w = min(common)
                candidate = sorted([u+1, v+1, w+1])
                if found is None or candidate < found:
                    found = candidate
        if found is not None:
            # early exit possible? Not necessarily minimal, so keep scanning.
            pass

    print(*found)

if __name__ == "__main__":
    main()