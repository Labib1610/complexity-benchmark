import sys
from typing import List, Tuple

def solve():
    j = int(sys.stdin.readline())
    checkpoints = []
    
    for _ in range(j):
        p1, p2 = map(int, sys.stdin.readline().split())
        checkpoints.append((p1, p2))
    
    # Sort by p1 in descending order
    # This is the optimal strategy - we want to process checkpoints with larger p1 first
    # because they give the Hauler more time to work while the Scout is doing inspections
    checkpoints.sort(key=lambda x: x[0], reverse=True)
    
    # Simulate the process
    scout_time = 0      # Time when Scout finishes current inspection
    hauler_time = 0     # Time when Hauler finishes current extraction
    
    for p1, p2 in checkpoints:
        # Scout does inspection
        scout_time += p1
        
        # Hauler can start extraction only after Scout finishes inspection
        # and after finishing previous extraction
        hauler_start = max(scout_time, hauler_time)
        
        # Hauler does extraction
        hauler_time = hauler_start + p2
    
    print(hauler_time)

solve()