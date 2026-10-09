from itertools import combinations

def solve():
    n, m, k = map(int, input().split())
    
    # Create adjacency list
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].add(v)
        adj[v].add(u)
    
    # Special case: k = 1
    if k == 1:
        print("YES")
        print(1)
        return
    
    # For small n, try all combinations
    if n <= 20:
        users = list(range(1, n + 1))
        for combo in combinations(users, k):
            valid = True
            for i in range(len(combo)):
                for j in range(i + 1, len(combo)):
                    if combo[j] in adj[combo[i]]:
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                print("YES")
                print(*combo)
                return
        print("NO")
        return
    
    # For larger n, use meet-in-the-middle approach
    # Split vertices into two halves
    mid = n // 2
    left_vertices = list(range(1, mid + 1))
    right_vertices = list(range(mid + 1, n + 1))
    
    # Generate all valid subsets for left side
    left_valid = {}
    for i in range(min(k + 1, len(left_vertices) + 1)):
        for combo in combinations(left_vertices, i):
            # Check if this subset is valid (no edges within)
            valid = True
            for x in range(len(combo)):
                for y in range(x + 1, len(combo)):
                    if combo[y] in adj[combo[x]]:
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                left_valid[combo] = set(combo)
    
    # Generate all valid subsets for right side
    right_valid = {}
    for i in range(min(k + 1, len(right_vertices) + 1)):
        for combo in combinations(right_vertices, i):
            # Check if this subset is valid (no edges within)
            valid = True
            for x in range(len(combo)):
                for y in range(x + 1, len(combo)):
                    if combo[y] in adj[combo[x]]:
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                right_valid[combo] = set(combo)
    
    # Check all combinations of left and right subsets
    for left_combo, left_set in left_valid.items():
        left_size = len(left_combo)
        needed_right = k - left_size
        
        if needed_right < 0:
            continue
            
        for right_combo, right_set in right_valid.items():
            if len(right_combo) != needed_right:
                continue
                
            # Check if no edges between left and right
            valid = True
            for u in left_combo:
                for v in right_combo:
                    if v in adj[u]:
                        valid = False
                        break
                if not valid:
                    break
            
            if valid:
                result = list(left_combo) + list(right_combo)
                print("YES")
                print(*result)
                return
    
    print("NO")

solve()