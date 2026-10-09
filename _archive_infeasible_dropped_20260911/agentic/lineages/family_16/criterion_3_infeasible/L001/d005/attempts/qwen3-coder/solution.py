import sys
import threading

def main():
    import sys
    j, T = map(int, sys.stdin.readline().split())
    
    items = []
    total_p1 = 0
    total_p2 = 0
    
    for i in range(j):
        p1, p2 = map(int, sys.stdin.readline().split())
        items.append((p1, p2))
        total_p1 += p1
        total_p2 += p2
        
        # Check for individual feasibility
        if p1 + p2 > T:
            print(f"JOB {i+1}")
            return
            
    # Check for machine saturation
    if total_p1 > T:
        print("LOAD 1")
        return
        
    if total_p2 > T:
        print("LOAD 2")
        return

threading.Thread(target=main).start()