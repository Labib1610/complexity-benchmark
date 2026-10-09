import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    m = int(next(it))
    T = int(next(it))

    jobs = []
    for _ in range(j):
        o = int(next(it))
        ops = []
        for __ in range(o):
            machine = int(next(it)) - 1
            dur = int(next(it))
            ops.append((machine, dur))
        jobs.append(ops)

    # earliest start times respecting precedence and machine availability
    machine_free = [0] * m
    job_next_ready = [0] * j
    start_times = [[] for _ in range(j)]

    for job_id, ops in enumerate(jobs):
        cur = 0
        for machine, dur in ops:
            st = max(machine_free[machine], cur)
            start_times[job_id].append(st)
            finish = st + dur
            machine_free[machine] = finish
            cur = finish
        job_next_ready[job_id] = cur

    makespan = max(machine_free) if machine_free else 0
    if makespan > T:
        print("NO")
    else:
        print("YES")
        out_lines = []
        for times in start_times:
            out_lines.append(' '.join(map(str, times)))
        sys.stdout.write('\n'.join(out_lines))

if __name__ == "__main__":
    solve()