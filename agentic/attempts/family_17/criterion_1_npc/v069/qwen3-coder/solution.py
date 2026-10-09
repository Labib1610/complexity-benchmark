from itertools import combinations
import sys

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    t = int(data[1])
    
    n = 3 * q
    target_sum = n * (n + 1) // 2
    
    trios = []
    idx = 2
    for _ in range(t):
        a = int(data[idx])
        b = int(data[idx+1])
        c = int(data[idx+2])
        trios.append((a, b, c))
        idx += 3
    
    # Precompute valid trios that satisfy local checksum constraint
    valid_trios = []
    for i, (a, b, c) in enumerate(trios):
        s = a + b + c
        if 6 <= s <= 9*q - 3:
            valid_trios.append(i)
    
    # We need to find a combination of q trios such that:
    # 1. All 3q operators are used exactly once
    # 2. The sum of all operators equals target_sum
    
    # Since each trio contributes exactly 3 operators and we choose q trios,
    # we will have 3q operators, which matches the roster size.
    # The global checksum is automatically satisfied since we use each operator once.
    
    # So we just need to find a matching that covers all operators.
    
    from collections import defaultdict
    
    # Build a graph where nodes are operators and edges are valid trios
    operator_to_trios = defaultdict(list)
    for i in valid_trios:
        a, b, c = trios[i]
        operator_to_trios[a].append(i)
        operator_to_trios[b].append(i)
        operator_to_trios[c].append(i)
    
    # Use backtracking to find a perfect matching
    def backtrack(index, selected, used_operators):
        if index == q:
            if len(used_operators) == n:
                return selected[:]
            else:
                return None
        
        # Try each valid trio
        for i in valid_trios:
            if i in selected:
                continue
            a, b, c = trios[i]
            if a in used_operators or b in used_operators or c in used_operators:
                continue
            
            # Add this trio
            selected.append(i)
            used_operators.add(a)
            used_operators.add(b)
            used_operators.add(c)
            
            result = backtrack(index + 1, selected, used_operators)
            if result is not None:
                return result
                
            # Backtrack
            selected.pop()
            used_operators.discard(a)
            used_operators.discard(b)
            used_operators.discard(c)
        
        return None
    
    # Optimization: start with operators that have fewer options
    # Count how many trios each operator appears in
    operator_count = defaultdict(int)
    for i in valid_trios:
        a, b, c = trios[i]
        operator_count[a] += 1
        operator_count[b] += 1
        operator_count[c] += 1
    
    # Sort operators by count (ascending)
    sorted_ops = sorted(operator_count.keys(), key=lambda x: operator_count[x])
    
    # Start backtracking
    result_indices = backtrack(0, [], set())
    
    if result_indices is None:
        print("NO")
        return
    
    print("YES")
    for i in result_indices:
        a, b, c = trios[i]
        print(a, b, c)

solve()