from itertools import combinations

def solve():
    q, t = map(int, input().split())
    triples = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        triples.append((a, b, c))
    
    # We need to select exactly q triples to cover all 3*q operators
    # This is essentially a matching problem - we want to find a perfect matching
    # where each operator appears exactly once
    
    # Try all combinations of q triples from the t available triples
    for selected_indices in combinations(range(t), q):
        used_operators = set()
        selected_triples = []
        valid = True
        
        for idx in selected_indices:
            triple = triples[idx]
            # Check if any operator in this triple is already used
            if any(op in used_operators for op in triple):
                valid = False
                break
            # Add operators to used set
            used_operators.update(triple)
            selected_triples.append(triple)
        
        # If we successfully assigned all operators
        if valid and len(used_operators) == 3 * q:
            print("YES")
            for triple in selected_triples:
                print(triple[0], triple[1], triple[2])
            return
    
    print("NO")

solve()