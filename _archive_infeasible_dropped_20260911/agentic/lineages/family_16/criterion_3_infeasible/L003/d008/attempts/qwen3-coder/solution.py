import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    j, T = map(int, sys.stdin.readline().split())
    teams = []
    sum_p1 = 0
    sum_p2 = 0
    
    for i in range(j):
        p1, p2 = map(int, sys.stdin.readline().split())
        teams.append((p1, p2))
        sum_p1 += p1
        sum_p2 += p2
    
    # Check LOAD 1: sum of all primary vehicles > T
    if sum_p1 > T:
        print("LOAD 1")
        return
    
    # Check LOAD 2: sum of all secondary vehicles > T
    if sum_p2 > T:
        print("LOAD 2")
        return
    
    # Check JOB i: p1_i + p2_i > T
    for i in range(j):
        p1, p2 = teams[i]
        if p1 + p2 > T:
            print(f"JOB {i+1}")
            return

threading.Thread(target=main).start()