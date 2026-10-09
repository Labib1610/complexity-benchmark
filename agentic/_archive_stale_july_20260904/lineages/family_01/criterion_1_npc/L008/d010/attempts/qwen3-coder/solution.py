from itertools import product

def determinant(su, sv):
    # Calculate the determinant of the matrix
    # C = [[su, sv, su**2 + u + v + 10],
    #      [1,  1,  sv           ],
    #      [sv, su, su*sv        ]]
    # det(C) = su*(1*(su*sv) - sv*sv) - sv*(1*(su*sv) - sv*su) + (su**2 + u + v + 10)*(1*su - 1*sv)
    #        = su*(su*sv - sv**2) - sv*(su*sv - su*sv) + (su**2 + u + v + 10)*(su - sv)
    #        = su*sv*(su - sv) - sv*0 + (su**2 + u + v + 10)*(su - sv)
    #        = (su - sv)*(su*sv + su**2 + u + v + 10)
    # But this is not matching with manual calculation. Let's do it properly:
    
    # Matrix:
    # [su,     sv,       su**2 + u + v + 10]
    # [1,      1,        sv               ]
    # [sv,     su,       su*sv            ]
    
    # Determinant:
    # su * (1 * su*sv - sv * 1) - sv * (1 * su*sv - sv * sv) + (su**2 + u + v + 10) * (1 * su - 1 * sv)
    # = su * (su*sv - sv) - sv * (su*sv - sv**2) + (su**2 + u + v + 10) * (su - sv)
    # = su * sv * (su - 1) - sv * (su*sv - sv**2) + (su**2 + u + v + 10) * (su - sv)
    # = su * sv * (su - 1) - sv**2 * (su - sv) + (su**2 + u + v + 10) * (su - sv)
    # = (su - sv) * (-sv**2 + su**2 + u + v + 10) + su * sv * (su - 1)
    # This is getting complex. Let's compute directly.
    
    a = su
    b = sv
    c = su**2 + 0 + 0 + 10  # u and v will be provided later
    d = 1
    e = 1
    f = sv
    g = sv
    h = su
    i = su * sv
    
    # det = a(e*i - f*h) - b(d*i - f*g) + c(d*h - e*g)
    det = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
    return det

def is_valid_for_link(su, sv, u, v):
    # We need to pass actual u and v to compute c[0][2] correctly
    c02 = su**2 + u + v + 10
    # Recompute determinant with correct values
    det = su*(1 * (su*sv) - sv * 1) - sv*(1 * (su*sv) - sv * sv) + c02*(1 * su - 1 * sv)
    return det != 0

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-based indexing
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2
        
    # Try all 3^n combinations, but in a smart way: backtrack with pruning
    # To minimize signature, try assignments in lexicographical order: (1,1,...,1), (1,1,...,2), ...
    
    best_signature = None
    best_assignment = None
    
    # Generate all possible assignments in lexicographical order
    for assignment in product([1,2,3], repeat=n):
        valid = True
        for u, v in edges:
            su = assignment[u]
            sv = assignment[v]
            # Compute determinant correctly
            c02 = su**2 + (u+1) + (v+1) + 10  # Back to 1-based for formula
            det = su*(1 * (su*sv) - sv * 1) - sv*(1 * (su*sv) - sv * sv) + c02*(1 * su - 1 * sv)
            if det == 0:
                valid = False
                break
                
        if valid:
            # Compute signature
            V = 0
            for s in assignment:
                V = 4 * V + s
            
            if best_signature is None or V < best_signature:
                best_signature = V
                best_assignment = assignment
    
    if best_assignment is None:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, best_assignment)))

if __name__ == "__main__":
    main()