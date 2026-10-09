from itertools import permutations

def solve():
    k, t = map(int, input().split())
    configs = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        configs.append((x, y, z))
    
    if k == 0:
        print("YES")
        return
    
    # Try all possible permutations of k configurations
    for perm in permutations(configs, k):
        specialists = set()
        machines = set()
        time_slots = set()
        
        valid = True
        for x, y, z in perm:
            if x in specialists or y in machines or z in time_slots:
                valid = False
                break
            specialists.add(x)
            machines.add(y)
            time_slots.add(z)
        
        if valid and len(specialists) == k and len(machines) == k and len(time_slots) == k:
            print("YES")
            for x, y, z in perm:
                print(x, y, z)
            return
    
    print("NO")

solve()