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
    
    # Sort edges by vertex order for lexicographic smallest triangle
    edges.sort()
    
    for u, v in edges:
        # Check common neighbors
        # Iterate over smaller adjacency list
        if len(adj[u]) > len(adj[v]):
            u, v = v, u
        for w in adj[u]:
            if w in adj[v]:
                # Found triangle
                a, b, c = sorted([u, v, w])
                print(a+1, b+1, c+1)
                return
    print(-1)

if __name__ == "__main__":
    solve()