import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    k = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    # Group profiles by operator
    profiles_by_op = [[] for _ in range(k + 1)]
    for _ in range(t):
        x = int(input_data[idx]); idx += 1
        y = int(input_data[idx]); idx += 1
        z = int(input_data[idx]); idx += 1
        profiles_by_op[x].append((y, z))
    
    # Check each operator has at least one profile
    for i in range(1, k + 1):
        if not profiles_by_op[i]:
            print("NO")
            return
    
    used_t = 0  # used terminals bitmask
    used_s = 0  # used shifts bitmask
    result = [None] * k
    
    # Precompute for pruning: for operators i..k, what terminals and shifts are available
    # available_terminals[i] = set of terminals used by operators i..k
    avail_t = [0] * (k + 2)
    avail_s = [0] * (k + 2)
    for i in range(k, 0, -1):
        at = 0
        as_ = 0
        for (y, z) in profiles_by_op[i]:
            at |= (1 << (y - 1))
            as_ |= (1 << (z - 1))
        avail_t[i] = at
        avail_s[i] = as_
    
    def backtrack(op, used_t, used_s):
        if op > k:
            return True
        # Pruning: remaining operators must cover remaining terminals and shifts
        # Actually, we need: for operators op..k, the union of their available terminals
        # must include all unused terminals, and similarly for shifts.
        # More precisely: unused terminals must be subset of avail_t[op..k]
        remaining_t_mask = ((1 << k) - 1) & ~used_t
        remaining_s_mask = ((1 << k) - 1) & ~used_s
        
        # Count remaining
        rem_t_count = bin(remaining_t_mask).count('1')
        rem_s_count = bin(remaining_s_mask).count('1')
        ops_left = k - op + 1
        if rem_t_count > ops_left or rem_s_count > ops_left:
            return False
        
        # Check if remaining terminals are coverable
        combined_t = 0
        combined_s = 0
        for i in range(op, k + 1):
            combined_t |= avail_t[i]
            combined_s |= avail_s[i]
        if (remaining_t_mask & combined_t) != remaining_t_mask:
            return False
        if (remaining_s_mask & combined_s) != remaining_s_mask:
            return False
        
        for (y, z) in profiles_by_op[op]:
            yt = 1 << (y - 1)
            zs = 1 << (z - 1)
            if not (used_t & yt) and not (used_s & zs):
                result[op - 1] = (op, y, z)
                if backtrack(op + 1, used_t | yt, used_s | zs):
                    return True
        return False
    
    if backtrack(1, 0, 0):
        print("YES")
        for i in range(k):
            print(f"{result[i][0]} {result[i][1]} {result[i][2]}")
    else:
        print("NO")

solve()