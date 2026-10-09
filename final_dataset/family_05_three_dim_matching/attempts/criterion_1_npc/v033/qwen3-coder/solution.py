from itertools import permutations

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
    
    # Try all permutations of k combinations from the list
    from itertools import combinations as iter_combinations
    
    for comb_indices in iter_combinations(range(t), k):
        selected = [combinations[i] for i in comb_indices]
        
        # Check if specialists, machines, and time slots are unique
        specialists = [crew[0] for crew in selected]
        machines = [crew[1] for crew in selected]
        time_slots = [crew[2] for crew in selected]
        
        if len(set(specialists)) == k and len(set(machines)) == k and len(set(time_slots)) == k:
            print("YES")
            for crew in selected:
                print(crew[0], crew[1], crew[2])
            return
    
    print("NO")

solve()