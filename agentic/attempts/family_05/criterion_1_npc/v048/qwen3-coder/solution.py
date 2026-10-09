from itertools import permutations

def solve():
    k, t = map(int, input().split())
    
    if t < k:
        print("NO")
        return
    
    configs = []
    for _ in range(t):
        c, e, g = map(int, input().split())
        configs.append((c, e, g))
    
    # Try all permutations of k configurations
    for perm in permutations(configs, k):
        # Check if this permutation uses each component exactly once
        chassis_used = [0] * (k + 1)
        cores_used = [0] * (k + 1)
        payloads_used = [0] * (k + 1)
        
        valid = True
        for c, e, g in perm:
            chassis_used[c] += 1
            cores_used[e] += 1
            payloads_used[g] += 1
            
            # If any component is used more than once, this permutation is invalid
            if chassis_used[c] > 1 or cores_used[e] > 1 or payloads_used[g] > 1:
                valid = False
                break
        
        # If all components are used exactly once
        if valid and all(chassis_used[i] == 1 for i in range(1, k+1)) and \
           all(cores_used[i] == 1 for i in range(1, k+1)) and \
           all(payloads_used[i] == 1 for i in range(1, k+1)):
            print("YES")
            for c, e, g in perm:
                print(c, e, g)
            return
    
    print("NO")

solve()