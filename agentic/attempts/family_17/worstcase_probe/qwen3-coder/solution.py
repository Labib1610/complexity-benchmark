from collections import defaultdict
import sys

def find_deployment(q, t, triples):
    if t == 0:
        if q == 0:
            print("YES")
            return
        else:
            print("NO")
            return
    
    # If the number of operators is not divisible by 3, it's impossible
    if 3 * q % 3 != 0 or q * 3 < 3:
        print("NO")
        return
        
    n = 3 * q  # Total number of operators
    
    # Create a graph where each operator is a node and each triple is a hyperedge
    # This is essentially a 3D matching problem
    
    # Try to find a perfect matching using backtracking
    # We'll use a greedy approach with backtracking
    
    # Build adjacency list for each operator
    adj = defaultdict(list)
    for i, (a, b, c) in enumerate(triples):
        adj[a].append(i)
        adj[b].append(i)
        adj[c].append(i)
    
    # Track which triples are used and which operators are covered
    used = [False] * t
    covered = [False] * (n + 1)
    result = []
    
    def backtrack():
        # Find the first uncovered operator
        first_uncovered = -1
        for i in range(1, n + 1):
            if not covered[i]:
                first_uncovered = i
                break
        
        # If all operators are covered, we found a solution
        if first_uncovered == -1:
            return True
            
        # Try each triple containing the first uncovered operator
        for triple_idx in adj[first_uncovered]:
            if used[triple_idx]:
                continue
                
            a, b, c = triples[triple_idx]
            
            # Check if all operators in this triple are still available
            if covered[a] or covered[b] or covered[c]:
                continue
                
            # Use this triple
            used[triple_idx] = True
            covered[a] = covered[b] = covered[c] = True
            result.append((a, b, c))
            
            # Recurse
            if backtrack():
                return True
                
            # Backtrack
            used[triple_idx] = False
            covered[a] = covered[b] = covered[c] = False
            result.pop()
            
        return False
    
    # Special case: if q=0, we need 0 triples
    if q == 0:
        print("YES")
        return
    
    if backtrack():
        print("YES")
        for triple in result:
            print(triple[0], triple[1], triple[2])
    else:
        print("NO")

# Read input
line = input().split()
q, t = int(line[0]), int(line[1])

triples = []
for _ in range(t):
    a, b, c = map(int, input().split())
    triples.append((a, b, c))

find_deployment(q, t, triples)