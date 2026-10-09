from collections import defaultdict

def solve():
    k, t = map(int, input().split())
    
    if k == 0:
        print("YES")
        return
    
    pathways = []
    for _ in range(t):
        u, v, w = map(int, input().split())
        pathways.append((u, v, w))
    
    # We need to find a perfect matching where each input, output, and frequency is used exactly once
    # This is equivalent to finding a permutation of inputs, outputs, and frequencies simultaneously
    # We can model this as a bipartite matching problem or use backtracking
    
    # Try all possible combinations using backtracking
    def backtrack(index, used_inputs, used_outputs, used_frequencies, selected):
        if len(selected) == k:
            return True
        
        if index >= len(pathways):
            return False
            
        # Try not taking current pathway
        if backtrack(index + 1, used_inputs, used_outputs, used_frequencies, selected):
            return True
            
        # Try taking current pathway if possible
        u, v, w = pathways[index]
        if u not in used_inputs and v not in used_outputs and w not in used_frequencies:
            used_inputs.add(u)
            used_outputs.add(v)
            used_frequencies.add(w)
            selected.append((u, v, w))
            
            if backtrack(index + 1, used_inputs, used_outputs, used_frequencies, selected):
                return True
                
            used_inputs.remove(u)
            used_outputs.remove(v)
            used_frequencies.remove(w)
            selected.pop()
            
        return False
    
    # Optimization: if t < k, impossible
    if t < k:
        print("NO")
        return
    
    selected = []
    if backtrack(0, set(), set(), set(), selected):
        print("YES")
        for u, v, w in selected:
            print(u, v, w)
    else:
        print("NO")

solve()