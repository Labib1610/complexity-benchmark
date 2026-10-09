import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    j, T = map(int, sys.stdin.readline().split())
    
    items = []
    sum_p1 = 0
    sum_p2 = 0
    
    for i in range(j):
        p1, p2 = map(int, sys.stdin.readline().split())
        items.append((p1, p2))
        sum_p1 += p1
        sum_p2 += p2
        
        # Check JOB condition immediately
        if p1 + p2 > T:
            print(f"JOB {i + 1}")
            return
            
    # If we reach here, no individual job is impossible
    # Check LOAD conditions
    if sum_p1 > T:
        print("LOAD 1")
        return
    if sum_p2 > T:
        print("LOAD 2")
        return

threading.Thread(target=main).start()