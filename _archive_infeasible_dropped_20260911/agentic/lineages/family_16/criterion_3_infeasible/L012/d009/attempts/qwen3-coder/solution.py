import sys
import threading

def main():
    import sys
    j, T = map(int, sys.stdin.readline().split())
    jobs = []
    sum_p1 = 0
    max_p2 = 0
    
    for i in range(j):
        p1, p2 = map(int, sys.stdin.readline().split())
        jobs.append((p1, p2))
        sum_p1 += p1
        if p2 > max_p2:
            max_p2 = p2
            
    # Experiment 1: Check if any job itself takes more than T
    for i in range(j):
        p1, p2 = jobs[i]
        if p1 + p2 > T:
            print(f"JOB {i+1}")
            return
            
    # Experiment 2: LOAD 1 - Serial capacitor charges, init time = 0
    # Total time = sum of all p1 (since p2=0 and no init grid limit)
    if sum_p1 > T:
        print("LOAD 1")
        return
        
    # Experiment 3: LOAD 2 - Serial system initializations, charge time = 0
    # Total time = max(p1) + sum of all p2 (since p1=0 and no cap grid limit)
    max_p1 = 0
    sum_p2 = 0
    for p1, p2 in jobs:
        if p1 > max_p1:
            max_p1 = p1
        sum_p2 += p2
        
    if max_p1 + sum_p2 > T:
        print("LOAD 2")
        return

# Run main in a separate thread to avoid recursion limit issues
threading.Thread(target=main).start()