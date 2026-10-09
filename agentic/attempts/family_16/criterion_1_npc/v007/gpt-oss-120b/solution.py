import sys, heapq

def solve() -> None:
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    it = iter(data)
    J = next(it)
    M = next(it)
    jobs = []
    for _ in range(J):
        o = next(it)
        ops = []
        for __ in range(o):
            machine = next(it) - 1
            dur = next(it)
            ops.append((machine, dur))
        jobs.append(ops)

    # initial state
    # progress per job: how many ops done
    prog = tuple(0 for _ in range(J))
    # next ready time per job (when previous op finished)
    job_ready = tuple(0 for _ in range(J))
    # machine free times
    mach_free = tuple(0 for _ in range(M))
    # current makespan (max of all times)
    start_state = (0, prog, job_ready, mach_free)  # priority, ...

    heap = [start_state]
    seen = {}
    while heap:
        makespan, prog, job_ready, mach_free = heapq.heappop(heap)
        if prog == tuple(len(jobs[i]) for i in range(J)):
            print(makespan)
            return
        key = (prog, mach_free)
        if key in seen and seen[key] <= makespan:
            continue
        seen[key] = makespan

        # generate possible next operations
        for i in range(J):
            pi = prog[i]
            if pi >= len(jobs[i]):
                continue
            machine, dur = jobs[i][pi]
            start = max(job_ready[i], mach_free[machine])
            finish = start + dur
            # new state
            new_prog = list(prog)
            new_prog[i] += 1
            new_prog = tuple(new_prog)

            new_job_ready = list(job_ready)
            new_job_ready[i] = finish
            new_job_ready = tuple(new_job_ready)

            new_mach_free = list(mach_free)
            new_mach_free[machine] = finish
            new_mach_free = tuple(new_mach_free)

            new_makespan = max(makespan, finish)
            heapq.heappush(heap, (new_makespan, new_prog, new_job_ready, new_mach_free))

if __name__ == "__main__":
    solve()