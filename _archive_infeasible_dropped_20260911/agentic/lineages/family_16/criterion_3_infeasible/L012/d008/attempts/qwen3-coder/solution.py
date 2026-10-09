import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    j, T = map(int, sys.stdin.readline().split())
    jobs = []
    for i in range(j):
        p1, p2 = map(int, sys.stdin.readline().split())
        jobs.append((p1, p2))
    
    # Check JOB i: individual job exceeds T
    for i in range(j):
        p1, p2 = jobs[i]
        if p1 + p2 > T:
            print(f"JOB {i+1}")
            return
    
    # Check LOAD 1: sum of all p1 > T
    sum_p1 = sum(p1 for p1, p2 in jobs)
    if sum_p1 > T:
        print("LOAD 1")
        return
    
    # Check LOAD 2: sum of all p2 > T
    sum_p2 = sum(p2 for p1, p2 in jobs)
    if sum_p2 > T:
        print("LOAD 2")
        return

threading.Thread(target=main).start()