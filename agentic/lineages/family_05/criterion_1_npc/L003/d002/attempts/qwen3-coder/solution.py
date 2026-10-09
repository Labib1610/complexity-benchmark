from itertools import permutations

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    configs = []
    idx = 2
    for _ in range(t):
        x = int(data[idx])
        y = int(data[idx+1])
        z = int(data[idx+2])
        configs.append((x, y, z))
        idx += 3
    
    # We need to pick k configurations such that each stone (1 to k) appears exactly once in each position
    # This is essentially finding a perfect matching in a tripartite hypergraph
    
    # Try all combinations of k configurations from the t available
    from itertools import combinations
    
    for combo in combinations(range(t), k):
        # For each combination, check if we can assign the stones 1..k to each position uniquely
        selected_configs = [configs[i] for i in combo]
        
        # Try all permutations of these configs to see if we can match each stone exactly once
        for perm in permutations(selected_configs):
            # Check if this permutation uses each stone 1..k exactly once in each position
            left_used = [False] * (k + 1)
            right_used = [False] * (k + 1)
            keystone_used = [False] * (k + 1)
            
            valid = True
            for x, y, z in perm:
                if left_used[x] or right_used[y] or keystone_used[z]:
                    valid = False
                    break
                left_used[x] = True
                right_used[y] = True
                keystone_used[z] = True
            
            if valid and all(left_used[1:k+1]) and all(right_used[1:k+1]) and all(keystone_used[1:k+1]):
                print("YES")
                for cfg in perm:
                    print(cfg[0], cfg[1], cfg[2])
                return
    
    print("NO")

solve()