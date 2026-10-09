import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    j = next(it)
    m = next(it)
    jobs = []
    for _ in range(j):
        o = next(it)
        steps = []
        for __ in range(o):
            r = next(it) - 1          # zero based
            d = next(it)
            steps.append((r, d))
        jobs.append(steps)

    # precompute suffix sums of durations for each job
    suffix = []
    for steps in jobs:
        s = [0] * (len(steps) + 1)
        for i in range(len(steps) - 1, -1, -1):
            s[i] = s[i + 1] + steps[i][1]
        suffix.append(s)

    total_ops = sum(len(st) for st in jobs)
    best = [float('inf')]

    # initial states
    pos = [0] * j                     # next operation index for each job
    job_ready = [0] * j               # earliest time job i can start its next op
    machine_ready = [0] * m           # earliest time each machine is free

    # lower bound function
    def lower_bound(cur_max):
        lb = cur_max
        # job based
        for i in range(j):
            if pos[i] < len(jobs[i]):
                lb = max(lb, job_ready[i] + suffix[i][pos[i]])
        # machine based
        for mach in range(m):
            rem = 0
            for i in range(j):
                p = pos[i]
                while p < len(jobs[i]) and jobs[i][p][0] != mach:
                    p += 1
                # sum durations of remaining ops on this machine for this job
                while p < len(jobs[i]) and jobs[i][p][0] == mach:
                    rem += jobs[i][p][1]
                    p += 1
            lb = max(lb, machine_ready[mach] + rem)
        return lb

    # recursive search
    def dfs(done, cur_max):
        if done == total_ops:
            if cur_max < best[0]:
                best[0] = cur_max
            return
        # prune by lower bound
        if lower_bound(cur_max) >= best[0]:
            return

        # generate list of ready jobs
        ready_jobs = [i for i in range(j) if pos[i] < len(jobs[i])]
        # simple heuristic: try jobs with earliest possible start first
        ready_jobs.sort(key=lambda i: max(job_ready[i], machine_ready[jobs[i][pos[i]][0]]))

        for i in ready_jobs:
            r, d = jobs[i][pos[i]]
            start = max(job_ready[i], machine_ready[r])
            finish = start + d

            # apply
            old_job_ready = job_ready[i]
            old_machine_ready = machine_ready[r]
            old_pos = pos[i]

            job_ready[i] = finish
            machine_ready[r] = finish
            pos[i] += 1

            dfs(done + 1, max(cur_max, finish))

            # revert
            job_ready[i] = old_job_ready
            machine_ready[r] = old_machine_ready
            pos[i] = old_pos

    dfs(0, 0)
    print(best[0])

if __name__ == "__main__":
    solve()