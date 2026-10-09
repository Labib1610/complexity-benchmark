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
    
    # Try to find a triangle
    for u, v in edges:
        # Intersection of neighbors of u and v
        common = adj[u] & adj[v]
        if common:
            w = min(common)
            a, b, c = sorted([u, v, w])
            print(a, b, c)
            return

if __name__ == "__main__":
    main()