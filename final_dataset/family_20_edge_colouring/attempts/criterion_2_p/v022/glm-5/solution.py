import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        N_alpha = int(next(iterator))
        N_omega = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return
    
    jobs = []
    # Track degree of each resource (number of jobs using it)
    deg_alpha = [0] * (N_alpha + 1)
    deg_omega = [0] * (N_omega + 1)
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        jobs.append((u, v))
        deg_alpha[u] += 1
        deg_omega[v] += 1
    
    # K is the maximum degree of any resource
    K = max(max(deg_alpha), max(deg_omega)) if m > 0 else 0
    
    # Group jobs by alpha resource
    alpha_jobs = defaultdict(list)
    for idx, (u, v) in enumerate(jobs):
        alpha_jobs[u].append((idx, v))
    
    result = [0] * m
    
    # For each alpha resource, assign phases to its jobs
    # We need to avoid: same phase for jobs sharing alpha (handled by processing each alpha separately)
    # and same phase for jobs sharing omega (handled by greedy assignment)
    
    for u in range(1, N_alpha + 1):
        job_list = alpha_jobs.get(u, [])
        if not job_list:
            continue
        
        # Sort by omega resource to make greedy assignment more efficient
        job_list.sort(key=lambda x: x[1])
        
        # Track which phases are used by each omega resource
        omega_used = defaultdict(set)
        
        for job_idx, v in job_list:
            # Find the smallest available phase (1 to K) not used by omega v
            used = omega_used[v]
            phase = 1
            while phase in used:
                phase += 1
            result[job_idx] = phase
            omega_used[v].add(phase)
    
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    solve()