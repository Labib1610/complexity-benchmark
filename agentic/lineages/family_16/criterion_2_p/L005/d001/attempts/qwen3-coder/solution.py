import sys
from functools import cmp_to_key

def compare_ships(ship_a, ship_b):
    # ship_a = (t1a, t2a), ship_b = (t1b, t2b)
    # Compare t2a + max(t1a + t2a + t1b, t1b + t2b) vs t2b + max(t1b + t2b + t1a, t1a + t2a)
    # Simplified: compare max(t1a+t2a+t1b+t2b, t1b+t2b+t1a) vs max(t1b+t2b+t1a+t2a, t1a+t2a+t1b)
    # Which is just comparing t1a+t2a+t1b+t2b vs t1b+t2b+t1a+t2a, always equal
    # So we use Johnson's rule:
    # if min(t2a, t1b) < min(t1a, t2b) => ship_a should come before ship_b
    
    t1a, t2a = ship_a
    t1b, t2b = ship_b
    
    # Johnson's algorithm comparison
    if min(t2a, t1b) > min(t1a, t2b):
        return 1
    elif min(t2a, t1b) < min(t1a, t2b):
        return -1
    else:
        return 0

def solve():
    j = int(sys.stdin.readline())
    ships = []
    
    for _ in range(j):
        t1, t2 = map(int, sys.stdin.readline().split())
        ships.append((t1, t2))
    
    # Sort using Johnson's rule
    ships.sort(key=cmp_to_key(compare_ships))
    
    # Simulate processing
    time_stage1 = 0
    time_stage2 = 0
    
    for t1, t2 in ships:
        time_stage1 += t1
        time_stage2 = max(time_stage2, time_stage1) + t2
    
    print(time_stage2)

solve()