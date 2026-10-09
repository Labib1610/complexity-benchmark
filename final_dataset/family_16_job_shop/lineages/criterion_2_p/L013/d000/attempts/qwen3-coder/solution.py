import sys
from functools import cmp_to_key

def compare_jobs(job1, job2):
    # Johnson's rule comparison
    # If min(a1, b2) < min(a2, b1), then job1 should come before job2
    a1, b1 = job1
    a2, b2 = job2
    if min(a1, b2) < min(a2, b1):
        return -1
    elif min(a1, b2) > min(a2, b1):
        return 1
    else:
        return 0

def main():
    j = int(sys.stdin.readline())
    jobs = []
    
    for _ in range(j):
        p1, p2 = map(int, sys.stdin.readline().split())
        jobs.append((p1, p2))
    
    # Sort jobs according to Johnson's rule
    jobs.sort(key=cmp_to_key(compare_jobs))
    
    # Calculate the minimum completion time
    time_m1 = 0  # Time when machine 1 becomes free
    time_m2 = 0  # Time when machine 2 becomes free
    
    for p1, p2 in jobs:
        time_m1 += p1
        time_m2 = max(time_m1, time_m2) + p2
    
    print(time_m2)

if __name__ == "__main__":
    main()