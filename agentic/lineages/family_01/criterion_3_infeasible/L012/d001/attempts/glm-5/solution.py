import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].add(v)
        adj[v].add(u)
    
    # Find lexicographically smallest triad (a, b, c) with a < b < c
    # where all three edges (a,b), (a,c), (b,c) exist.
    # Iterate a from 1 to n-2, then b from a+1 to n-1, then check c candidates.
    
    for a in range(1, n - 1):
        # Candidates for b must be > a and adjacent to a
        # To ensure lexicographic order, we iterate b in increasing order
        # We need to iterate b from a+1 to n, but only if edge (a,b) exists
        # Since we want smallest b, we sort the neighbors of a that are > a
        
        neighbors_a = adj[a]
        # Create list of valid b candidates (b > a and b in neighbors_a)
        valid_b = []
        # Iterating through neighbors_a is efficient if degree is small
        # But we need them sorted. 
        # Since we iterate a from 1 upwards, and for each a we need sorted b,
        # we can collect and sort.
        
        # Optimization: only consider b > a
        for neighbor in neighbors_a:
            if neighbor > a:
                valid_b.append(neighbor)
        
        valid_b.sort()
        
        for b in valid_b:
            # Now we need c such that c > b, c in neighbors_a, and c in neighbors_b
            # To find smallest c, we iterate c from b+1 to n
            # c must be in neighbors_a (which is neighbors_a set)
            # c must be in neighbors_b (which is adj[b] set)
            
            neighbors_b = adj[b]
            
            # We can iterate candidates for c from the intersection of neighbors_a and neighbors_b
            # but we must ensure c > b.
            # Since we want the smallest c, we should iterate c in increasing order.
            # We can iterate c from b+1 to n and check membership.
            # However, checking membership is O(1).
            # The total complexity depends on the number of (a,b) pairs and the range of c.
            
            # Let's iterate c from b+1 to n.
            # To optimize, we iterate through the smaller set between neighbors_a and neighbors_b
            # and check if the element is in the other set and > b.
            # Then we take the minimum such c.
            
            # Since we want the first c, we can just iterate c from b+1 to n.
            # But if n is large and degrees are small, this is inefficient.
            # Better to iterate through intersection.
            
            # Iterate through neighbors_a (or neighbors_b) and find candidates for c
            # Let's pick the smaller set to iterate
            if len(neighbors_a) < len(neighbors_b):
                set_to_iterate = neighbors_a
                other_set = neighbors_b
            else:
                set_to_iterate = neighbors_b
                other_set = neighbors_a
            
            # We need smallest c > b that is in both sets
            # Since we want smallest c, we should collect valid c's and take min
            # But we can just iterate and find the first one if we iterate in sorted order
            
            # However, sets are not sorted. We can't iterate in sorted order efficiently without sorting.
            # But we only need the *smallest* c.
            # So we can scan the set and keep track of the minimum valid c.
            
            min_c = n + 1 # Initialize with a value larger than any possible c
            
            for c_candidate in set_to_iterate:
                if c_candidate > b and c_candidate in other_set:
                    if c_candidate < min_c:
                        min_c = c_candidate
                        # We can't break early because we need the minimum
                        # But if we found c = b+1, that's the absolute minimum possible for this b
                        # so we can break.
                        if min_c == b + 1:
                            break
            
            if min_c <= n:
                # Found the smallest c for this (a, b)
                print(a, b, min_c)
                return

if __name__ == '__main__':
    solve()