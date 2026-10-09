import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    q = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    n = 3 * q
    
    configs = []
    comp_to_configs = defaultdict(list)
    
    for i in range(t):
        a = int(input_data[idx]); idx += 1
        b = int(input_data[idx]); idx += 1
        c = int(input_data[idx]); idx += 1
        configs.append((a, b, c))
        comp_to_configs[a].append(i)
        comp_to_configs[b].append(i)
        comp_to_configs[c].append(i)
    
    # Check every component has at least one config
    for comp in range(1, n + 1):
        if comp not in comp_to_configs or len(comp_to_configs[comp]) == 0:
            print("NO")
            return
    
    used = [False] * (n + 1)
    chosen = []
    
    def backtrack():
        if len(chosen) == q:
            return True
        
        # Find most constrained unprocessed component (MRV)
        best_comp = -1
        best_count = float('inf')
        best_configs = None
        
        for comp in range(1, n + 1):
            if used[comp]:
                continue
            avail = [ci for ci in comp_to_configs[comp] 
                     if not used[configs[ci][0]] and not used[configs[ci][1]] and not used[configs[ci][2]]]
            cnt = len(avail)
            if cnt == 0:
                return False
            if cnt < best_count:
                best_count = cnt
                best_comp = comp
                best_configs = avail
                if cnt == 1:
                    break
        
        if best_comp == -1:
            return len(chosen) == q
        
        # Try each available config for the most constrained component
        for ci in best_configs:
            a, b, c = configs[ci]
            if used[a] or used[b] or used[c]:
                continue
            used[a] = used[b] = used[c] = True
            chosen.append(ci)
            
            if backtrack():
                return True
            
            chosen.pop()
            used[a] = used[b] = used[c] = False
        
        return False
    
    if backtrack():
        print("YES")
        for ci in chosen:
            a, b, c = configs[ci]
            print(f"{a} {b} {c}")
    else:
        print("NO")

solve()