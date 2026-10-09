import sys

def solve():
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
    
    # Sort edges by (u, v) to find lexicographically smallest triangle
    edges.sort()
    
    for u, v in edges:
        # Find common neighbor w > v to ensure a < b < c
        common = adj[u] & adj[v]
        for w in sorted(common):
            if w > v:
                print(u + 1, v + 1, w + 1)
                return

if __name__ == "__main__":
    solve()