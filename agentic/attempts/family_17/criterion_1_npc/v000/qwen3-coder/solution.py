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
    
    # Create adjacency list for graph representation
    # Each operator is a node, each triple is a hyperedge
    adj = defaultdict(list)
    for i, (a, b, c) in enumerate(triples):
        adj[a].append(i)
        adj[b].append(i)
        adj[c].append(i)
    
    # Try to find a perfect matching using backtracking
    used_triples = [False] * len(triples)
    selected = []
    covered = [False] * (n + 1)
    
    def backtrack(operator):
        if operator > n:
            return True
            
        if covered[operator]:
            return backtrack(operator + 1)
            
        # Try all triples containing this operator
        for triple_idx in adj[operator]:
            if used_triples[triple_idx]:
                continue
                
            a, b, c = triples[triple_idx]
            
            # Check if all operators in this triple are available
            if covered[a] or covered[b] or covered[c]:
                continue
                
            # Use this triple
            used_triples[triple_idx] = True
            selected.append((a, b, c))
            covered[a] = covered[b] = covered[c] = True
            
            # Continue with next uncovered operator
            next_op = operator + 1
            while next_op <= n and covered[next_op]:
                next_op += 1
                
            if backtrack(next_op):
                return True
                
            # Backtrack
            used_triples[triple_idx] = False
            selected.pop()
            covered[a] = covered[b] = covered[c] = False
            
        return False
    
    # Start backtracking from operator 1
    if backtrack(1):
        print("YES")
        for triple in selected:
            print(*triple)
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