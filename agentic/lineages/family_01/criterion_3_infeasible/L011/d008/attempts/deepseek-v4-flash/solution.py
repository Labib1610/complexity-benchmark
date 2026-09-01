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
    
    # Try to find lexicographically smallest triangle
    for u in range(n):
        for v in adj[u]:
            if v > u:
                common = adj[u] & adj[v]
                if common:
                    w = min(common)
                    if w > v:
                        print(u + 1, v + 1, w + 1)
                        return

if __name__ == "__main__":
    main()