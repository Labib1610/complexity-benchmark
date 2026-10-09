import sys
from functools import cmp_to_key

def compare_jobs(job1, job2):
    # job1 = (p1, p2, index)
    # Johnson's rule: compare p1 + max(p2, p1') vs p1' + max(p2', p1)
    p1a, p2a, _ = job1
    p1b, p2b, _ = job2
    
    # This is based on the optimal scheduling for two machines
    # We want to minimize the makespan
    # The comparison function for Johnson's algorithm
    if p1a <= p2a and p1b <= p2b:
        # Both are type 1 (p1 <= p2), order by p1 ascending
        return p1a - p1b
    elif p1a >= p2a and p1b >= p2b:
        # Both are type 2 (p1 >= p2), order by p2 descending
        return p2b - p2a
    elif p1a <= p2a and p1b >= p2b:
        # job1 is type 1, job2 is type 2, job1 should come first
        return -1
    else:
        # job1 is type 2, job2 is type 1, job2 should come first
        return 1

def main():
    j = int(sys.stdin.readline())
    jobs = []
    
    for i in range(j):
        p1, p2 = map(int, sys.stdin.readline().split())
        jobs.append((p1, p2, i))
    
    # Sort according to Johnson's rule
    jobs.sort(key=cmp_to_key(compare_jobs))
    
    # Calculate the final completion time
    X = 0  # Time when oven finishes current job
    Y = 0  # Time when icing station finishes current job
    
    for p1, p2, _ in jobs:
        X += p1
        Y = max(X, Y) + p2
    
    print(Y)

if __name__ == "__main__":
    main()