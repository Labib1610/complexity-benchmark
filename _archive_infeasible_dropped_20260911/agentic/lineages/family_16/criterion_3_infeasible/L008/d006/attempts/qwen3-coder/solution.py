import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    j, T = map(int, sys.stdin.readline().split())
    jobs = []
    for _ in range(j):
        p1, p2 = map(int, sys.stdin.readline().split())
        jobs.append((p1, p2))
    
    # Check for JOB i violations
    for i in range(j):
        p1, p2 = jobs[i]
        # A job violates JOB i if p1 + p2 > T
        # Because of condition 2: G_k(t) must reach p1 before S_k(t) can increase
        # So S_k(t) has at most (T - p1) time to increase to p2
        # Hence we need p1 + p2 <= T
        if p1 + p2 > T:
            print(f"JOB {i+1}")
            return
    
    # Check for LOAD 1 violation
    total_p1 = sum(p1 for p1, _ in jobs)
    if total_p1 > T:
        print("LOAD 1")
        return
        
    # Check for LOAD 2 violation
    total_p2 = sum(p2 for _, p2 in jobs)
    if total_p2 > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    threading.Thread(target=main).start()