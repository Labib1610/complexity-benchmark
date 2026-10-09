import sys
from functools import lru_cache

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    k = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    # Group combinations by technician
    by_tech = [[] for _ in range(k + 1)]
    for _ in range(t):
        x = int(input_data[idx]); idx += 1
        y = int(input_data[idx]); idx += 1
        z = int(input_data[idx]); idx += 1
        by_tech[x].append((y - 1, z - 1))  # 0-indexed
    
    # Check each technician has at least one option
    for i in range(1, k + 1):
        if not by_tech[i]:
            print("NO")
            return
    
    # Order technicians by number of options (fewest first for better pruning)
    tech_order = list(range(1, k + 1))
    tech_order.sort(key=lambda x: len(by_tech[x]))
    
    full_mask = (1 << k) - 1
    result = [None] * k
    
    # Backtracking with memoization of dead-end states
    dead_states = set()
    
    def backtrack(pos, used_y, used_z):
        if pos == k:
            return True
        key = (pos, used_y, used_z)
        if key in dead_states:
            return False
        
        tech = tech_order[pos]
        for (y, z) in by_tech[tech]:
            ybit = 1 << y
            zbit = 1 << z
            if not (used_y & ybit) and not (used_z & zbit):
                result[pos] = (tech, y + 1, z + 1)
                if backtrack(pos + 1, used_y | ybit, used_z | zbit):
                    return True
                result[pos] = None
        
        dead_states.add(key)
        return False
    
    if backtrack(0, 0, 0):
        print("YES")
        for r in result:
            print(f"{r[0]} {r[1]} {r[2]}")
    else:
        print("NO")

solve()