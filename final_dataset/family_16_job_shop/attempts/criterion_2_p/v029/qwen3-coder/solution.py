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
    jobs.sort(key=lambda x: (x[0], -x[1]))
    
    # Calculate the minimum finish time
    time_a = 0  # Time when Artist A finishes current job
    time_b = 0  # Time when Artist B finishes current job
    
    for p1, p2 in jobs:
        time_a += p1
        time_b = max(time_a, time_b) + p2
    
    print(time_b)

# Run the main function in a thread with increased stack size
threading.Thread(target=main).start()