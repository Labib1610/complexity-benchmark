import sys

# Increase recursion depth just in case
sys.setrecursionlimit(10000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    j = int(next(it))
    m = int(next(it))
    T = int(next(it))
    
    jobs = []
    total_ops = 0
    for i in range(j):
        o = int(next(it))
        total_ops += o
        op_list = []
        for _ in range(o):
            mach = int(next(it)) - 1  # 0-indexed
            dur = int(next(it))
            op_list.append((mach, dur))
        jobs.append(op_list)
        
    # Precalculate tails for each operation
    # tail[i][k] = sum of durations of operations after k in job i
    tails = []
    job_durations = []
    for i in range(j):
        t_list = [0] * len(jobs[i])
        s = 0
        for k in range(len(jobs[i]) - 1, -1, -1):
            t_list[k] = s
            s += jobs[i][k][1]
        tails.append(t_list)
        job_durations.append(s)
        
    # Check if trivial bounds exceed T
    for dur in job_durations:
        if dur > T:
            print("NO")
            return
            
    mach_total = [0] * m
    for i in range(j):
        for mach, dur in jobs[i]:
            mach_total[mach] += dur
    for mt in mach_total:
        if mt > T:
            print("NO")
            return

    # Giffler-Thompson active schedule search with Branch and Bound
    cur_op = [0] * j
    job_avail = [0] * j
    mach_avail = [0] * m
    
    # Store start times
    start_times = [[0] * len(jobs[i]) for i in range(j)]
    
    # Lower bound helper
    # Remaining operations on each machine
    # To quickly check single machine lower bounds with release times and tails
    
    def search(completed):
        if completed == total_ops:
            return True
            
        # Quick lower bound checks
        for i in range(j):
            if cur_op[i] < len(jobs[i]):
                # Remaining time for job i
                rem = jobs[i][cur_op[i]][1] + tails[i][cur_op[i]]
                if job_avail[i] + rem > T:
                    return False

        # Machine bounds
        # Gather remaining ops for each machine
        # Check simple bounds
        # We can also do Jackson's preemptive rule if needed, but simple head + sum + tail is often fast
        for mach in range(m):
            ops_on_mach = []
            for i in range(j):
                for k in range(cur_op[i], len(jobs[i])):
                    if jobs[i][k][0] == mach:
                        # Earliest time this op can reach this machine:
                        # approx: job_avail[i] + sum of intermediate durations
                        # intermediate = tails[i][cur_op[i]] - tails[i][k] - jobs[i][k][1]
                        inter = tails[i][cur_op[i]] - tails[i][k] - jobs[i][k][1]
                        r = job_avail[i] + inter
                        d = jobs[i][k][1]
                        q = tails[i][k]
                        ops_on_mach.append((r, d, q))
            if not ops_on_mach:
                continue
            
            # Simple 1-machine lower bound
            sum_d = sum(x[1] for x in ops_on_mach)
            min_r = min(x[0] for x in ops_on_mach)
            min_q = min(x[2] for x in ops_on_mach)
            
            start_m = max(mach_avail[mach], min_r)
            if start_m + sum_d + min_q > T:
                return False
                
            for r, d, q in ops_on_mach:
                if max(mach_avail[mach], r) + d + q > T:
                    return False

        # Find candidate operations (one per active job)
        best_ec = float('inf')
        best_mach = -1
        
        candidates = []
        for i in range(j):
            k = cur_op[i]
            if k < len(jobs[i]):
                mach, dur = jobs[i][k]
                es = max(job_avail[i], mach_avail[mach])
                ec = es + dur
                candidates.append((i, k, mach, dur, es, ec))
                if ec < best_ec:
                    best_ec = ec
                    best_mach = mach
                    
        if best_mach == -1:
            return True
            
        # Conflict set: operations on best_mach that can start before best_ec
        # Sort conflict set by some heuristic (e.g. earliest release time, or minimum tail)
        conflict_ops = []
        for cand in candidates:
            i, k, mach, dur, es, ec = cand
            if mach == best_mach and es < best_ec:
                # Heuristic sort key: smaller tail or smaller es + dur + tail
                conflict_ops.append((es, -tails[i][k], cand))
                
        # Sort by earliest start, or most critical (largest tail)
        conflict_ops.sort(key=lambda x: (x[0], x[1]))
        
        for _, _, cand in conflict_ops:
            i, k, mach, dur, es, ec = cand
            if es + dur + tails[i][k] > T:
                continue
                
            old_job_avail = job_avail[i]
            old_mach_avail = mach_avail[mach]
            
            start_times[i][k] = es
            job_avail[i] = es + dur
            mach_avail[mach] = es + dur
            cur_op[i] += 1
            
            if search(completed + 1):
                return True
                
            cur_op[i] -= 1
            job_avail[i] = old_job_avail
            mach_avail[mach] = old_mach_avail
            
        return False

    if search(0):
        print("YES")
        for i in range(j):
            print(*(start_times[i]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()