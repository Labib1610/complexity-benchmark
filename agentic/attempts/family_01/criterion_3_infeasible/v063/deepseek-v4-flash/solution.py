import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    adj_set = [set() for _ in range(n+1)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        adj_set[u].add(v)
        adj_set[v].add(u)
    
    # Sort adjacency lists for deterministic order
    for i in range(1, n+1):
        adj[i].sort()
    
    # Search for triangle
    for a in range(1, n+1):
        for b in adj[a]:
            if b <= a:
                continue
            for c in adj[b]:
                if c <= b:
                    continue
                if c in adj_set[a]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()