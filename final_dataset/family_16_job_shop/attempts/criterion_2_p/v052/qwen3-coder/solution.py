import sys
from functools import cmp_to_key

def compare_cores(core_a, core_b):
    # core = (p1, p2, index)
    # Johnson's rule: 
    # if p1_a < p2_a and p1_b > p2_b, then a should come before b
    # if p1_a > p2_a and p1_b < p2_b, then b should come before a
    # otherwise, sort by min(p1_a, p2_b) vs min(p1_b, p2_a)
    
    p1_a, p2_a = core_a[0], core_a[1]
    p1_b, p2_b = core_b[0], core_b[1]
    
    # If both are in the same group, sort by p1 ascending for group 1 (p1 <= p2) 
    # and by p2 descending for group 2 (p1 > p2)
    if (p1_a <= p2_a) and (p1_b <= p2_b):
        # Both in group 1: sort by p1 ascending
        return p1_a - p1_b
    elif (p1_a > p2_a) and (p1_b > p2_b):
        # Both in group 2: sort by p2 descending
        return p2_b - p2_a
    elif (p1_a <= p2_a) and (p1_b > p2_b):
        # a in group 1, b in group 2: a comes first
        return -1
    elif (p1_a > p2_a) and (p1_b <= p2_b):
        # a in group 2, b in group 1: b comes first
        return 1
    else:
        # Tie-breaker
        return p1_a - p1_b

def solve():
    j = int(sys.stdin.readline())
    cores = []
    for i in range(j):
        p1, p2 = map(int, sys.stdin.readline().split())
        cores.append((p1, p2))
        
    # Apply Johnson's algorithm for F2||Cmax
    # Sort jobs according to Johnson's rule:
    # 1. Group jobs where p1 <= p2 (group A) and p1 > p2 (group B)
    # 2. Within group A, sort by p1 ascending
    # 3. Within group B, sort by p2 descending
    
    group_A = []  # p1 <= p2, sort by p1 ascending
    group_B = []  # p1 > p2, sort by p2 descending
    
    for i in range(j):
        p1, p2 = cores[i]
        if p1 <= p2:
            group_A.append((p1, p2, i))
        else:
            group_B.append((p1, p2, i))
            
    group_A.sort(key=lambda x: x[0])  # Sort by p1 ascending
    group_B.sort(key=lambda x: x[1], reverse=True)  # Sort by p2 descending
    
    # Final sequence: group_A + group_B
    sequence = group_A + group_B
    
    # Simulate the process
    excite_finish_times = [0] * j
    dampen_finish_times = [0] * j
    
    excite_time = 0
    for i in range(j):
        _, p1, p2 = sequence[i][0], sequence[i][0], sequence[i][1]
        excite_time += p1
        excite_finish_times[i] = excite_time
        
    dampen_time = 0
    for i in range(j):
        p1, p2 = sequence[i][0], sequence[i][1]
        # Dampening can start when both excitation finishes and previous dampening finishes
        dampen_start = max(excite_finish_times[i], dampen_time)
        dampen_time = dampen_start + p2
        dampen_finish_times[i] = dampen_time
        
    print(dampen_finish_times[-1])

solve()