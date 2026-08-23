import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Sort edges to ensure we find lexicographically smallest triangle first
    edges.sort()
    
    # Strategy 1: Check edges for common neighbors
    # This is efficient if graph is dense
    for u, v in edges:
        # Iterate through neighbors of the smaller degree vertex
        if len(adj[u]) > len(adj[v]):
            u, v = v, u
        for w in adj[u]:
            if w != v and w in adj[v]:
                # Found triangle u, v, w
                res = sorted([u, v, w])
                print(res[0], res[1], res[2])
                return
    
    # Strategy 2: Check all triples (should not reach here if graph has triangle)
    # This is a fallback for correctness
    for i in range(1, n + 1):
        for j in adj[i]:
            if j > i:
                for k in adj[j]:
                    if k > j and k in adj[i]:
                        print(i, j, k)
                        return

if __name__ == '__main__':
    solve()