import sys
from collections import defaultdict

def find_matching(k, triples):
    # Build a graph where each surgeon maps to possible (theater, patient) pairs
    # This is essentially a tripartite matching problem
    
    # We'll use backtracking with pruning
    def backtrack(surgeon_idx, used_theaters, used_patients, current_match):
        if surgeon_idx == k:
            return True
            
        # For current surgeon (surgeon_idx + 1), try all viable combinations
        for t, p in surgeon_triples[surgeon_idx + 1]:
            if t not in used_theaters and p not in used_patients:
                used_theaters.add(t)
                used_patients.add(p)
                current_match.append((surgeon_idx + 1, t, p))
                
                if backtrack(surgeon_idx + 1, used_theaters, used_patients, current_match):
                    return True
                    
                used_theaters.remove(t)
                used_patients.remove(p)
                current_match.pop()
        
        return False
    
    # Group triples by surgeon
    surgeon_triples = defaultdict(list)
    for x, y, z in triples:
        surgeon_triples[x].append((y, z))
    
    # Check if all surgeons have at least one option
    for i in range(1, k + 1):
        if i not in surgeon_triples:
            return None
    
    # Try to find a valid matching
    used_theaters = set()
    used_patients = set()
    current_match = []
    
    if backtrack(0, used_theaters, used_patients, current_match):
        return current_match
    else:
        return None

def main():
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    triples = []
    idx = 2
    for _ in range(t):
        x = int(data[idx])
        y = int(data[idx + 1])
        z = int(data[idx + 2])
        triples.append((x, y, z))
        idx += 3
    
    result = find_matching(k, triples)
    
    if result is None:
        print("NO")
    else:
        print("YES")
        for x, y, z in result:
            print(x, y, z)

if __name__ == "__main__":
    main()