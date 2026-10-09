import sys
from itertools import combinations

def solve():
    q, t = map(int, sys.stdin.readline().split())
    
    triples = []
    for _ in range(t):
        a, b, c = map(int, sys.stdin.readline().split())
        triples.append((a, b, c))
    
    # We need to find a perfect matching that covers all 3*q nodes
    # This is essentially a exact cover problem
    
    # Create a graph where each triple is a node and edges represent conflicts
    # Two triples conflict if they share at least one element
    
    # But actually we want to find a set of triples such that each number 1..3q appears exactly once
    # This is a maximum matching problem in a hypergraph, or more specifically, 
    # we're looking for a partition of the universe into sets of size 3
    
    # Since q <= 200, and we have at most 20000 triples, we can try backtracking approach
    
    # Let's model this as finding a set of disjoint triples that cover all elements
    
    # Use backtracking with optimizations
    n = 3 * q
    elements = list(range(1, n + 1))
    
    # For each element, keep track of which triples contain it
    element_to_triples = [[] for _ in range(n + 1)]
    for i, (a, b, c) in enumerate(triples):
        element_to_triples[a].append(i)
        element_to_triples[b].append(i)
        element_to_triples[c].append(i)
    
    # Sort triples by how constrained they are (fewer available elements first)
    # Actually let's just try a simple backtracking approach
    
    used_elements = [False] * (n + 1)
    selected_triples = []
    
    def backtrack(index):
        # Find the first unused element
        while index <= n and used_elements[index]:
            index += 1
            
        # If all elements are used, we found a solution
        if index > n:
            return True
            
        # Try each triple containing this element
        for triple_idx in element_to_triples[index]:
            a, b, c = triples[triple_idx]
            
            # Check if this triple can be used
            if not used_elements[a] and not used_elements[b] and not used_elements[c]:
                # Use this triple
                used_elements[a] = used_elements[b] = used_elements[c] = True
                selected_triples.append(triple_idx)
                
                # Recurse
                if backtrack(index + 1):
                    return True
                    
                # Backtrack
                used_elements[a] = used_elements[b] = used_elements[c] = False
                selected_triples.pop()
        
        return False
    
    # Optimization: start with elements that have fewest possible triples
    element_count = [len(element_to_triples[i]) for i in range(1, n + 1)]
    order = sorted(range(1, n + 1), key=lambda x: element_count[x-1])
    
    # Try to find a solution starting with the most constrained element
    if backtrack(1):
        print("YES")
        for idx in selected_triples:
            a, b, c = triples[idx]
            print(a, b, c)
    else:
        print("NO")

solve()