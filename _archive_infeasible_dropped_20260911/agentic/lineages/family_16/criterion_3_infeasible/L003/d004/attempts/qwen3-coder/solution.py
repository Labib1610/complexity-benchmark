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
    
    # Check for JOB certificate
    for i in range(j):
        p1, p2 = jobs[i]
        # Minimum end time for entity i in domain 2:
        # S1 >= 0 => E1 >= p1 => S2 >= E1 >= p1 => E2 >= S2 + p2 >= p1 + p2
        min_end_time = p1 + p2
        if min_end_time > T:
            print(f"JOB {i+1}")
            return
    
    # Check for LOAD certificate
    # For domain 1:
    spans1 = [p1 for p1, _ in jobs]
    total_span1 = sum(spans1)
    # In the worst case (no overlaps allowed), we need at least total_span1 time
    if total_span1 > T:
        print("LOAD 1")
        return
        
    # For domain 2:
    spans2 = [p2 for _, p2 in jobs]
    total_span2 = sum(spans2)
    if total_span2 > T:
        print("LOAD 2")
        return

threading.Thread(target=main).start()