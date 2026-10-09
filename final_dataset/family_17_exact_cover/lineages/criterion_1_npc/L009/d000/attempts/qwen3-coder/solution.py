from collections import defaultdict
import sys

def find_matching(q, t, configurations):
    if t < q:
        return None
    
    # Create adjacency list for graph matching
    # Each configuration is a "right" node, each module is a "left" node
    # We want to find a matching that covers all 3q modules
    
    if q == 0:
        return []
    
    # Try all possible combinations of q configurations
    # Since q <= 200 and we need exact coverage, this is a matching problem
    # We'll use a backtracking approach with optimizations
    
    # Convert configurations to sets for faster intersection checks
    config_sets = [set(config) for config in configurations]
    modules = list(range(1, 3*q + 1))
    
    # Precompute which configurations contain each module
    module_to_configs = defaultdict(list)
    for i, config_set in enumerate(config_sets):
        for module in config_set:
            module_to_configs[module].append(i)
    
    # Try to build a solution using backtracking
    selected = []
    used_configs = [False] * len(configurations)
    used_modules = [False] * (3*q + 1)
    
    def backtrack(config_index):
        # If we've selected q configurations, check if all modules are covered
        if len(selected) == q:
            return all(used_modules[1:])
        
        # If we can't possibly select enough configurations, return False
        if len(selected) + (len(configurations) - config_index) < q:
            return False
            
        # Try each remaining configuration
        for i in range(config_index, len(configurations)):
            config = configurations[i]
            config_set = config_sets[i]
            
            # Check if this configuration conflicts with already used modules
            if any(used_modules[module] for module in config):
                continue
            
            # Use this configuration
            selected.append(i)
            for module in config:
                used_modules[module] = True
            
            # Recurse
            if backtrack(i + 1):
                return True
            
            # Backtrack
            selected.pop()
            for module in config:
                used_modules[module] = False
        
        return False
    
    # Special case for small inputs
    if q <= 10:
        if backtrack(0):
            return [configurations[i] for i in selected]
        else:
            return None
    
    # For larger inputs, try a greedy approach first
    def greedy_approach():
        selected_greedy = []
        used_modules_greedy = [False] * (3*q + 1)
        available_configs = list(range(len(configurations)))
        
        for _ in range(q):
            # Find the first available configuration that doesn't conflict
            found = False
            for i in available_configs[:]:
                config = configurations[i]
                if not any(used_modules_greedy[module] for module in config):
                    selected_greedy.append(i)
                    for module in config:
                        used_modules_greedy[module] = True
                    available_configs.remove(i)
                    found = True
                    break
            if not found:
                return None
        return [configurations[i] for i in selected_greedy]
    
    # Try greedy first
    result = greedy_approach()
    if result is not None:
        return result
    
    # If greedy fails, try backtracking on smaller subset
    if backtrack(0):
        return [configurations[i] for i in selected]
    
    return None

def main():
    input_lines = []
    for line in sys.stdin:
        input_lines.append(line.strip())
    
    q, t = map(int, input_lines[0].split())
    configurations = []
    
    for i in range(1, t + 1):
        if i < len(input_lines):
            a, b, c = map(int, input_lines[i].split())
            configurations.append((a, b, c))
    
    result = find_matching(q, t, configurations)
    
    if result is None:
        print("NO")
    else:
        print("YES")
        for config in result:
            print(config[0], config[1], config[2])

if __name__ == "__main__":
    main()