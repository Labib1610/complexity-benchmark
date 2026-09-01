import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    adj = [set() for _ in range(n + 1)]
    degrees = [0] * (n + 1)
    edges = []

    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].add(v)
        adj[v].add(u)
        degrees[u] += 1
        degrees[v] += 1
        edges.append((u, v))

    # Strategy 1: Find a triangle (det = 4)
    # Sort nodes by degree to optimize search
    nodes = list(range(1, n + 1))
    nodes.sort(key=lambda x: degrees[x])
    
    # We iterate through nodes in sorted order to find the lexicographically smallest valid triplet.
    # Since we need smallest a, then b, then c, we iterate a from 1 to n.
    # For a fixed a, we iterate b from a+1 to n.
    # To check if a-b-c is a triangle, we need to check if c is in adj[a] and adj[b].
    # We iterate c from b+1 to n.
    # This naive iteration is O(n^3) worst case.
    # Optimization: For a fixed a, we iterate b > a. If edge (a,b) exists, we check intersection of adj[a] and adj[b] for any c > b.
    # To ensure we find the smallest triplet, we must check candidates in order.
    
    # Let's try to find a triangle first.
    # If we find any triangle, we can potentially use it to bound the search for the lexicographically smallest one.
    # However, finding *any* triangle fast is useful to know if we can fallback to a simpler logic.
    
    # Optimized Triangle Finding (Chiba-Nishizeki style):
    # Sort vertices by degree descending for processing, but we need to output based on labels.
    # The problem asks for smallest labels.
    # Let's stick to the label order for the outer loops to guarantee the first found is the correct one,
    # but use degree ordering to optimize the inner checks.
    
    # Heuristic: If degrees are small, O(sum(deg^2)) is small.
    # If degrees are large, the graph is dense, and we find a triangle quickly.
    
    found_a, found_b, found_c = -1, -1, -1
    
    # We iterate 'a' from 1 to n
    for a in range(1, n + 1):
        # We need 'b' > a
        # Collect neighbors of 'a' that are greater than 'a'
        neighbors_a = [v for v in adj[a] if v > a]
        neighbors_a.sort() # Sort to ensure we check b in increasing order
        
        for b in neighbors_a:
            # We need 'c' > b
            # Check if there exists c in adj[a] and adj[b] such that c > b
            # We iterate through neighbors of 'a' that are > b
            # and check if they are in adj[b]
            
            # Optimization: iterate through the smaller adjacency list for intersection
            # We need c > b.
            # Candidates are neighbors of 'a' > b.
            # We iterate these candidates and check presence in adj[b].
            
            # To ensure smallest 'c', we must check candidates in increasing order.
            # neighbors_a is sorted. We iterate from start.
            # Actually, we can just iterate neighbors_a again.
            
            for c in neighbors_a:
                if c > b:
                    if c in adj[b]:
                        # Found a triangle a, b, c
                        # Since we iterate a in increasing order, then b, then c,
                        # this is the lexicographically smallest triangle.
                        print(f"{a} {b} {c}")
                        return

    # Strategy 2: If no triangle found, look for a path a-b-c (det = -2)
    # We need the lexicographically smallest path.
    # Iterate a from 1 to n.
    # Iterate b from a+1 to n.
    # Iterate c from b+1 to n.
    # Check if exactly two edges exist.
    # This is O(n^3) which might be too slow for n=2000 if the graph is very sparse.
    # However, if no triangle exists, the graph is triangle-free.
    # A triangle-free graph can have O(n^2) edges (e.g. complete bipartite).
    # But if it has O(n^2) edges, we would have found a triangle (dense graph).
    # Triangle-free graphs with many edges have specific structure (bipartite).
    # If edges are few, O(n^3) might pass if optimized?
    # Actually, if no triangle, we just need to find the first path.
    
    # Let's just run the naive check for paths.
    # To optimize, we can iterate a, then b > a.
    # If edge (a,b) exists, we need c > b such that (a,c) or (b,c) exists, but not both.
    # If edge (a,b) does not exist, we need c > b such that exactly one of (a,c) or (b,c) exists.
    
    # Since we returned only if triangle found, we proceed to path finding.
    # This part is reached only if no triangle exists.
    # In a graph with no triangles, finding a path is guaranteed.
    
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            for c in range(b + 1, n + 1):
                # Count edges
                cnt = 0
                if b in adj[a]: cnt += 1
                if c in adj[a]: cnt += 1
                if c in adj[b]: cnt += 1
                if cnt == 2:
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()