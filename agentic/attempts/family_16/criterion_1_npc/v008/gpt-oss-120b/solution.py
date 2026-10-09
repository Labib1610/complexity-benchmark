import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    J = next(it)
    M = next(it)

    jobs = []                     # jobs[j] = list of (machine, duration)
    total_ops = 0
    for _ in range(J):
        o = next(it)
        ops = []
        for __ in range(o):
            mac = next(it) - 1   # zero based
            dur = next(it)
            ops.append((mac, dur))
        jobs.append(ops)
        total_ops += o

    # total work per machine (constant, used for lower bound)
    total_machine_load = [0] * M
    for j in range(J):
        for mac, dur in jobs[j]:
            total_machine_load[mac] += dur
    machine_load_bound = max(total_machine_load)

    # remaining work per job (dynamic)
    rem_job = [sum(dur for _, dur in jobs[j]) for j in range(J)]

    # search state
    next_op = [0] * J                 # next operation index of each job
    job_done = [0] * J                # finishing time of last scheduled op
    machine_intervals = [[] for _ in range(M)]

    # ---------------------------------------------------------------
    # auxiliary functions
    def earliest_start(mac: int, ready: int, dur: int) -> int:
        """first time >= ready where [t, t+dur) does not intersect existing intervals"""
        t = ready
        for s, e in machine_intervals[mac]:
            if t + dur <= s:          # fits before this interval
                return t
            if t < e:
                t = e
        return t

    # ---------------------------------------------------------------
    # greedy schedule for initial upper bound
    def greedy_makespan() -> int:
        # copy mutable state
        g_next = next_op[:]
        g_done = job_done[:]
        g_rem = rem_job[:]
        g_inter = [lst[:] for lst in machine_intervals]

        ops_left = total_ops
        while ops_left:
            best_finish = None
            best_j = None
            best_mac = None
            best_dur = None
            best_start = None
            for j in range(J):
                if g_next[j] >= len(jobs[j]):
                    continue
                mac, dur = jobs[j][g_next[j]]
                start = earliest_start(mac, g_done[j], dur)
                finish = start + dur
                if best_finish is None or finish < best_finish:
                    best_finish = finish
                    best_j = j
                    best_mac = mac
                    best_dur = dur
                    best_start = start
            # schedule chosen operation
            # insert interval
            lst = g_inter[best_mac]
            pos = 0
            while pos < len(lst) and lst[pos][0] < best_start:
                pos += 1
            lst.insert(pos, (best_start, best_finish))

            g_done[best_j] = best_finish
            g_next[best_j] += 1
            g_rem[best_j] -= best_dur
            ops_left -= 1
        return max(g_done)

    best = greedy_makespan()

    # ---------------------------------------------------------------
    # depth‑first branch and bound
    def dfs(scheduled: int):
        nonlocal best
        if scheduled == total_ops:
            cur = max(job_done)
            if cur < best:
                best = cur
            return

        # lower bound
        job_lb = max(job_done[i] + rem_job[i] for i in range(J))
        lb = job_lb if job_lb > machine_load_bound else machine_load_bound
        if lb >= best:
            return

        # list ready jobs
        ready = [j for j in range(J) if next_op[j] < len(jobs[j])]

        # order by earliest finishing time (good heuristic)
        cand = []
        for j in ready:
            mac, dur = jobs[j][next_op[j]]
            start = earliest_start(mac, job_done[j], dur)
            finish = start + dur
            cand.append((finish, start, j, mac, dur))
        cand.sort()                     # try promising ones first

        for finish, start, j, mac, dur in cand:
            # place operation
            lst = machine_intervals[mac]
            pos = 0
            while pos < len(lst) and lst[pos][0] < start:
                pos += 1
            lst.insert(pos, (start, finish))

            old_done = job_done[j]
            job_done[j] = finish
            next_op[j] += 1
            rem_job[j] -= dur

            dfs(scheduled + 1)

            # undo
            rem_job[j] += dur
            next_op[j] -= 1
            job_done[j] = old_done
            lst.pop(pos)

    dfs(0)
    print(best)


if __name__ == "__main__":
    solve()