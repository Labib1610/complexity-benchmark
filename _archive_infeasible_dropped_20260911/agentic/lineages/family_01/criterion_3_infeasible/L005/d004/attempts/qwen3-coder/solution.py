import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    index = 2
    edges = []
    adj = defaultdict(set)
    
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Compute degrees
    deg = [0] * (n + 1)
    for u in adj:
        deg[u] = len(adj[u])
    
    # Create edge set for O(1) lookup
    edge_set = set()
    for u, v in edges:
        if u > v:
            u, v = v, u
        edge_set.add((u, v))
    
    # Iterate through all triangles {a,b,c} with a<b<c
    # Check the condition: number of edges incident to {a,b,c} = (deg[a] + deg[b] + deg[c]) - 3
    # The number of edges incident to {a,b,c} is:
    # deg[a] + deg[b] + deg[c] - 2*(number of edges between a,b,c)
    # We want this to be equal to (deg[a] + deg[b] + deg[c]) - 3
    # So: deg[a] + deg[b] + deg[c] - 2*E_abc = deg[a] + deg[b] + deg[c] - 3
    # => 2*E_abc = 3 => E_abc = 1.5, which is impossible.
    # Wait, let's re-think.
    
    # The number of edges that involve at least one of a, b, c is:
    # Total edges incident to a, b, or c.
    # This is: deg[a] + deg[b] + deg[c] - (number of edges between pairs in {a,b,c})
    # We want this to be equal to (deg[a] + deg[b] + deg[c]) - 3
    # So: deg[a] + deg[b] + deg[c] - E_abc = deg[a] + deg[b] + deg[c] - 3
    # => E_abc = 3
    # So we need exactly 3 edges among the three nodes {a,b,c}, i.e., they form a triangle.
    
    # But wait, that's not right either. Let's read the condition again.
    # "the total number of preliminary reports involving *at least one* of these three individuals 
    # is exactly equal to (D_a + D_b + D_c) - 3"
    
    # The number of edges involving at least one of a,b,c is:
    # |Edges where at least one endpoint is in {a,b,c}|
    
    # Let's think of it this way:
    # Total edges incident to a: deg[a]
    # Total edges incident to b: deg[b]
    # Total edges incident to c: deg[c]
    # When we sum deg[a] + deg[b] + deg[c], we count:
    # - Edges between a and b: counted twice (in deg[a] and deg[b])
    # - Edges between a and c: counted twice
    # - Edges between b and c: counted twice
    # - Edges between a and some x (not b,c): counted once
    # - Edges between b and some x (not a,c): counted once
    # - Edges between c and some x (not a,b): counted once
    
    # So the actual number of distinct edges involving at least one of {a,b,c} is:
    # deg[a] + deg[b] + deg[c] - (number of edges between a,b - between a,c - between b,c)
    # Let E_ab, E_ac, E_bc be 1 if the edge exists, 0 otherwise.
    # Then number of edges among a,b,c is E_ab + E_ac + E_bc.
    # So number of edges involving at least one of {a,b,c} = 
    # deg[a] + deg[b] + deg[c] - (E_ab + E_ac + E_bc)
    
    # We want this to be equal to (deg[a] + deg[b] + deg[c]) - 3
    # So: deg[a] + deg[b] + deg[c] - (E_ab + E_ac + E_bc) = deg[a] + deg[b] + deg[c] - 3
    # => E_ab + E_ac + E_bc = 3
    # So we need all three edges to exist between a,b,c. That is, a triangle.
    
    # But the examples don't seem to support that.
    # Example 1: edges (1,2), (1,3), (2,3), (2,4), (3,4)
    # For {1,2,3}: deg[1]=2, deg[2]=3, deg[3]=3. Sum=8.
    # Edges among 1,2,3: (1,2), (1,3), (2,3) => 3 edges.
    # Edges involving at least one of {1,2,3}: all except (2,4) and (3,4) => 3 edges.
    # Wait, no. Edges involving at least one of {1,2,3}:
    # (1,2): yes
    # (1,3): yes
    # (2,3): yes
    # (2,4): yes (2 is in set)
    # (3,4): yes (3 is in set)
    # So all 5 edges involve at least one of {1,2,3}.
    # deg[1] + deg[2] + deg[3] = 2 + 3 + 3 = 8.
    # 8 - 3 = 5. Yes, it matches.
    
    # So the condition is: 
    # Number of edges involving at least one node in {a,b,c} = deg[a] + deg[b] + deg[c] - 3
    
    # Let's think combinatorially.
    # When we sum deg[a] + deg[b] + deg[c], we overcount the edges within the triangle.
    # For a triangle, there are 3 internal edges, each counted twice, so overcount by 3.
    # So actual number of distinct edges touching {a,b,c} = deg[a] + deg[b] + deg[c] - 3.
    # This matches the required condition for any triangle.
    
    # So we just need to find any triangle.
    # But the problem says "at least one such group exists" and to find the lexicographically smallest.
    
    # Let's re-check Example 2:
    # Edges: (1,2), (1,4), (2,4), (3,4), (3,5), (4,5)
    # Degrees: deg[1]=2, deg[2]=2, deg[3]=2, deg[4]=4, deg[5]=2
    # Check {1,2,4}:
    # deg[1] + deg[2] + deg[4] = 2 + 2 + 4 = 8
    # Edges among them: (1,2), (1,4), (2,4) => 3 edges
    # Edges involving at least one of {1,2,4}: all edges except (3,5) => 5 edges
    # 8 - 3 = 5. Yes.
    
    # So the condition is satisfied by any triangle.
    # We need to find a triangle {a,b,c} with a<b<c that is lexicographically smallest.
    
    # Build adjacency list
    adj_list = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # Sort adjacency lists for consistent iteration
    for i in range(1, n + 1):
        adj_list[i].sort()
    
    # Convert to sets for fast lookup
    adj_set = [set() for _ in range(n + 1)]
    for i in range(1, n + 1):
        adj_set[i] = set(adj_list[i])
    
    # Find the lexicographically smallest triangle
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            if b not in adj_set[a]:
                continue
            for c in range(b + 1, n + 1):
                if c not in adj_set[a]:
                    continue
                if c not in adj_set[b]:
                    continue
                # Found triangle {a,b,c}
                print(a, b, c)
                return

if __name__ == "__main__":
    main()