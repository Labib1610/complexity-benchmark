import sys
from collections import defaultdict

def find_deployment(q, t, trios):
    if t < q:
        return None
    
    # Create adjacency list for graph representation
    # Each operator is a node, each trio is a hyperedge
    # We'll create a graph where each valid trio is represented
    
    # Use backtracking with pruning
    def backtrack(used_operators, selected_trios, remaining_trios):
        if len(selected_trios) == q:
            return selected_trios[:]
        
        if len(remaining_trios) < q - len(selected_trios):
            return None
            
        for i, trio in enumerate(remaining_trios):
            a, b, c = trio
            if a not in used_operators and b not in used_operators and c not in used_operators:
                used_operators.add(a)
                used_operators.add(b)
                used_operators.add(c)
                selected_trios.append(trio)
                
                result = backtrack(used_operators, selected_trios, remaining_trios[i+1:])
                if result is not None:
                    return result
                    
                selected_trios.pop()
                used_operators.remove(a)
                used_operators.remove(b)
                used_operators.remove(c)
        
        return None
    
    # Sort trios by smallest element to improve pruning
    trios.sort()
    result = backtrack(set(), [], trios)
    return result

def main():
    input_lines = []
    for line in sys.stdin:
        input_lines.append(line.strip())
    
    line_idx = 0
    q, t = map(int, input_lines[line_idx].split())
    line_idx += 1
    
    trios = []
    for i in range(t):
        a, b, c = map(int, input_lines[line_idx].split())
        trios.append((a, b, c))
        line_idx += 1
    
    # Special case: if q=0, we need 0 trios
    if q == 0:
        print("YES")
        return
    
    if t == 0:
        print("NO")
        return
    
    # Try to find a solution using backtracking with optimization
    def solve():
        # Create a graph approach - maximum matching in 3-uniform hypergraph
        # But let's use a more direct approach with optimizations
        
        # Preprocessing: count how many times each operator appears
        operator_count = defaultdict(int)
        for trio in trios:
            for op in trio:
                operator_count[op] += 1
        
        # Check if any operator doesn't appear enough times
        for i in range(1, 3*q + 1):
            if operator_count[i] == 0:
                return None
        
        # Use recursive backtracking with better pruning
        def backtrack_v2(available_trios, used_ops, selected):
            if len(selected) == q:
                return selected[:]
            
            # Pruning: not enough trios left
            if len(available_trios) < q - len(selected):
                return None
                
            # Pruning: check if all unused operators can still be covered
            remaining_ops = set(range(1, 3*q + 1)) - used_ops
            if len(remaining_ops) > 3 * (q - len(selected)):
                return None
            
            for i, trio in enumerate(available_trios):
                a, b, c = trio
                if a not in used_ops and b not in used_ops and c not in used_ops:
                    # Check if this trio helps cover needed operators
                    new_used = used_ops | {a, b, c}
                    new_selected = selected + [trio]
                    result = backtrack_v2(available_trios[i+1:], new_used, new_selected)
                    if result is not None:
                        return result
            
            return None
        
        return backtrack_v2(trios, set(), [])
    
    result = solve()
    
    if result is None:
        print("NO")
    else:
        print("YES")
        for trio in result:
            print(trio[0], trio[1], trio[2])

if __name__ == "__main__":
    main()