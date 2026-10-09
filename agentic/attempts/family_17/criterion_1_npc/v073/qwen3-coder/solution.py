from collections import defaultdict
import sys

def find_exact_cover(sets, universe):
    """
    Find an exact cover using backtracking with optimization.
    Each set is a tuple of elements, and we want to find a subset of sets
    such that every element in the universe appears exactly once.
    """
    if not universe:
        return []
    
    # Choose the element that appears in the fewest sets (most constrained)
    element_count = defaultdict(int)
    element_sets = defaultdict(list)
    
    for i, s in enumerate(sets):
        for elem in s:
            if elem in universe:
                element_count[elem] += 1
                element_sets[elem].append(i)
    
    # Select the element with minimum count
    selected_element = min(universe, key=lambda x: element_count[x])
    possible_sets = element_sets[selected_element]
    
    # If any element doesn't appear in any set, no solution
    if element_count[selected_element] == 0:
        return None
    
    for set_idx in possible_sets:
        selected_set = sets[set_idx]
        # Check if this set is still valid (all elements in current universe)
        if not all(elem in universe for elem in selected_set):
            continue
            
        # Remove elements of this set from universe
        new_universe = universe - set(selected_set)
        
        # Recursively solve with remaining elements
        result = find_exact_cover(sets[:set_idx] + sets[set_idx+1:], new_universe)
        if result is not None:
            return [set_idx] + result
    
    return None

def main():
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    t = int(data[1])
    
    specialists = list(range(1, 3*q + 1))
    universe = set(specialists)
    sets = []
    original_indices = []  # To keep track of original index for output
    
    idx = 2
    for i in range(t):
        a = int(data[idx])
        b = int(data[idx+1])
        c = int(data[idx+2])
        idx += 3
        sets.append((a, b, c))
        original_indices.append(i)
    
    # Solve exact cover problem
    solution_indices = find_exact_cover(sets, universe)
    
    if solution_indices is None:
        print("NO")
    else:
        print("YES")
        for idx in solution_indices:
            crew = sets[idx]
            print(crew[0], crew[1], crew[2])

if __name__ == "__main__":
    main()