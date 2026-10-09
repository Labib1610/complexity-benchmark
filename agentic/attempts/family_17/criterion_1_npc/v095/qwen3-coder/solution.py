import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    t = int(data[1])
    
    # Total frequency bands: 3*q
    # Each resonator covers exactly 3 bands
    # Need exactly q resonators to cover all 3*q bands without overlap
    
    configs = []
    index = 2
    for i in range(t):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        configs.append((a, b, c))
        index += 3
    
    # This is essentially a matching problem:
    # We want to select exactly q triplets from the t triplets,
    # such that all 3q numbers from 1 to 3q are covered exactly once.
    
    # Model as a bipartite matching:
    # Left side: q positions (slots) 
    # Right side: t resonator configurations
    # Edge exists if we can use that configuration
    
    # But actually, it's more direct to think of it as:
    # Find a subset of q triplets that partitions the set {1,2,...,3q}
    
    # Let's model this as exact cover and use backtracking with pruning
    
    # Map each number 1..3q to the list of configs that contain it
    num_to_configs = defaultdict(list)
    for idx, (a,b,c) in enumerate(configs):
        num_to_configs[a].append(idx)
        num_to_configs[b].append(idx)
        num_to_configs[c].append(idx)
    
    # Check if any number is not covered by any config
    for i in range(1, 3*q + 1):
        if i not in num_to_configs:
            print("NO")
            return
    
    # Try to build a mapping: for each number, decide which config will cover it
    # But better approach: try to select q configs such that they form a partition
    
    # Use backtracking: select configs one by one ensuring no overlap
    used_configs = [False] * t
    selected = []
    covered = [False] * (3*q + 1)  # covered[i] = True if frequency i is already covered
    
    def backtrack(config_index):
        # If we've selected q configs and covered all 3q frequencies
        if len(selected) == q:
            # Check if all frequencies are covered
            for i in range(1, 3*q + 1):
                if not covered[i]:
                    return False
            return True
        
        # Pruning: if remaining positions cannot be filled, return False
        # We need (q - len(selected)) more configs
        # And there are (t - config_index) configs left
        if config_index >= t:
            return False
            
        # Try configs from config_index onwards to avoid duplicate combinations
        for i in range(config_index, t):
            a, b, c = configs[i]
            # If this config does not conflict with already covered frequencies
            if not covered[a] and not covered[b] and not covered[c]:
                # Choose this config
                selected.append(i)
                used_configs[i] = True
                covered[a] = covered[b] = covered[c] = True
                
                # Recurse
                if backtrack(i+1):
                    return True
                    
                # Backtrack
                selected.pop()
                used_configs[i] = False
                covered[a] = covered[b] = covered[c] = False
        
        return False
    
    # Optimization: sort configs to try "earlier" ones first
    # Or just proceed with original order
    
    if backtrack(0):
        print("YES")
        for idx in selected:
            a, b, c = configs[idx]
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    main()