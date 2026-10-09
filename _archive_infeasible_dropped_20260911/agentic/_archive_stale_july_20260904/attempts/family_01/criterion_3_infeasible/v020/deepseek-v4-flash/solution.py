import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [set() for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # For each edge (u, v), find the smallest w > v such that w is adjacent to both u and v
    # Since we need lexicographically smallest (a, b, c), we iterate a from 1 to n
    for a in range(1, n + 1):
        # For each b > a that is adjacent to a
        for b in range(a + 1, n + 1):
            if b not in adj[a]:
                continue
            # Now find smallest c > b such that c is adjacent to both a and b
            # We can intersect adjacency lists
            # Since n <= 2000, we can just iterate
            for c in range(b + 1, n + 1):
                if c in adj[a] and c in adj[b]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()