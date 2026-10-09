import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(input_data[idx]); idx += 1
    T = int(input_data[idx]); idx += 1
    
    p1 = [0] * j
    p2 = [0] * j
    
    for i in range(j):
        p1[i] = int(input_data[idx]); idx += 1
        p2[i] = int(input_data[idx]); idx += 1
    
    # Check LOAD 1: set all p2 = 0, B_j = sum(p1)
    if sum(p1) > T:
        print("LOAD 1")
        return
    
    # Check LOAD 2: set all p1 = 0, B_j = sum(p2)
    if sum(p2) > T:
        print("LOAD 2")
        return
    
    # Otherwise, must be JOB obstruction
    # For job i alone (all others 0): B_j = p1[i] + p2[i]
    # Find any i where p1[i] + p2[i] > T
    for i in range(j):
        if p1[i] + p2[i] > T:
            print(f"JOB {i+1}")
            return

solve()