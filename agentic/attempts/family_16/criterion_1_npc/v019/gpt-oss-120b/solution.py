import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    J = int(next(it))
    M = int(next(it))
    jobs = []
    total_ops = 0
    for _ in range(J):
        o = int(next(it))
        ops = []
        for __ in range(o):
            app = int(next(it)) - 1
            dur = int(next(it))
            ops.append((app, dur))
        jobs.append(ops)
        total_ops += o

    # precompute remaining sums per job and per machine
    rem_job = [ [0]*(len(jobs[i])+1) for i in range(J) ]
    for i in range(J):
        s = 0
        for p in range(len(jobs[i])-1, -1, -1):
            s += jobs[i][p][1]
            rem_job[i][p] = s
        rem_job[i][len(jobs[i])] = 0

    rem_machine = [0]*M
    for i in range(J):
        for app, dur in jobs[i]:
            rem_machine[app] += dur

    best = [float('inf')]

    job_pos = [0]*J          # next operation index
    job_ready = [0]*J        # time when job can start next op
    machine_free = [0]*M

    def dfs(done_ops: int):
        if done_ops == total_ops:
            cur = max(job_ready)
            if cur < best[0]:
                best[0] = cur
            return

        # lower bound
        cur_mk = max(job_ready)
        lb = cur_mk
        for i in range(J):
            if job_pos[i] < len(jobs[i]):
                lb = max(lb, job_ready[i] + rem_job[i][job_pos[i]])
        for k in range(M):
            if rem_machine[k]:
                lb = max(lb, machine_free[k] + rem_machine[k])
        if lb >= best[0]:
            return

        # generate candidates: jobs not finished
        candidates = []
        for i in range(J):
            if job_pos[i] < len(jobs[i]):
                app, dur = jobs[i][job_pos[i]]
                start = max(job_ready[i], machine_free[app])
                candidates.append((start, i, app, dur))
        # sort by earliest start to improve pruning
        candidates.sort()
        for start, i, app, dur in candidates:
            # schedule this operation
            prev_job_ready = job_ready[i]
            prev_machine_free = machine_free[app]
            prev_rem_machine = rem_machine[app]

            job_ready[i] = start + dur
            machine_free[app] = start + dur
            job_pos[i] += 1
            rem_machine[app] -= dur

            dfs(done_ops + 1)

            # backtrack
            job_ready[i] = prev_job_ready
            machine_free[app] = prev_machine_free
            job_pos[i] -= 1
            rem_machine[app] = prev_rem_machine

    dfs(0)
    print(best[0])

if __name__ == "__main__":
    solve()