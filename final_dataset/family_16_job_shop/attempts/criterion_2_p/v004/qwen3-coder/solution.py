import sys
import threading

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    jobs = []
    for i in range(j):
        p1 = int(data[2*i + 1])
        p2 = int(data[2*i + 2])
        jobs.append((p1, p2))
    
    # Sort jobs according to Johnson's rule:
    # Jobs with p1 <= p2 come first, sorted by p1 ascending
    # Jobs with p1 > p2 come later, sorted by p2 descending
    def johnson_key(job):
        p1, p2 = job
        if p1 <= p2:
            return (0, p1)
        else:
            return (1, -p2)
    
    jobs.sort(key=johnson_key)
    
    # Simulate the schedule
    time_m1 = 0
    time_m2 = 0
    for p1, p2 in jobs:
        time_m1 += p1
        time_m2 = max(time_m2, time_m1) + p2
    
    print(time_m2)

threading.Thread(target=main).start()