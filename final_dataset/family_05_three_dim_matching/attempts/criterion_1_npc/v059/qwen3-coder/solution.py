from itertools import combinations

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    groupings = []
    index = 2
    for _ in range(t):
        x = int(data[index])
        y = int(data[index+1])
        z = int(data[index+2])
        groupings.append((x, y, z))
        index += 3
    
    # Try all combinations of k groupings from the t available
    for combo in combinations(range(t), k):
        # Count how many times each part is used
        chassis_count = [0] * (k + 1)
        power_count = [0] * (k + 1)
        logic_count = [0] * (k + 1)
        
        selected_groupings = []
        for i in combo:
            x, y, z = groupings[i]
            chassis_count[x] += 1
            power_count[y] += 1
            logic_count[z] += 1
            selected_groupings.append((x, y, z))
        
        # Check if each part is used exactly once
        valid = True
        for i in range(1, k + 1):
            if chassis_count[i] != 1 or power_count[i] != 1 or logic_count[i] != 1:
                valid = False
                break
        
        if valid:
            print("YES")
            for x, y, z in selected_groupings:
                print(x, y, z)
            return
    
    print("NO")

solve()