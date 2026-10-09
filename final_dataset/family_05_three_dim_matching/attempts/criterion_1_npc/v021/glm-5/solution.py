import sys
from functools import lru_cache

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    k = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    points_by_x = [[] for _ in range(k + 1)]
    for _ in range(t):
        x = int(input_data[idx]); idx += 1
        y = int(input_data[idx]); idx += 1
        z = int(input_data[idx]); idx += 1
        points_by_x[x].append((y, z))
    
    # Check each x has at least one point
    for i in range(1, k + 1):
        if not points_by_x[i]:
            print("NO")
            return
    
    # Recursive search with memoization
    # State: (x_index, y_mask, z_mask) where x_index = number of x's processed + 1
    # We process x from 1 to k
    
    solution = [None] * k
    found = [False]
    
    # Use iterative deepening or just DFS with pruning
    # For k up to 22, bitmasks fit in int
    
    import sys
    sys.setrecursionlimit(10000)
    
    memo = set()
    
    def dfs(x_idx, y_mask, z_mask):
        if found[0]:
            return True
        if x_idx > k:
            found[0] = True
            return True
        
        state = (x_idx, y_mask, z_mask)
        if state in memo:
            return False
        
        for (y, z) in points_by_x[x_idx]:
            y_bit = 1 << (y - 1)
            z_bit = 1 << (z - 1)
            if not (y_mask & y_bit) and not (z_mask & z_bit):
                solution[x_idx - 1] = (x_idx, y, z)
                if dfs(x_idx + 1, y_mask | y_bit, z_mask | z_bit):
                    return True
                solution[x_idx - 1] = None
        
        memo.add(state)
        return False
    
    if dfs(1, 0, 0):
        print("YES")
        for s in solution:
            print(f"{s[0]} {s[1]} {s[2]}")
    else:
        print("NO")

solve()