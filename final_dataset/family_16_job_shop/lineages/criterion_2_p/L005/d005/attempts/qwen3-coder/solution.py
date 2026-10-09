import sys
from typing import List, Tuple

def solve():
    j = int(sys.stdin.readline())
    vessels = []
    for _ in range(j):
        t1, t2 = map(int, sys.stdin.readline().split())
        vessels.append((t1, t2))
    
    # Sort vessels by t1 ascending, and by t2 descending if t1 is equal
    # This is the optimal strategy: vessels with smaller t1 should go first
    # If t1 is equal, vessels with larger t2 should go first
    vessels.sort(key=lambda x: (x[0], -x[1]))
    
    alpha_end_time = 0  # Time when the current alpha phase ends
    beta_end_time = 0   # Time when the last beta phase ends
    
    for t1, t2 in vessels:
        # Alpha phase starts when the previous alpha phase ends
        alpha_start_time = alpha_end_time
        alpha_end_time = alpha_start_time + t1
        
        # Beta phase can start only when:
        # 1. Own alpha phase ends (alpha_end_time)
        # 2. Previous vessel's beta phase ends (beta_end_time)
        beta_start_time = max(alpha_end_time, beta_end_time)
        beta_end_time = beta_start_time + t2
    
    print(beta_end_time)

solve()