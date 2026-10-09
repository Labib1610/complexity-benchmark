import sys
from functools import cmp_to_key

def compare_jobs(job1, job2):
    # job = (p1, p2, index)
    # Compare job1 followed by job2 vs job2 followed by job1
    p1_1, p2_1 = job1[0], job1[1]
    p1_2, p2_2 = job2[0], job2[1]
    
    # Time if we do job1 then job2
    time1 = max(p1_1 + p2_1 + p2_2, p1_1 + p1_2 + p2_2)
    # Time if we do job2 then job1
    time2 = max(p1_2 + p2_2 + p2_1, p1_2 + p1_1 + p2_1)
    
    if time1 < time2:
        return -1
    elif time1 > time2:
        return 1
    else:
        return 0

def main():
    j = int(sys.stdin.readline())
    jobs = []
    
    for i in range(j):
        p1, p2 = map(int, sys.stdin.readline().split())
        jobs.append((p1, p2))
    
    # Sort jobs using the custom comparator
    # For better performance, we can use Johnson's rule instead of pairwise comparison
    # Johnson's rule: 
    # - If min(p1, p2) == p1, prefer smaller p1 (ascending)
    # - If min(p1, p2) == p2, prefer larger p2 (descending)
    # But let's implement a simpler O(n log n) approach
    
    # Apply Johnson's rule sorting
    def johnson_key(job):
        p1, p2 = job
        if p1 <= p2:
            return (0, p1)  # First group: p1 <= p2, sort by p1 ascending
        else:
            return (1, -p2)  # Second group: p1 > p2, sort by p2 descending
    
    jobs.sort(key=johnson_key)
    
    # Calculate the total completion time
    primary_time = 0
    secondary_time = 0
    
    for p1, p2 in jobs:
        primary_time += p1
        secondary_time = max(secondary_time + p2, primary_time + p2)
    
    print(secondary_time)

if __name__ == "__main__":
    main()