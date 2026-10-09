from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    if t < k:
        print("NO")
        return
    
    combinations = []
    index = 2
    for _ in range(t):
        x = int(data[index])
        y = int(data[index+1])
        z = int(data[index+2])
        combinations.append((x, y, z))
        index += 3
    
    # Try to find a perfect matching using backtracking with pruning
    # We need to match each source, reflector, and detector exactly once
    
    # Build mappings for pruning
    source_map = defaultdict(list)
    reflector_map = defaultdict(list)
    detector_map = defaultdict(list)
    
    for i, (x, y, z) in enumerate(combinations):
        source_map[x].append(i)
        reflector_map[y].append(i)
        detector_map[z].append(i)
    
    # Check if any source/reflector/detector is not covered by any combination
    for i in range(1, k+1):
        if not source_map[i] or not reflector_map[i] or not detector_map[i]:
            print("NO")
            return
    
    # Backtracking approach
    used_combinations = [False] * t
    used_sources = [False] * (k+1)
    used_reflectors = [False] * (k+1)
    used_detectors = [False] * (k+1)
    result = []
    
    def backtrack(pos):
        if pos == k:
            return True
            
        for i in range(t):
            if used_combinations[i]:
                continue
                
            x, y, z = combinations[i]
            
            if used_sources[x] or used_reflectors[y] or used_detectors[z]:
                continue
            
            used_combinations[i] = True
            used_sources[x] = True
            used_reflectors[y] = True
            used_detectors[z] = True
            result.append((x, y, z))
            
            if backtrack(pos + 1):
                return True
                
            used_combinations[i] = False
            used_sources[x] = False
            used_reflectors[y] = False
            used_detectors[z] = False
            result.pop()
            
        return False
    
    # Optimization: sort combinations to try more promising ones first
    # Prioritize combinations that use less frequent elements
    combo_scores = []
    for i, (x, y, z) in enumerate(combinations):
        score = len(source_map[x]) + len(reflector_map[y]) + len(detector_map[z])
        combo_scores.append((score, i))
    
    combo_scores.sort()
    ordered_indices = [idx for score, idx in combo_scores]
    
    # Try combinations in the optimized order
    def backtrack_optimized(pos):
        if pos == k:
            return True
            
        for i in ordered_indices:
            if used_combinations[i]:
                continue
                
            x, y, z = combinations[i]
            
            if used_sources[x] or used_reflectors[y] or used_detectors[z]:
                continue
            
            used_combinations[i] = True
            used_sources[x] = True
            used_reflectors[y] = True
            used_detectors[z] = True
            result.append((x, y, z))
            
            if backtrack_optimized(pos + 1):
                return True
                
            used_combinations[i] = False
            used_sources[x] = False
            used_reflectors[y] = False
            used_detectors[z] = False
            result.pop()
            
        return False
    
    if backtrack_optimized(0):
        print("YES")
        for x, y, z in result:
            print(x, y, z)
    else:
        print("NO")

solve()