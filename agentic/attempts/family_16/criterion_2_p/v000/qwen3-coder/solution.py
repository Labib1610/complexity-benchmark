import sys
from functools import cmp_to_key

def compare_jobs(job1, job2):
    # Johnson's rule comparison
    # job1 = (p1_a, p2_a), job2 = (p1_b, p2_b)
    # if min(p1_a, p2_b) < min(p1_b, p2_a) then job1 should come before job2
    a_p1, a_p2 = job1
    b_p1, b_p2 = job2
    
    if min(a_p1, b_p2) < min(b_p1, a_p2):
        return -1
    elif min(a_p1, b_p2) > min(b_p1, a_p2):
        return 1
    else:
        return 0

def main():
    j = int(sys.stdin.readline())
    jobs = []
    
    for _ in range(j):
        p1, p2 = map(int, sys.stdin.readline().split())
        jobs.append((p1, p2))
    
    # Sort according to Johnson's rule
    jobs.sort(key=cmp_to_key(compare_jobs))
    
    # Simulate the processing
    time_m1 = 0  # Current time on machine 1
    time_m2 = 0  # Current time on machine 2
    
    for p1, p2 in jobs:
        # Machine 1 finishes this job at time_m1 + p1
        time_m1 += p1
        # Machine 2 can start this job only after both:
        # 1. Machine 1 finishes it (time_m1)
        # 2. Machine 2 is free (time_m2)
        # So it starts at max(time_m1, time_m2) and finishes at max(time_m1, time_m2) + p2
        time_m2 = max(time_m1, time_m2) + p2
    
    print(time_m2)

if __name__ == "__main__":
    main()