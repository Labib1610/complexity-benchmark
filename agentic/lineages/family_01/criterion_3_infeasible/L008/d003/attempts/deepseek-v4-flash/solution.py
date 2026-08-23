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
    
    best = None
    best_score = None
    
    for u, v in edges:
        # Find common neighbors
        common = adj[u] & adj[v]
        for w in common:
            a, b, c = sorted([u+1, v+1, w+1])
            score = a * 10**8 + b * 10**4 + c
            if best_score is None or score < best_score:
                best_score = score
                best = (a, b, c)
    
    print(*best)

if __name__ == "__main__":
    solve()