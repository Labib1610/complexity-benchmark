import sys
from functools import cmp_to_key

def compare_jobs(job1, job2):
    # job = (p1, p2, index)
    p1_1, p2_1 = job1[0], job1[1]
    p1_2, p2_2 = job2[0], job2[1]
    
    # If one job's p1 <= another's p2 and vice versa, we need a tie-breaking rule
    # Johnson's rule: compare p1_i + p2_j with p1_j + p2_i
    if p1_1 + p2_2 < p1_2 + p2_1:
        return -1
    elif p1_1 + p2_2 > p1_2 + p2_1:
        return 1
    else:
        return 0

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    jobs = []
    index = 1
    for i in range(j):
        p1 = int(data[index])
        p2 = int(data[index+1])
        jobs.append((p1, p2))
        index += 2
    
    # Apply Johnson's rule for optimal sequencing
    # Sort jobs by comparing (p1_i, p2_i) and (p1_j, p2_j)
    # A job i should come before job j if min(p1_i, p2_j) < min(p1_j, p2_i)
    # Actually, for two-stage flow shop, Johnson's algorithm is:
    # - Jobs with p1 <= p2 go first, sorted by p1 ascending
    # - Jobs with p1 > p2 go later, sorted by p2 descending
    
    # But there's a more precise version:
    # For jobs i and j, i should precede j if min(p1_i, p2_j) <= min(p1_j, p2_i)
    # However, a simpler and commonly used heuristic that works well is:
    # Sort by p1 ascending if p1 <= p2, otherwise sort by p2 descending
    
    def job_compare(a, b):
        p1_a, p2_a = a
        p1_b, p2_b = b
        
        # Johnson's algorithm proper:
        if p1_a <= p2_a:
            if p1_b > p2_b:
                return -1
            else:
                if p1_a < p1_b:
                    return -1
                elif p1_a > p1_b:
                    return 1
                else:
                    return 0
        else:
            if p1_b <= p2_b:
                return 1
            else:
                if p2_a > p2_b:
                    return -1
                elif p2_a < p2_b:
                    return 1
                else:
                    return 0
    
    # Even simpler approach for flow shop scheduling (Johnson's Rule):
    # Create two lists:
    # L1 = jobs where p1 <= p2, sorted by p1 ascending
    # L2 = jobs where p1 > p2, sorted by p2 descending
    # Final sequence = L1 + L2
    
    L1 = [(p1, p2) for p1, p2 in jobs if p1 <= p2]
    L2 = [(p1, p2) for p1, p2 in jobs if p1 > p2]
    
    L1.sort(key=lambda x: x[0])  # Sort by p1 ascending
    L2.sort(key=lambda x: x[1], reverse=True)  # Sort by p2 descending
    
    ordered_jobs = L1 + L2
    
    # Simulate the process
    time_bake = 0
    time_decorate = 0
    
    for p1, p2 in ordered_jobs:
        time_bake += p1
        time_decorate = max(time_decorate, time_bake) + p2
    
    print(time_decorate)

if __name__ == "__main__":
    main()