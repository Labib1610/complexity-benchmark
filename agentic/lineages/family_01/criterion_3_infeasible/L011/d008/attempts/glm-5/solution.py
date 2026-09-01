import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [0] * (n + 1)
    deg = [0] * (n + 1)
    edges = []
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
        deg[u] += 1
        deg[v] += 1
    
    # Sort vertices by degree for the low-degree algorithm
    vertices = list(range(1, n + 1))
    vertices.sort(key=lambda x: deg[x])
    
    # Case 1: at least one vertex has degree < 64
    # We look for a triangle where the middle vertex (by degree) has degree < 64
    for v in vertices:
        if deg[v] >= 64:
            break
        # v is the middle vertex by degree order
        # Neighbors of v with degree < deg[v] are "lower"
        # Neighbors of v with degree >= deg[v] are "higher"
        lower = []
        higher = []
        for u in range(1, n + 1):
            if (adj[v] >> u) & 1:
                if deg[u] < deg[v] or (deg[u] == deg[v] and u < v):
                    lower.append(u)
                else:
                    higher.append(u)
        
        # For each pair of higher neighbors, check if they are connected
        # If they are, (lower_neighbor, v, higher_neighbor) forms a triangle
        # where v is the middle vertex by degree order
        for i in range(len(higher)):
            a = higher[i]
            for j in range(i + 1, len(higher)):
                b = higher[j]
                if (adj[a] >> b) & 1:
                    # Found a triangle, v is the middle vertex
                    # Check if it's an unresolvable bottleneck
                    # Count edges among the three vertices
                    cnt = 0
                    if (adj[a] >> b) & 1:
                        cnt += 1
                    if (adj[a] >> v) & 1:
                        cnt += 1
                    if (adj[b] >> v) & 1:
                        cnt += 1
                    # Unresolvable bottleneck iff cnt is odd (1 or 3)
                    if cnt & 1:
                        result = sorted([a, b, v])
                        print(f"{result[0]} {result[1]} {result[2]}")
                        return
        
        # For each pair of lower neighbors, check if they are connected
        for i in range(len(lower)):
            a = lower[i]
            for j in range(i + 1, len(lower)):
                b = lower[j]
                if (adj[a] >> b) & 1:
                    # Found a triangle, v is the middle vertex
                    cnt = 0
                    if (adj[a] >> b) & 1:
                        cnt += 1
                    if (adj[a] >> v) & 1:
                        cnt += 1
                    if (adj[b] >> v) & 1:
                        cnt += 1
                    if cnt & 1:
                        result = sorted([a, b, v])
                        print(f"{result[0]} {result[1]} {result[2]}")
                        return
    
    # Case 2: all vertices have degree >= 64
    # This means m >= 64*n/2 = 32*n
    # For n <= 2000, m >= 32*2000 = 64000, but m <= 2*10^5
    # The graph is dense, so we can find triangles efficiently
    # We iterate over edges and check common neighbors
    # Since deg >= 64, we use the edge iteration approach
    
    # For dense graphs, iterate over edges and find common neighbors
    # To find the lexicographically smallest triangle, we can iterate edges in order
    # and for each edge (u, v), find common neighbors w > v
    
    # But we need the lexicographically smallest unresolvable bottleneck
    # So we iterate a from 1 to n, then b from a+1 to n, then c from b+1 to n
    # But this is O(n^3) which is too slow for n=2000
    
    # Instead, we use the fact that in a dense graph, most triangles are unresolvable
    # We iterate over edges (u, v) with u < v, and find common neighbors w > v
    # The first such triangle we find might not be the lexicographically smallest
    # So we need to be more careful
    
    # Actually, let's think about this differently
    # We iterate a from 1 to n
    # For each a, we look at all pairs (b, c) where b > a, c > b, and both are neighbors of a
    # We check if (b, c) is an edge
    # The first valid triangle we find is the lexicographically smallest
    
    # But this is still O(sum of deg(a)^2) which could be large
    
    # However, since all degrees >= 64, and m <= 2*10^5, n <= 2000
    # The average degree is 2m/n <= 2*2*10^5/2000 = 200
    # So sum of deg(a)^2 could be up to n * (200)^2 = 2000 * 40000 = 8*10^7
    # This might be acceptable
    
    # Actually, let's be smarter. We iterate a from 1 to n.
    # For each a, we get its neighbors that are > a.
    # We sort them and iterate over pairs.
    # But we can optimize by only checking pairs where both are neighbors of a.
    
    # Actually, for the dense case, let's just iterate over all edges and find triangles
    # Then collect all unresolvable bottlenecks and find the minimum
    
    # But that could be too many triangles
    
    # Let me think again...
    # In the dense case, we can iterate a from 1 to n
    # For each a, iterate over edges (b, c) where b > a and c > a and both are neighbors of a
    # We can do this by looking at the adjacency of a and finding edges among neighbors
    
    # Since we want the lexicographically smallest, we iterate a from 1 to n
    # For each a, we want the smallest b > a such that there exists c > b with (a,b), (a,c), (b,c) all edges
    # and the triangle is an unresolvable bottleneck
    
    # For a fixed a, we iterate b from a+1 to n
    # If (a, b) is an edge, we look for c > b such that (a, c) and (b, c) are edges
    # and the triangle is unresolvable
    
    # The number of edges is m, and for each edge (a, b), we look at common neighbors > b
    # The total work is sum over edges of (number of common neighbors > b)
    # This is at most sum over edges of min(deg(a), deg(b))
    # In the worst case, this is m * max_deg = 2*10^5 * 2000 = 4*10^8, too slow
    
    # But we can optimize: for each edge (a, b), we iterate over the smaller adjacency list
    # and check if the neighbor is in the other adjacency list and > b
    
    # Actually, let's just try the straightforward approach and see if it's fast enough
    # given the constraints
    
    # Let me reconsider the problem structure
    # An unresolvable bottleneck is a triangle with 1 or 3 edges
    # A triangle with 2 edges is not possible (if a-b and a-c are edges, and b-c is not, that's 2 edges)
    # Wait, actually the three vertices don't need to form a triangle
    # They just need to have 1 or 3 edges among them
    
    # So we're looking for triples (a, b, c) with exactly 1 or exactly 3 edges among them
    # And we want the lexicographically smallest such triple
    
    # This changes things! We don't need a triangle necessarily
    
    # For 3 edges: it's a triangle
    # For 1 edge: exactly one pair is connected
    
    # Let me reconsider the algorithm
    # For the 1-edge case, we can iterate over edges (a, b) and find c > b such that
    # c is not connected to a and not connected to b
    # For the 3-edge case, we find triangles
    
    # The 1-edge case is easier for sparse graphs
    # The 3-edge case is easier for dense graphs
    
    # Actually, for the 1-edge case:
    # Iterate a from 1 to n
    # For each a, iterate b from a+1 to n
    # If (a, b) is an edge, find the smallest c > b such that (a, c) and (b, c) are not edges
    # If (a, b) is not an edge, we need to find c > b such that exactly one of (a, c), (b, c) is an edge
    
    # This is getting complicated. Let me think of a unified approach.
    
    # Actually, let's just iterate a from 1 to n, b from a+1 to n, c from b+1 to n
    # and check the edge count. But O(n^3) is too slow for n=2000.
    
    # Let me think about this more carefully.
    # We want the lexicographically smallest (a, b, c) with edge count 1 or 3.
    
    # For a fixed a, we want the smallest b > a, and then smallest c > b.
    # 
    # Case 1: edge count = 1
    #   Subcase 1a: (a, b) is the only edge. Need c > b with (a, c) and (b, c) not edges.
    #   Subcase 1b: (a, c) is the only edge. Need (a, b) and (b, c) not edges.
    #   Subcase 1c: (b, c) is the only edge. Need (a, b) and (a, c) not edges.
    # 
    # Case 2: edge count = 3 (triangle)
    #   All three edges present.
    
    # For a fixed a and b:
    #   If (a, b) is an edge:
    #     We need c > b such that:
    #       - (a, c) and (b, c) are both edges (triangle, count=3), or
    #       - (a, c) and (b, c) are both non-edges (count=1)
    #   If (a, b) is not an edge:
    #     We need c > b such that exactly one of (a, c), (b, c) is an edge (count=1)
    
    # For the triangle case, we need common neighbors of a and b that are > b.
    # For the count=1 case with (a,b) being an edge, we need c > b that's a non-neighbor of both.
    # For the count=1 case with (a,b) not being an edge, we need c > b that's a neighbor of exactly one.
    
    # The challenge is doing this efficiently.
    
    # Let me try a different approach: iterate over all triples in a smart order.
    # We iterate a from 1 to n. For each a, we iterate b from a+1 to n.
    # For each (a, b), we compute the set of valid c > b.
    # If non-empty, we take the smallest c and we're done (since we iterate in order).
    
    # The key question is: how do we efficiently find if there exists a valid c > b?
    
    # For the triangle case (count=3): c must be a common neighbor of a and b, with c > b.
    #   We can precompute for each pair (a, b) the common neighbors, but that's O(n^2) space.
    #   Alternatively, for each edge (a, b), we iterate over neighbors of a and check if they're neighbors of b.
    
    # For the count=1 case:
    #   If (a, b) is an edge: c > b, c not neighbor of a, c not neighbor of b.
    #     This means c is in the complement of (neighbors(a) ∪ neighbors(b)) ∪ {a, b}, and c > b.
    #     If |neighbors(a) ∪ neighbors(b)| < n - 2, there exists such c.
    #     But we need c > b specifically.
    #   If (a, b) is not an edge: c > b, c is neighbor of exactly one of a, b.
    #     c ∈ (neighbors(a) △ neighbors(b)) and c > b.
    
    # This is getting complex. Let me try to implement a solution that works for both sparse and dense cases.
    
    # Given the constraints (n <= 2000, m <= 2*10^5), let me try the following:
    # 1. For each a from 1 to n:
    #    For each b from a+1 to n:
    #      Check if there exists c > b forming an unresolvable bottleneck with a, b.
    #      If yes, output and return.
    # 
    # The check for existence of c:
    #   Let e_ab = 1 if (a,b) is an edge, else 0
    #   We need c > b such that e_ab + e_ac + e_bc is odd (1 or 3).
    #   If e_ab = 1: need e_ac + e_bc even (0 or 2), so e_ac = e_bc.
    #     - Both 1: triangle, c is common neighbor
    #     - Both 0: c is non-neighbor of both
    #   If e_ab = 0: need e_ac + e_bc odd (1), so exactly one of e_ac, e_bc is 1.
    #     - c is neighbor of exactly one of a, b
    
    # For the triangle subcase, we can check common neighbors > b.
    # For the non-neighbor subcase, we need to find c > b not adjacent to a or b.
    # For the exactly-one subcase, we need c > b adjacent to exactly one of a, b.
    
    # Let me think about the complexity.
    # For each (a, b) pair, the check could take O(n) in the worst case.
    # Total: O(n^3) which is 8*10^9, too slow.
    
    # But we can optimize:
    # For the triangle case, we only check if (a, b) is an edge, and then look at common neighbors.
    # For the non-neighbor case (e_ab=1, need c non-neighbor of both), we can check if
    #   the number of vertices > b that are non-neighbors of both is > 0.
    #   This is (n - b) - |neighbors(a) ∩ {b+1..n}| - |neighbors(b) ∩ {b+1..n}| + |common neighbors ∩ {b+1..n}|
    #   Hmm, this is getting complicated.
    
    # Let me try a different approach.
    # Since we want the lexicographically smallest, and we iterate a, b, c in order,
    # we can try to find the answer quickly by checking promising candidates first.
    
    # Actually, let me just implement the O(n^2 * sqrt(m)) or similar approach.
    
    # Alternative: for each a, precompute the adjacency bitset.
    # Then for each pair (a, b), we can compute things using bitset operations.
    # But n=2000 means bitsets of 2000 bits, and Python handles this with integers.
    
    # Let me try this approach:
    # For each a from 1 to n:
    #   For each b from a+1 to n:
    #     Compute the set of valid c > b using bitset operations.
    #     If non-empty, find the smallest c and output.
    
    # The bitset operations:
    #   adj[a] is a bitset where bit i is set if (a, i) is an edge.
    #   For c > b, we use a mask: mask = ((1 << (n+1)) - 1) ^ ((1 << (b+1)) - 1)
    #   This gives us bits b+1, b+2, ..., n set.
    #   
    #   If e_ab = 1 (bit b is set in adj[a]):
    #     Triangle: adj[a] & adj[b] & mask
    #     Non-neighbor: ~(adj[a] | adj[b]) & mask & valid_range
    #     Valid c = (adj[a] & adj[b] & mask) | (~(adj[a] | adj[b]) & mask & valid_range)
    #   If e_ab = 0:
    #     Exactly one: (adj[a] ^ adj[b]) & mask
    
    # Wait, but adj[a] includes all neighbors, including those <= b.
    # We need to mask to only consider c > b.
    # Also, ~(adj[a] | adj[b]) would include a and b themselves, and vertices <= b.
    # So we need to be careful with the mask.
    
    # Let me define:
    #   full_mask = (1 << (n + 1)) - 1  # bits 0 to n
    #   range_mask = full_mask & ~((1 << (b + 1)) - 1)  # bits b+1 to n
    #   But we also need to exclude a and b from the non-neighbor case.
    #   Since a < b < c, and c > b, a and b are already excluded by range_mask.
    
    # So:
    #   If e_ab = 1:
    #     valid_c = ((adj[a] & adj[b]) | (~(adj[a] | adj[b]) & full_mask)) & range_mask
    #   If e_ab = 0:
    #     valid_c = (adj[a] ^ adj[b]) & range_mask
    
    # Then if valid_c != 0, the smallest c is the position of the lowest set bit.
    
    # The complexity is O(n^2) bitset operations, each on O(n) bits.
    # With n=2000, each bitset fits in a Python integer (about 250 bytes).
    # Bitset operations on 2000-bit integers are fast.
    # Total: O(n^2) = 4*10^6 operations, each taking O(n/64) time, so about 6*10^4 * 4*10^6 = 2.4*10^11...
    # No wait, Python integer operations on 2000-bit integers are O(1) effectively for our purposes.
    # Actually, Python big integer operations take time proportional to the number of words.
    # For 2000 bits, that's about 32 64-bit words, so each operation is O(32).
    # Total: 4*10^6 * 32 = 1.28*10^8, which should be acceptable.
    
    # Let me implement this.
    
    full_mask = (1 << (n + 1)) - 1
    
    for a in range(1, n + 1):
        adj_a = adj[a]
        for b in range(a + 1, n + 1):
            adj_b = adj[b]
            range_mask = full_mask & ~((1 << (b + 1)) - 1)
            
            if (adj_a >> b) & 1:  # (a, b) is an edge
                # Need c > b with (e_ac + e_bc) even
                # Triangle: adj_a & adj_b
                # Non-neighbor: ~(adj_a | adj_b)
                valid_c = ((adj_a & adj_b) | (~(adj_a | adj_b) & full_mask)) & range_mask
            else:  # (a, b) is not an edge
                # Need c > b with exactly one of e_ac, e_bc = 1
                valid_c = (adj_a ^ adj_b) & range_mask
            
            if valid_c:
                # Find the lowest set bit
                c = (valid_c & -valid_c).bit_length() - 1
                print(f"{a} {b} {c}")
                return

solve()