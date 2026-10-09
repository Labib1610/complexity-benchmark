import sys
from itertools import combinations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    # Read the conflicting pairs
    conflicts = set()
    idx = 3
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        conflicts.add((u, v))
        conflicts.add((v, u))
        idx += 2
    
    # Generate all combinations of k compounds
    compounds = list(range(1, n+1))
    
    # Since n <= 46 and we might need to check C(n,k) which can be large,
    # but given the constraints, a brute-force approach should work.
    # However, let's optimize by checking only necessary combinations.
    
    # For small k, we can iterate through combinations efficiently.
    # Python's itertools.combinations generates combinations in lexicographic order.
    
    found = False
    result = []
    
    # We'll generate combinations and check for stability
    for combo in combinations(compounds, k):
        # Check if any pair in this combination has a conflict
        valid = True
        for i in range(k):
            for j in range(i+1, k):
                u = combo[i]
                v = combo[j]
                if (u,v) in conflicts:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            found = True
            result = list(combo)
            break
    
    if found:
        print("YES")
        print(' '.join(map(str, result)))
    else:
        print("NO")

if __name__ == "__main__":
    main()