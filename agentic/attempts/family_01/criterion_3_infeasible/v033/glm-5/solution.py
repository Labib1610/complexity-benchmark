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
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort edges lexicographically to find the smallest triangle first
    edges.sort()
    
    for u, v in edges:
        # Find common neighbors w where w > max(u, v) to maintain order
        # We need to check if w is connected to both u and v
        # To find lexicographically smallest triangle, we iterate w in order
        # Since edges are sorted by u then v, and we check w > v,
        # the first triangle found will be lexicographically smallest
        if len(adj[u]) < len(adj[v]):
            smaller, larger = adj[u], adj[v]
        else:
            smaller, larger = adj[v], adj[u]
        
        for w in smaller:
            if w > v and w in larger:
                print(u, v, w)
                return
    
    # Fallback: check all triples (should not reach here per problem guarantee)
    for a in range(1, n + 1):
        for b in adj[a]:
            if b <= a:
                continue
            for c in adj[b]:
                if c <= b:
                    continue
                if c in adj[a]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()