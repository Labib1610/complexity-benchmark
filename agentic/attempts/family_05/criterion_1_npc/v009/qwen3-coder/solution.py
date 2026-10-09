from itertools import permutations

def solve():
    k, t = map(int, input().split())
    
    # Read all allowed combinations
    allowed = set()
    for _ in range(t):
        x, y, z = map(int, input().split())
        allowed.add((x, y, z))
    
    # Generate all possible permutations of machines for specialists
    # We need to find a permutation of machines and a permutation of time slots
    # such that all k triples (i, perm_y[i], perm_z[i]) are allowed
    
    specialists = list(range(1, k + 1))
    
    # Try all permutations of machines
    for perm_y in permutations(range(1, k + 1)):
        # Try all permutations of time slots
        for perm_z in permutations(range(1, k + 1)):
            # Check if this combination works
            valid = True
            crews = []
            for i in range(k):
                x = specialists[i]
                y = perm_y[i]
                z = perm_z[i]
                if (x, y, z) not in allowed:
                    valid = False
                    break
                crews.append((x, y, z))
            
            if valid:
                print("YES")
                for crew in crews:
                    print(crew[0], crew[1], crew[2])
                return
    
    print("NO")

solve()