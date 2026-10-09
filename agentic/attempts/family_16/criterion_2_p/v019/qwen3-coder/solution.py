import sys
from functools import cmp_to_key

def compare_jobs(job1, job2):
    # job = (p1, p2, index)
    p1_1, p2_1, _ = job1
    p1_2, p2_2, _ = job2
    
    # If p1_1 < p2_1, we want job1 to go first
    # If p1_2 < p2_2, we want job2 to go first
    
    # This is the Johnson's rule comparison
    if p1_1 < p2_1 and p1_2 >= p2_2:
        return -1
    elif p1_1 >= p2_1 and p1_2 < p2_2:
        return 1
    else:
        # For other cases, we can use the sum as tie-breaker or just return 0
        # But to make it deterministic, let's compare p1_1 + p2_1 with p1_2 + p2_2
        if p1_1 + p2_1 < p1_2 + p2_2:
            return -1
        elif p1_1 + p2_1 > p1_2 + p2_2:
            return 1
        else:
            return 0

def main():
    j = int(sys.stdin.readline())
    jobs = []
    
    for i in range(j):
        p1, p2 = map(int, sys.stdin.readline().split())
        jobs.append((p1, p2, i))
    
    # Sort using Johnson's rule
    def compare(a, b):
        p1_a, p2_a, _ = a
        p1_b, p2_b, _ = b
        
        # Johnson's algorithm sorting rule
        if p1_a < p2_a and p1_b >= p2_b:
            return -1
        if p1_a >= p2_a and p1_b < p2_b:
            return 1
            
        # If both are in the same category, sort by min(p1, p2) 
        min_a = min(p1_a, p2_a)
        min_b = min(p1_b, p2_b)
        
        if min_a != min_b:
            if min_a < min_b:
                return -1
            else:
                return 1
        else:
            # If still tied, sort by p1
            if p1_a < p1_b:
                return -1
            elif p1_a > p1_b:
                return 1
            else:
                return 0
    
    jobs.sort(key=cmp_to_key(compare))
    
    # Calculate the finish time
    calligrapher_time = 0
    bookbinder_finish_time = 0
    
    for p1, p2, _ in jobs:
        calligrapher_time += p1
        bookbinder_finish_time = max(bookbinder_finish_time, calligrapher_time) + p2
    
    print(bookbinder_finish_time)

if __name__ == "__main__":
    main()