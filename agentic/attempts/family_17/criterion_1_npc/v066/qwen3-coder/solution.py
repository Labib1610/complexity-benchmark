from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    configs = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        configs.append((a, b, c))
    
    # Build a graph where each person is a node and each configuration is an edge
    # This is actually a matching problem: we want to select q configurations such that
    # each person from 1 to 3q is in exactly one configuration
    
    # This can be modeled as a maximum matching problem in a bipartite graph
    # Left side: configurations (0 to t-1)
    # Right side: people (1 to 3q)
    # But we actually want a perfect matching where each person is matched exactly once
    # and we select exactly q configurations
    
    # Better approach: model as exact cover problem and use backtracking
    
    # For small constraints, we can use backtracking
    # But let's think of it as a matching: we want to select q triples that partition 
    # the set {1, 2, ..., 3q}
    
    # Use backtracking with pruning
    used = [False] * (3 * q + 1)
    selected = []
    
    def backtrack(idx):
        # Check if all people are covered
        if len(selected) == q:
            # Verify that all people 1 to 3q are used exactly once
            temp_used = [False] * (3 * q + 1)
            for triple in selected:
                a, b, c = triple
                if temp_used[a] or temp_used[b] or temp_used[c]:
                    return False
                temp_used[a] = temp_used[b] = temp_used[c] = True
            for i in range(1, 3*q + 1):
                if not temp_used[i]:
                    return False
            return True
        
        if idx == t:
            return False
            
        # Try including this configuration
        a, b, c = configs[idx]
        if not used[a] and not used[b] and not used[c]:
            used[a] = used[b] = used[c] = True
            selected.append(configs[idx])
            if backtrack(idx + 1):
                return True
            selected.pop()
            used[a] = used[b] = used[c] = False
        
        # Try not including this configuration
        if backtrack(idx + 1):
            return True
            
        return False
    
    # This backtracking might be too slow. Let's try a different approach.
    # Model this as a maximum matching problem or use a more efficient algorithm.
    
    # Use a greedy approach with backtracking optimization
    # But for correctness, let's use a more systematic approach
    
    # Try to model as exact cover and use algorithm X (dancing links) or simple recursion
    # with better pruning
    
    def can_cover():
        # Try all combinations using recursive backtracking with better state management
        selected_configs = []
        used_people = [False] * (3 * q + 1)
        
        def dfs(config_idx):
            if len(selected_configs) == q:
                return True
            if config_idx == t:
                return False
                
            # Try including current configuration
            a, b, c = configs[config_idx]
            if not used_people[a] and not used_people[b] and not used_people[c]:
                used_people[a] = used_people[b] = used_people[c] = True
                selected_configs.append(config_idx)
                if dfs(config_idx + 1):
                    return True
                selected_configs.pop()
                used_people[a] = used_people[b] = used_people[c] = False
            
            # Try not including current configuration
            if dfs(config_idx + 1):
                return True
                
            return False
        
        if dfs(0):
            print("YES")
            for idx in selected_configs:
                print(configs[idx][0], configs[idx][1], configs[idx][2])
            return True
        else:
            return False
    
    if not can_cover():
        print("NO")

solve()