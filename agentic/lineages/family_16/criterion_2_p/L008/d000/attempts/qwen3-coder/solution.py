import sys
import threading

def main():
    import sys
    j = int(sys.stdin.readline())
    jobs = []
    for _ in range(j):
        p1, p2 = map(int, sys.stdin.readline().split())
        jobs.append((p1, p2))
    
    # Sort jobs by p1 ascending, then by p2 descending
    # This is the optimal ordering for minimizing the maximum completion time
    jobs.sort(key=lambda x: (x[0], -x[1]))
    
    # Simulate the process
    time_a = 0  # Time when Artist A finishes the current job
    time_b = 0  # Time when Artist B finishes the current job
    
    for p1, p2 in jobs:
        time_a += p1
        time_b = max(time_a, time_b) + p2
    
    print(time_b)

# Use threading to increase recursion limit for large inputs
threading.Thread(target=main).start()