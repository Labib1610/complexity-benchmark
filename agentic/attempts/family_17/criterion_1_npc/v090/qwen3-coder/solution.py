def solve():
    import sys
    import random
    
    # For faster input/output
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    t = int(data[1])
    
    units = []
    idx = 2
    for i in range(t):
        a = int(data[idx])
        b = int(data[idx+1])
        c = int(data[idx+2])
        idx += 3
        units.append((a, b, c))
    
    # Try multiple times with different orderings
    for _ in range(min(100, t)):
        # Shuffle the units to try different orders
        random.shuffle(units)
        
        used = [False] * (3*q + 1)
        selected = []
        found = True
        
        for unit in units:
            a, b, c = unit
            if not used[a] and not used[b] and not used[c]:
                used[a] = used[b] = used[c] = True
                selected.append(unit)
                if len(selected) == q:
                    break
        
        if len(selected) == q:
            print("YES")
            for unit in selected:
                print(unit[0], unit[1], unit[2])
            return
    
    # If random approach doesn't work, try greedy approach
    # Sort units by some criteria and try greedy selection
    units.sort()  # Sort by first element
    
    used = [False] * (3*q + 1)
    selected = []
    
    for unit in units:
        a, b, c = unit
        if not used[a] and not used[b] and not used[c]:
            used[a] = used[b] = used[c] = True
            selected.append(unit)
            if len(selected) == q:
                break
    
    if len(selected) == q:
        print("YES")
        for unit in selected:
            print(unit[0], unit[1], unit[2])
        return
    
    # Try another ordering - sort by sum
    units.sort(key=lambda x: x[0] + x[1] + x[2])
    
    used = [False] * (3*q + 1)
    selected = []
    
    for unit in units:
        a, b, c = unit
        if not used[a] and not used[b] and not used[c]:
            used[a] = used[b] = used[c] = True
            selected.append(unit)
            if len(selected) == q:
                break
    
    if len(selected) == q:
        print("YES")
        for unit in selected:
            print(unit[0], unit[1], unit[2])
        return
    
    print("NO")

solve()