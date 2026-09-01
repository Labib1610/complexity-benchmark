from itertools import product

def determinant(su, sv):
    # Compute the determinant of the characteristic matrix
    # C = [[1, su + 2, su^2 + 4*sv],
    #      [1, sv,     sv^2      ],
    #      [1, sv + 1, sv^2 + 2*sv]]
    #
    # det(C) = 1 * (sv * (sv^2 + 2*sv) - (sv^2) * (sv + 1)) 
    #        - (su + 2) * (1 * (sv^2 + 2*sv) - (sv^2) * 1)
    #        + (su^2 + 4*sv) * (1 * (sv + 1) - sv * 1)
    # Simplify each term:
    # First term: sv*(sv^2 + 2*sv) - sv^2*(sv + 1) = sv^3 + 2*sv^2 - sv^3 - sv^2 = sv^2
    # Second term: -(su + 2) * (sv^2 + 2*sv - sv^2) = -(su + 2) * (2*sv)
    # Third term: (su^2 + 4*sv) * (sv + 1 - sv) = (su^2 + 4*sv) * 1
    # So det = sv^2 - 2*sv*(su + 2) + (su^2 + 4*sv)
    #        = sv^2 - 2*sv*su - 4*sv + su^2 + 4*sv
    #        = sv^2 - 2*sv*su + su^2
    #        = (su - sv)^2
    return (su - sv) ** 2

def is_valid_configuration(assignment, links):
    for u, v in links:
        su = assignment[u - 1]
        sv = assignment[v - 1]
        if determinant(su, sv) == 0:
            return False
    return True

def compute_signature(assignment):
    V = 0
    for s in assignment:
        V = 4 * V + s
    return V

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
    
    links = []
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        links.append((u, v))
        index += 2
    
    best_assignment = None
    min_signature = None
    
    # Try all 3^n possible assignments
    for assignment in product([1, 2, 3], repeat=n):
        if is_valid_configuration(assignment, links):
            sig = compute_signature(assignment)
            if min_signature is None or sig < min_signature:
                min_signature = sig
                best_assignment = assignment
    
    if best_assignment is None:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, best_assignment)))

if __name__ == "__main__":
    main()