from collections import defaultdict
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    t = int(data[1])
    
    blueprints = []
    index = 2
    for _ in range(t):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        blueprints.append((a, b, c))
        index += 3
    
    # Create a graph where each component is a node and each blueprint is a hyperedge
    # We can model this as a matching problem or use a backtracking approach
    # Since q <= 200, and we need to match exactly q blueprints, we can try to find a matching
    
    # Use a greedy approach or backtracking
    # Let's try a backtracking approach with optimizations
    
    # First, build a mapping from components to which blueprints contain them
    component_to_blueprints = defaultdict(list)
    for i, (a, b, c) in enumerate(blueprints):
        component_to_blueprints[a].append(i)
        component_to_blueprints[b].append(i)
        component_to_blueprints[c].append(i)
    
    # We need to select exactly q blueprints such that all 3q components are used exactly once
    # This is a exact cover problem, which can be solved with backtracking
    
    selected = [False] * t  # which blueprints are selected
    used_components = [False] * (3*q + 1)  # which components are used
    solution = []
    
    def backtrack(blueprint_index, count):
        if count == q:
            # Check if all components are used
            for i in range(1, 3*q + 1):
                if not used_components[i]:
                    return False
            return True
        
        if blueprint_index == t:
            return False
            
        # Try not taking this blueprint
        if backtrack(blueprint_index + 1, count):
            return True
            
        # Try taking this blueprint
        a, b, c = blueprints[blueprint_index]
        if not used_components[a] and not used_components[b] and not used_components[c]:
            selected[blueprint_index] = True
            used_components[a] = True
            used_components[b] = True
            used_components[c] = True
            solution.append(blueprint_index)
            
            if backtrack(blueprint_index + 1, count + 1):
                return True
                
            # Backtrack
            selected[blueprint_index] = False
            used_components[a] = False
            used_components[b] = False
            used_components[c] = False
            solution.pop()
            
        return False
    
    # Optimization: sort blueprints by their first component to improve pruning
    # Also, we can do a quick check: if any component is not in any blueprint, return NO
    for i in range(1, 3*q + 1):
        if not component_to_blueprints[i]:
            print("NO")
            return
    
    if backtrack(0, 0):
        print("YES")
        for idx in solution:
            a, b, c = blueprints[idx]
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    main()