from itertools import combinations

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    profiles = []
    index = 2
    for _ in range(t):
        x = int(data[index])
        y = int(data[index+1])
        z = int(data[index+2])
        profiles.append((x, y, z))
        index += 3
    
    # Try all combinations of k profiles
    for combo in combinations(range(t), k):
        operators = set()
        terminals = set()
        shifts = set()
        
        valid = True
        selected_profiles = []
        
        for i in combo:
            x, y, z = profiles[i]
            if x in operators or y in terminals or z in shifts:
                valid = False
                break
            operators.add(x)
            terminals.add(y)
            shifts.add(z)
            selected_profiles.append((x, y, z))
        
        if valid and len(operators) == k and len(terminals) == k and len(shifts) == k:
            print("YES")
            for profile in selected_profiles:
                print(profile[0], profile[1], profile[2])
            return
    
    print("NO")

solve()