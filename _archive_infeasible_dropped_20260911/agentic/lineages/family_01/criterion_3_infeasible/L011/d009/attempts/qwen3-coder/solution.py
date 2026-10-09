import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Read operations
    operations = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-based indexing
        v = int(data[index+1]) - 1
        operations.append((u, v))
        index += 2
    
    # For each sequence, keep track of which operations it participates in
    seq_ops = [set() for _ in range(n)]
    for i, (u, v) in enumerate(operations):
        seq_ops[u].add(i)
        seq_ops[v].add(i)
    
    # We need to find a, b, c such that F(a,b) + F(b,c) + F(c,a) = 3m + 6
    # Let's analyze what this means:
    # At each position k, if both sequences have 1, score is 3. Otherwise, score is 1.
    # So total score = 3*(number of positions where both have 1) + 1*(m - that count)
    # = 3*count + (m - count) = 2*count + m
    # We want 2*count_ab + m + 2*count_bc + m + 2*count_ca + m = 3m + 6
    # => 2*(count_ab + count_bc + count_ca) + 3m = 3m + 6
    # => count_ab + count_bc + count_ca = 3
    
    # So we need three sequences a,b,c such that they share exactly 3 positions where both are 1.
    # Since each operation sets exactly two sequences to 1 at that position,
    # count_ab is just the number of operations involving both a and b.
    # So we need pairs (a,b), (b,c), (c,a) to appear together in exactly 3 operations.
    
    # But let's think differently. 
    # In our case, since every operation involves exactly 2 distinct sequences,
    # and no pair appears twice, count_ab is exactly the number of times both a and b appear in the same operation.
    # Which is 1 if there's an operation on (a,b), 0 otherwise.
    # Wait, that's not right. Each operation creates a pair.
    # So count_ab = 1 if there exists an operation (a,b) or (b,a), 0 otherwise.
    # But we have m operations, so we can compute count_ab directly.
    
    # Actually, let's re-read:
    # For position k, operation k sets S_u[k]=1 and S_v[k]=1.
    # So for sequences i,j: count of positions where both are 1 is the number of operations k where {u,v} = {i,j}.
    # But "No two operations will specify the exact same pair of indices"
    # So count_ij is 1 if there's an operation on pair {i,j}, 0 otherwise.
    # Therefore, for any triple a,b,c:
    # count_ab + count_bc + count_ca is the number of edges between them in the graph of operations.
    # We want this sum to be 3.
    # That means we want a triangle in the graph - three nodes with edges between each pair.
    
    # So the problem reduces to: find a triangle in the graph formed by the m edges,
    # and return the lexicographically smallest such triple.
    
    # Build adjacency information
    adj = [set() for _ in range(n)]
    edge_list = []
    for u, v in operations:
        adj[u].add(v)
        adj[v].add(u)
        edge_list.append((u, v))
    
    # For efficiency, let's create a mapping from pairs to whether they exist
    edge_exists = set()
    for u, v in operations:
        if u > v:
            u, v = v, u
        edge_exists.add((u, v))
    
    # Now we look for triangles
    best = None
    
    # Check all triples in lexicographical order
    for a in range(n):
        for b in range(a+1, n):
            # If no edge between a and b, skip
            if b not in adj[a]:
                continue
            for c in range(b+1, n):
                # Check if we have edges (a,b), (b,c), (a,c)
                if c not in adj[a]:
                    continue
                if c not in adj[b]:
                    continue
                # Found a triangle
                return print(a+1, b+1, c+1) # Convert back to 1-based
    
    # Should never reach here given the problem guarantees a solution
    assert False

if __name__ == "__main__":
    main()