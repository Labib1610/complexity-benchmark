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
            mach = int(next(it)) - 1
            dur = int(next(it))
            ops.append((mach, dur))
        jobs.append(ops)
        total_ops += o

    # initial upper bound: schedule jobs one after another in given order
    machine_ready = [0] * M
    job_ready = [0] * J
    for jid in range(J):
        for mach, dur in jobs[jid]:
            start = max(job_ready[jid], machine_ready[mach])
            finish = start + dur
            job_ready[jid] = finish
            machine_ready[mach] = finish
    best = max(job_ready)

    # precompute remaining total duration per job and per machine for lower bound
    rem_job_total = [[0] * (len(jobs[i]) + 1) for i in range(J)]
    for i in range(J):
        s = 0
        for k in range(len(jobs[i]) - 1, -1, -1):
            s += jobs[i][k][1]
            rem_job_total[i][k] = s
        rem_job_total[i][len(jobs[i])] = 0

    rem_machine_total = [[0] * (len(jobs[i]) + 1) for i in range(J)]
    # not per machine, we will compute on the fly

    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dfs(state):
        # state: tuple of job positions, machine ready times, job ready times
        # but machine and job ready times can be large; we compress by storing differences?
        # Instead, we avoid memoization due to large time values.
        pass

    # We'll implement plain DFS with pruning
    job_pos = [0] * J
    job_ready = [0] * J
    machine_ready = [0] * M
    scheduled = 0
    nonlocal_best = {'val': best}

    # Precompute for each job the suffix sum of durations per machine
    suffix_machine = []
    for ops in jobs:
        sm = {}
        cur = {}
        for idx in range(len(ops) - 1, -1, -1):
            mach, dur = ops[idx]
            cur = cur.copy()
            cur[mach] = cur.get(mach, 0) + dur
            sm[idx] = cur
        sm[len(ops)] = {}
        suffix_machine.append(sm)

    def lower_bound():
        # max of current max finish and optimistic finishes
        lb = 0
        # job based
        for i in range(J):
            pos = job_pos[i]
            if pos < len(jobs[i]):
                lb = max(lb, job_ready[i] + rem_job_total[i][pos])
        # machine based
        for m in range(M):
            # sum of remaining durations on this machine
            rem = 0
            for i in range(J):
                pos = job_pos[i]
                if pos < len(jobs[i]):
                    rem += suffix_machine[i][pos].get(m, 0)
            lb = max(lb, machine_ready[m] + rem)
        return lb

    def dfs():
        if scheduled == total_ops:
            cur = max(job_ready)
            if cur < nonlocal_best['val']:
                nonlocal_best['val'] = cur
            return
        # prune
        if lower_bound() >= nonlocal_best['val']:
            return
        # collect ready operations
        ready = []
        for i in range(J):
            p = job_pos[i]
            if p < len(jobs[i]):
                mach, dur = jobs[i][p]
                est = max(job_ready[i], machine_ready[mach])
                ready.append((est, i, mach, dur))
        # sort to try earlier start first
        ready.sort()
        for est, i, mach, dur in ready:
            # schedule this operation
            old_job_ready = job_ready[i]
            old_mach_ready = machine_ready[mach]
            start = est
            finish = start + dur
            job_ready[i] = finish
            machine_ready[mach] = finish
            job_pos[i] += 1
            nonlocal scheduled
            scheduled += 1

            dfs()

            # backtrack
            scheduled -= 1
            job_pos[i] -= 1
            job_ready[i] = old_job_ready
            machine_ready[mach] = old_mach_ready

    dfs()
    print(nonlocal_best['val'])

if __name__ == "__main__":
    solve()