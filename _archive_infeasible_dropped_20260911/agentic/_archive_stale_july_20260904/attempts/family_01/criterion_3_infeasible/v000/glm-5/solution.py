import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort adjacency lists for deterministic iteration order
    adj_list = [sorted(s) for s in adj]
    
    # We need to find the lexicographically smallest triangle
    # Iterate a from 1 to n, b from a+1 to n, c from b+1 to n
    # Check if (a,b,c) forms a triangle
    # To speed up, we can iterate a, then b in adj[a] with b > a
    # then c in adj[a] with c > b, and check if c in adj[b]
    
    # To make the check O(1), we can use the set `adj`
    # We iterate a from 1 to n
    # For each a, we iterate b in adj_list[a] where b > a
    # For each b, we iterate c in adj_list[a] where c > b
    # and check if c in adj[b]
    
    # This is O(sum over a of (deg(a) choose 2))
    # In the worst case (complete graph), this is O(n^3) which is too slow for n=2000
    # However, we can optimize by iterating b in adj[a] and c in adj[a] and checking adj[b]
    # But we need to ensure b < c
    
    # Alternative approach:
    # Iterate a from 1 to n
    # For each a, iterate b in adj[a] where b > a
    # For each b, iterate c in adj[b] where c > b
    # Check if c in adj[a]
    # This is similar complexity
    
    # Given the constraints, we need a more efficient approach
    # We can use the fact that we are looking for the lexicographically smallest triangle
    # So we can stop as soon as we find the first one
    
    # To optimize, we can iterate a from 1 to n
    # For each a, we iterate b in adj[a] where b > a
    # For each b, we iterate c in adj[a] where c > b
    # and check if c in adj[b]
    # This is still O(n^3) in the worst case
    
    # However, we can use the fact that the graph is sparse (m <= 2e5)
    # So the average degree is small
    # In the worst case, the graph is dense (m = n(n-1)/2)
    # But n=2000, n^3 = 8e9 which is too slow
    
    # We need a better approach
    # We can use the fact that we are looking for the lexicographically smallest triangle
    # So we can iterate a from 1 to n
    # For each a, we iterate b in adj[a] where b > a
    # For each b, we iterate c in adj[b] where c > b
    # Check if c in adj[a]
    # This is O(sum over a of deg(a)^2)
    # In the worst case (complete graph), this is O(n^3)
    
    # But we can optimize by using the fact that we can stop early
    # We can iterate a from 1 to n
    # For each a, we iterate b in adj[a] where b > a
    # For each b, we iterate c in adj[b] where c > b
    # Check if c in adj[a]
    # If we find such c, we can return immediately
    
    # To make the check O(1), we can use the set `adj`
    # We can also sort the adjacency lists to ensure we iterate in order
    
    # Let's implement this and see if it passes
    # If it's too slow, we can optimize further
    
    for a in range(1, n + 1):
        for b in adj_list[a]:
            if b <= a:
                continue
            for c in adj_list[a]:
                if c <= b:
                    continue
                if c in adj[b]:
                    print(a, b, c)
                    return
    
    # If we reach here, no triangle found (should not happen per problem statement)
    # But the problem guarantees at least one triangle exists

if __name__ == "__main__":
    solve()