from itertools import permutations

def solve():
    k, t = map(int, input().split())
    
    if t == 0:
        if k == 0:
            print("YES")
        else:
            print("NO")
        return
    
    combinations = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        combinations.append((x, y, z))
    
    # Try all possible subsets of k combinations
    from itertools import combinations as iter_combinations
    
    for selected in iter_combinations(range(t), k):
        # Get the actual combinations
        chosen = [combinations[i] for i in selected]
        
        # Check if all technicians, rigs, and windows are unique
        techs = set()
        rigs = set()
        windows = set()
        
        valid = True
        for x, y, z in chosen:
            if x in techs or y in rigs or z in windows:
                valid = False
                break
            techs.add(x)
            rigs.add(y)
            windows.add(z)
        
        if valid and len(techs) == k and len(rigs) == k and len(windows) == k:
            print("YES")
            for x, y, z in chosen:
                print(x, y, z)
            return
    
    print("NO")

solve()