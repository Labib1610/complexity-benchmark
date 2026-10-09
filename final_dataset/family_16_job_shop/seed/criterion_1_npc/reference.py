import sys


def main():
    sys.setrecursionlimit(1000000)
    data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(data[idx]); m = int(data[idx + 1]); idx += 2

    jobs = []  # jobs[i] = list of (machine0, duration)
    for _ in range(j):
        o = int(data[idx]); idx += 1
        ops = []
        for _ in range(o):
            mc = int(data[idx]) - 1; du = int(data[idx + 1]); idx += 2
            ops.append((mc, du))
        jobs.append(ops)

    best = [float("inf")]

    def lower_bound(nextop, mfree, jfree):
        mrem = [0] * m
        jrem = [0] * j
        for i in range(j):
            for kk in range(nextop[i], len(jobs[i])):
                mc, du = jobs[i][kk]
                mrem[mc] += du
                jrem[i] += du
        lb = 0
        for c in range(m):
            v = mfree[c] + mrem[c]
            if v > lb:
                lb = v
        for i in range(j):
            v = jfree[i] + jrem[i]
            if v > lb:
                lb = v
        return lb

    # Giffler-Thompson branch and bound over active schedules.
    def rec(nextop, mfree, jfree, cur_ms):
        if cur_ms >= best[0]:
            return
        sched = []  # (job, machine, dur, est, ect)
        for i in range(j):
            p = nextop[i]
            if p < len(jobs[i]):
                mc, du = jobs[i][p]
                est = mfree[mc] if mfree[mc] > jfree[i] else jfree[i]
                sched.append((i, mc, du, est, est + du))
        if not sched:
            if cur_ms < best[0]:
                best[0] = cur_ms
            return
        if lower_bound(nextop, mfree, jfree) >= best[0]:
            return
        cstar = min(s[4] for s in sched)
        mstar = next(s[1] for s in sched if s[4] == cstar)
        conflict = [s for s in sched if s[1] == mstar and s[3] < cstar]
        for (i, mc, du, est, ect) in conflict:
            nm = mfree[:]
            nj = jfree[:]
            nn = nextop[:]
            nm[mc] = ect
            nj[i] = ect
            nn[i] += 1
            rec(nn, nm, nj, cur_ms if cur_ms > ect else ect)

    rec([0] * j, [0] * m, [0] * j, 0)
    print(best[0])


main()
