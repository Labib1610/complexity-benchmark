from itertools import combinations

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    t = int(data[1])
    
    # Total number of people
    n = 3 * q
    
    # Read triads
    triads = []
    index = 2
    for _ in range(t):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        triads.append((a, b, c))
        index += 3
    
    # Try all combinations of q triads from t triads
    # But this is too slow for large inputs, so we need a better approach
    
    # Model as exact cover problem and use backtracking
    # Each person must be covered exactly once
    # Each triad can be used at most once
    
    # We'll use backtracking with optimizations
    def backtrack(triad_indices, used_people):
        if len(triad_indices) == q:
            return triad_indices[:]
        
        # Pruning: if remaining needed > remaining available, return None
        remaining_needed = q - len(triad_indices)
        if remaining_needed > len(triads) - len(triad_indices):
            return None
            
        # Find next unused person to focus on
        next_person = None
        for i in range(1, n+1):
            if i not in used_people:
                next_person = i
                break
        
        if next_person is None:
            # All people are used, check if we have exactly q triads
            if len(triad_indices) == q:
                return triad_indices[:]
            else:
                return None
        
        # Try to find a triad that contains next_person
        for i in range(len(triads)):
            if i in triad_indices:
                continue
            a, b, c = triads[i]
            if next_person in (a, b, c):
                # Check if all people in this triad are available
                if a not in used_people and b not in used_people and c not in used_people:
                    triad_indices.append(i)
                    used_people.add(a)
                    used_people.add(b)
                    used_people.add(c)
                    
                    result = backtrack(triad_indices, used_people)
                    if result is not None:
                        return result
                    
                    # Backtrack
                    triad_indices.pop()
                    used_people.remove(a)
                    used_people.remove(b)
                    used_people.remove(c)
        
        return None
    
    # Optimization: sort triads by their minimum element to improve pruning
    # This doesn't change correctness but might help with search order
    
    # Start backtracking
    solution_indices = backtrack([], set())
    
    if solution_indices is None:
        print("NO")
    else:
        print("YES")
        for idx in solution_indices:
            a, b, c = triads[idx]
            print(a, b, c)

solve()