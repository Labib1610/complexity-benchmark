import sys
from functools import cmp_to_key

def compare(vessel1, vessel2):
    # Compare two vessels for sorting
    # This is based on Johnson's rule for F2||Cmax (flow shop scheduling)
    # Compare min(a1, b2) vs min(a2, b1)
    a1, b1 = vessel1
    a2, b2 = vessel2
    
    x = min(a1, b2)
    y = min(a2, b1)
    
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        # If tie, we can use secondary criteria or just keep original order
        # But for consistency, let's break ties by a_i + b_i ascending
        sum1 = a1 + b1
        sum2 = a2 + b2
        if sum1 < sum2:
            return -1
        elif sum1 > sum2:
            return 1
        else:
            return 0

def solve():
    j = int(sys.stdin.readline())
    vessels = []
    
    for _ in range(j):
        t1, t2 = map(int, sys.stdin.readline().split())
        vessels.append((t1, t2))
    
    # Sort according to Johnson's rule
    vessels.sort(key=cmp_to_key(compare))
    
    # Simulate the process
    alpha_end_time = 0  # When the current vessel finishes Alpha
    beta_end_time = 0   # When the previous vessel finishes Beta
    
    for a, b in vessels:
        # Alpha phase starts when the previous vessel finishes Alpha
        alpha_end_time += a
        
        # Beta phase can start when both:
        # 1. This vessel finishes Alpha (alpha_end_time)
        # 2. Previous vessel finishes Beta (beta_end_time)
        # So Beta starts at max(alpha_end_time, beta_end_time)
        beta_start = max(alpha_end_time, beta_end_time)
        beta_end_time = beta_start + b
    
    print(beta_end_time)

solve()