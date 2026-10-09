from collections import defaultdict

def solve():
    q, t = map(int, input().split())
    groups = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        groups.append((a, b, c))
    
    # Try all combinations of q groups from t available groups
    # Since q <= 200 and t <= 20000, we need an efficient approach
    
    # This is essentially a matching problem - we want to select q groups
    # such that each number from 1 to 3*q appears exactly once
    
    # Use backtracking with pruning
    def backtrack(selected_groups, used_artifacts, index):
        if len(selected_groups) == q:
            return selected_groups
        
        if index >= t:
            return None
            
        # Pruning: if even selecting all remaining groups won't give us enough
        if len(selected_groups) + (t - index) < q:
            return None
            
        # Try including current group
        a, b, c = groups[index]
        if a not in used_artifacts and b not in used_artifacts and c not in used_artifacts:
            used_artifacts.add(a)
            used_artifacts.add(b)
            used_artifacts.add(c)
            selected_groups.append(groups[index])
            
            result = backtrack(selected_groups, used_artifacts, index + 1)
            if result is not None:
                return result
                
            selected_groups.pop()
            used_artifacts.remove(a)
            used_artifacts.remove(b)
            used_artifacts.remove(c)
        
        # Try not including current group
        result = backtrack(selected_groups, used_artifacts, index + 1)
        return result
    
    # Optimization: sort groups by smallest element to improve pruning
    groups.sort()
    
    result = backtrack([], set(), 0)
    
    if result is None:
        print("NO")
    else:
        print("YES")
        for group in result:
            print(group[0], group[1], group[2])

solve()