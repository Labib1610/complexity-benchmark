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

    # Check edges in sorted order for lexicographically smallest triangle
    edges.sort()
    for u, v in edges:
        # For the edge (u, v), find a common neighbor w > v for lexicographic order
        common = adj[u] & adj[v]
        for w in sorted(common):
            if w > v:
                print(u, v, w)
                return

if __name__ == "__main__":
    main()