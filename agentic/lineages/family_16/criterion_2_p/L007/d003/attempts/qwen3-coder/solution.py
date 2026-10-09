import sys
from collections import deque

def solve():
    j = int(sys.stdin.readline())
    manuscripts = []
    for _ in range(j):
        p1, p2 = map(int, sys.stdin.readline().split())
        manuscripts.append((p1, p2))
    
    # Sort manuscripts by p1 (historian time) in descending order
    # This is because we want to process longer historian times first
    # to minimize the total time
    manuscripts.sort(key=lambda x: x[0], reverse=True)
    
    # Simulate the process
    historian_finish_time = 0
    conservator_finish_time = 0
    
    # For each manuscript in the sorted order
    for p1, p2 in manuscripts:
        # Historian finishes examining this manuscript at this time
        historian_finish_time += p1
        
        # Conservator can start working on this manuscript only after:
        # 1. Historian finishes examining it (historian_finish_time)
        # 2. Conservator is free (conservator_finish_time)
        # So conservator starts at max(historian_finish_time, conservator_finish_time)
        conservator_start_time = max(historian_finish_time, conservator_finish_time)
        
        # Conservator finishes at start_time + p2
        conservator_finish_time = conservator_start_time + p2
    
    print(conservator_finish_time)

solve()