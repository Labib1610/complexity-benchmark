import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [set() for _ in range(n + 1)]
    edges = set()
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].add(v)
        adj[v].add(u)
        edges.add((u, v))
        edges.add((v, u))
    
    # Iterate over a < b < c
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if (a, b) not in edges:
                continue
            # Find common neighbor c > b
            for c in range(b + 1, n + 1):
                if (a, c) in edges and (b, c) in edges:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()