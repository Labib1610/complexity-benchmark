from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    n = 3 * q
    
    if t == 0:
        if q == 0:
            print("YES")
        else:
            print("NO")
        return
    
    configurations = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        configurations.append((a, b, c))
    
    # Build graph: each configuration is a node, edges connect configs that don't share parts
    adj = defaultdict(list)
    config_parts = []
    
    for i, (a, b, c) in enumerate(configurations):
        config_parts.append({a, b, c})
    
    for i in range(t):
        for j in range(i + 1, t):
            # If configurations don't share any parts, they can be used together
            if not (config_parts[i] & config_parts[j]):
                adj[i].append(j)
                adj[j].append(i)
    
    # Try to find a clique of size q in this graph
    # This is equivalent to finding q configurations that don't share any parts
    
    # Use backtracking to find a valid combination
    def backtrack(index, selected, used_parts):
        if len(selected) == q:
            return selected[:]
        
        if index >= t:
            return None
        
        # Try including current configuration
        current_parts = config_parts[index]
        if not (used_parts & current_parts):  # No overlap with already used parts
            selected.append(index)
            new_used = used_parts | current_parts
            result = backtrack(index + 1, selected, new_used)
            if result is not None:
                return result
            selected.pop()
        
        # Try not including current configuration
        return backtrack(index + 1, selected, used_parts)
    
    # Optimization: try configurations that use parts 1, 2, 3 first
    result = backtrack(0, [], set())
    
    if result is not None:
        print("YES")
        for idx in result:
            a, b, c = configurations[idx]
            print(a, b, c)
    else:
        print("NO")

solve()