import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    N_alpha = int(next(it))
    N_omega = int(next(it))
    m = int(next(it))
    
    jobs = []
    alpha_jobs = defaultdict(list)
    omega_jobs = defaultdict(list)
    
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        jobs.append((u, v))
        alpha_jobs[u].append(i)
        omega_jobs[v].append(i)
    
    # Compute K = max degree
    K = 0
    for lst in alpha_jobs.values():
        if len(lst) > K:
            K = len(lst)
    for lst in omega_jobs.values():
        if len(lst) > K:
            K = len(lst)
    
    # Bipartite edge coloring using greedy matching
    # We process jobs in order, assigning the smallest available phase
    # that doesn't conflict with already assigned jobs sharing resources.
    
    # For each resource, track which phases are currently used
    alpha_used = defaultdict(set)  # alpha_id -> set of used phases
    omega_used = defaultdict(set)  # omega_id -> set of used phases
    
    result = [0] * m
    
    for i, (u, v) in enumerate(jobs):
        # Find smallest phase in 1..K not used by u or v
        # Since K >= max(deg(u), deg(v)), such a phase always exists
        used_u = alpha_used[u]
        used_v = omega_used[v]
        
        # Greedy: try phases 1 to K
        for phase in range(1, K + 1):
            if phase not in used_u and phase not in used_v:
                result[i] = phase
                used_u.add(phase)
                used_v.add(phase)
                break
    
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    solve()