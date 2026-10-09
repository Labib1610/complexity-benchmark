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
    total_dur = 0
    for _ in range(J):
        o = int(next(it))
        ops = []
        for __ in range(o):
            w = int(next(it)) - 1
            d = int(next(it))
            ops.append((w, d))
            total_dur += d
        jobs.append(ops)

    # precompute remaining durations per job and per machine for fast lower bound
    rem_job = [ [0]*(len(jobs[i])+1) for i in range(J) ]  # suffix sums
    for i in range(J):
        s = 0
        for k in range(len(jobs[i])-1, -1, -1):
            s += jobs[i][k][1]
            rem_job[i][k] = s
    # for machines
    max_ops = max(len(j) for j in jobs)
    # we will compute remaining per machine on the fly

    best = total_dur * 2  # upper bound

    # initial states
    next_idx = [0]*J
    job_ready = [0]*J
    machine_free = [0]*M

    # list of operations per machine for quick remaining sum
    ops_by_machine = [[] for _ in range(M)]
    for i, job in enumerate(jobs):
        for pos, (w, d) in enumerate(job):
            ops_by_machine[w].append((i, pos, d))
    # precompute suffix sums per machine sorted by position? easier compute on the fly

    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dfs(state_next, state_job_ready, state_machine_free):
        nonlocal best
        # convert to mutable lists
        next_idx = list(state_next)
        job_ready = list(state_job_ready)
        machine_free = list(state_machine_free)

        # check completion
        if all(next_idx[i] == len(jobs[i]) for i in range(J)):
            cur = max(job_ready)  # all finished
            if cur < best:
                best = cur
            return

        # lower bound
        lb = 0
        for i in range(J):
            if next_idx[i] < len(jobs[i]):
                lb = max(lb, job_ready[i] + rem_job[i][next_idx[i]])
        for w in range(M):
            # sum remaining durations on this machine
            rem = 0
            for i in range(J):
                idx = next_idx[i]
                while idx < len(jobs[i]) and jobs[i][idx][0] != w:
                    idx += 1
                if idx < len(jobs[i]) and jobs[i][idx][0] == w:
                    # this and all later ops on this machine for this job
                    # we need to sum all future ops of this job that are on w
                    for p in range(idx, len(jobs[i])):
                        if jobs[i][p][0] == w:
                            rem += jobs[i][p][1]
            lb = max(lb, machine_free[w] + rem)
        cur_makespan = max(max(job_ready), max(machine_free))
        if max(cur_makespan, lb) >= best:
            return

        # collect ready operations
        ready = []
        for i in range(J):
            idx = next_idx[i]
            if idx < len(jobs[i]):
                w, d = jobs[i][idx]
                ready.append((i, w, d))
        # simple heuristic: sort by earliest possible start
        ready.sort(key=lambda x: max(job_ready[x[0]], machine_free[x[1]]))

        for i, w, d in ready:
            start = max(job_ready[i], machine_free[w])
            finish = start + d
            # update state
            old_job = job_ready[i]
            old_mach = machine_free[w]
            old_idx = next_idx[i]

            job_ready[i] = finish
            machine_free[w] = finish
            next_idx[i] += 1

            dfs(tuple(next_idx), tuple(job_ready), tuple(machine_free))

            # revert
            job_ready[i] = old_job
            machine_free[w] = old_mach
            next_idx[i] = old_idx

    dfs(tuple(next_idx), tuple(job_ready), tuple(machine_free))
    print(best)

if __name__ == "__main__":
    solve()