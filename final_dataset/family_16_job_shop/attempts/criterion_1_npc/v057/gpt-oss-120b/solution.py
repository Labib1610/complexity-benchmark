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
    for _ in range(J):
        o = int(next(it))
        steps = []
        for __ in range(o):
            ins = int(next(it)) - 1
            dur = int(next(it))
            steps.append((ins, dur))
        jobs.append(steps)

    # precompute remaining total duration per job from each position
    rem_job = [ [0]*(len(job)+1) for job in jobs ]
    for idx, job in enumerate(jobs):
        total = 0
        for pos in range(len(job)-1, -1, -1):
            total += job[pos][1]
            rem_job[idx][pos] = total
        rem_job[idx][len(job)] = 0

    # remaining total per machine from each position (we need per job pos)
    # We'll compute on the fly: for each machine, sum of durations of steps not yet scheduled that require it.
    # To speed, precompute for each job and each position the remaining per machine.
    rem_machine = [ [ [0]*M for _ in range(len(job)+1) ] for job in jobs ]
    for idx, job in enumerate(jobs):
        cur = [0]*M
        for pos in range(len(job)-1, -1, -1):
            ins, dur = job[pos]
            cur = cur.copy()
            cur[ins] += dur
            rem_machine[idx][pos] = cur
        rem_machine[idx][len(job)] = [0]*M

    best = [float('inf')]

    # initial states
    pos = [0]*J
    job_ready = [0]*J
    machine_free = [0]*M

    def lower_bound():
        # max of current completions and optimistic remaining
        lb = 0
        # current makespan so far
        cur_mk = max(machine_free) if machine_free else 0
        lb = max(lb, cur_mk)
        # for each job, earliest finish if it runs without further machine conflicts
        for j in range(J):
            if pos[j] < len(jobs[j]):
                lb = max(lb, job_ready[j] + rem_job[j][pos[j]])
        # for each machine, consider remaining work on that machine
        for m in range(M):
            rem = 0
            for j in range(J):
                rem += rem_machine[j][pos[j]][m]
            lb = max(lb, machine_free[m] + rem)
        return lb

    def dfs():
        # prune
        lb = lower_bound()
        if lb >= best[0]:
            return
        # check if all done
        if all(pos[j] == len(jobs[j]) for j in range(J)):
            makespan = max(machine_free) if machine_free else 0
            if makespan < best[0]:
                best[0] = makespan
            return

        # collect enabled tasks
        enabled = []
        for j in range(J):
            if pos[j] < len(jobs[j]):
                ins, dur = jobs[j][pos[j]]
                earliest = max(job_ready[j], machine_free[ins])
                enabled.append((earliest, j, ins, dur))

        # sort to try earlier start first (branching heuristic)
        enabled.sort()
        for earliest, j, ins, dur in enabled:
            # schedule this task
            start = earliest
            finish = start + dur

            # save state
            old_job_ready = job_ready[j]
            old_machine_free = machine_free[ins]
            pos[j] += 1
            job_ready[j] = finish
            machine_free[ins] = finish

            dfs()

            # restore
            pos[j] -= 1
            job_ready[j] = old_job_ready
            machine_free[ins] = old_machine_free

    dfs()
    print(best[0])

if __name__ == "__main__":
    solve()