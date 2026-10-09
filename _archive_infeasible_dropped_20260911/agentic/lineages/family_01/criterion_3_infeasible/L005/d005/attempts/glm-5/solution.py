import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    deg = [0] * (n + 1)
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        deg[u] += 1
        deg[v] += 1
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort nodes by degree descending
    nodes = list(range(1, n + 1))
    nodes.sort(key=lambda x: -deg[x])
    
    # Iterate over pairs (u, v) in order of decreasing deg[u] + deg[v]
    # To find lexicographically smallest, we iterate u from 1 to n-1, v from u+1 to n
    # but we want to find the answer quickly. We use the heuristic to check high-degree pairs first.
    # Once found, we continue to search for lexicographically smaller ones.
    
    best = None
    
    # We'll iterate u from 1 to n-1, v from u+1 to n
    # But to optimize, we might want to check promising pairs first.
    # However, to ensure correctness and find the lexicographically smallest,
    # we can iterate in order and update best.
    
    # Optimization: precompute sorted neighbors for intersection
    # But for n=2000, O(n^2) pairs is 4e6, and intersection is O(n) worst case -> 8e9 operations too slow.
    # We need to use the heuristic to break early or limit checks.
    
    # Let's use the heuristic: check pairs in order of decreasing deg[u] + deg[v]
    # We'll create a list of pairs sorted by -deg[u]-deg[v]
    # Then iterate and update best.
    
    pairs = []
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            pairs.append((i, j))
    
    # Sort pairs by -deg[u] - deg[v]
    pairs.sort(key=lambda x: -(deg[x[0]] + deg[x[1]]))
    
    for u, v in pairs:
        if best is not None:
            # If current pair is lexicographically larger than best, skip
            if u > best[0]:
                continue
            if u == best[0] and v > best[1]:
                continue
        
        # Check if u and v are connected
        if v not in adj[u]:
            continue
        
        # Find common neighbors
        # Iterate over the smaller adjacency list
        if len(adj[u]) < len(adj[v]):
            common = adj[u]
            other = adj[v]
        else:
            common = adj[v]
            other = adj[u]
        
        for w in common:
            if w <= v:
                continue
            if w in other:
                # Check condition
                # L_u + L_v + L_w + (m - (L_u + L_v + L_w - cnt_uv - cnt_uw - cnt_vw + cnt_uvw)) == m + 3
                # cnt_uv = 1, cnt_uw = 1, cnt_vw = 1, cnt_uvw = 0
                # So condition simplifies to L_u + L_v + L_w - 3 == m + 3 - m = 3
                # => L_u + L_v + L_w == 6
                if deg[u] + deg[v] + deg[w] == 6:
                    if best is None or (u, v, w) < best:
                        best = (u, v, w)
    
    print(f"{best[0]} {best[1]} {best[2]}")

if __name__ == "__main__":
    solve()