from collections import defaultdict
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    t = int(data[1])
    
    index = 2
    combinations = []
    for _ in range(t):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        combinations.append((a, b, c))
        index += 3
    
    # Try to find a matching that covers all 3*q nodes
    # This is a exact cover problem - we can model it as finding a maximum matching in a hypergraph
    # But since each combination covers exactly 3 nodes and we need to cover 3*q nodes with q combinations,
    # we just need to find if there exists a perfect matching in terms of combinations
    
    # We'll use backtracking / DFS approach
    # Build a graph where each node (staff) points to combinations it's part of
    staff_to_combinations = defaultdict(list)
    for i, (a, b, c) in enumerate(combinations):
        staff_to_combinations[a].append(i)
        staff_to_combinations[b].append(i)
        staff_to_combinations[c].append(i)
    
    # Try to assign combinations
    selected = [False] * t  # which combinations are selected
    assigned = [False] * (3*q + 1)  # which staff are assigned
    result = []
    
    def backtrack(pos):
        if pos == 3*q + 1:
            return sum(assigned) == 3*q
        
        if assigned[pos]:
            return backtrack(pos + 1)
        
        # Try each combination that includes 'pos'
        for comb_idx in staff_to_combinations[pos]:
            if selected[comb_idx]:
                continue
            a, b, c = combinations[comb_idx]
            if not assigned[a] and not assigned[b] and not assigned[c]:
                # Assign this combination
                selected[comb_idx] = True
                assigned[a] = assigned[b] = assigned[c] = True
                result.append((a, b, c))
                
                if backtrack(pos + 1):
                    return True
                
                # Backtrack
                selected[comb_idx] = False
                assigned[a] = assigned[b] = assigned[c] = False
                result.pop()
        
        return False
    
    # Optimization: start with the staff member who has the fewest options
    # Find the unassigned staff with minimum available combinations
    def find_next_unassigned():
        min_options = float('inf')
        best_pos = -1
        for i in range(1, 3*q + 1):
            if not assigned[i]:
                options = len([c for c in staff_to_combinations[i] if not selected[c]])
                if options < min_options:
                    min_options = options
                    best_pos = i
        return best_pos if best_pos != -1 else 3*q + 1
    
    # Alternative backtracking with better heuristics
    def backtrack_opt():
        # Check if all assigned
        if sum(assigned) == 3*q:
            return True
            
        # Find the unassigned person with the fewest options
        min_options = float('inf')
        pos = -1
        for i in range(1, 3*q + 1):
            if not assigned[i]:
                options = len([c for c in staff_to_combinations[i] if not selected[c]])
                if options < min_options:
                    min_options = options
                    pos = i
        
        if pos == -1:
            return sum(assigned) == 3*q
            
        # Try each combination that includes 'pos'
        for comb_idx in staff_to_combinations[pos]:
            if selected[comb_idx]:
                continue
            a, b, c = combinations[comb_idx]
            if not assigned[a] and not assigned[b] and not assigned[c]:
                # Assign this combination
                selected[comb_idx] = True
                assigned[a] = assigned[b] = assigned[c] = True
                result.append((a, b, c))
                
                if backtrack_opt():
                    return True
                
                # Backtrack
                selected[comb_idx] = False
                assigned[a] = assigned[b] = assigned[c] = False
                result.pop()
        
        return False
    
    # Initialize assignment
    if backtrack_opt():
        print("YES")
        for a, b, c in result:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    main()