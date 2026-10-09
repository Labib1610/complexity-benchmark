#!/usr/bin/env python3
"""Worst-case (witness-graded) tier for family 16 — JOB-SHOP scheduling.

The seed asks for the minimum makespan (a number), which cannot be cheaply verified (certifying an
optimum is NP-hard -> the gradeable ceiling). So, exactly like the colouring worst-case tier, this is
a FEASIBILITY + WITNESS reframe:
  - plant an instance together with a compact feasible schedule of makespan T (so YES by construction),
  - ask the solver for ANY schedule with makespan <= T,
  - grade by VERIFYING the schedule (job order + machine non-overlap + makespan <= T) in O(ops).
Near the packing threshold (many ops, few machines, T tight) finding such a schedule is hard, but the
planted schedule guarantees one exists, so instances stay gradeable at any size.

I/O:
  input : line 1 = "j m T"; next j lines = "o  m1 d1  m2 d2 ... mo do" (1-indexed machines, durations)
  output: "YES" then j lines, each with o integers = start times of that job's operations in order;
          or a single line "NO".
"""
import argparse, random, sys


def plant(n_jobs, m, ops_per_job, seed):
    """Build jobs with random (machine,duration) ops, then compute a COMPACT feasible schedule by
    active list-scheduling (at each step start the ready op that can begin earliest). The resulting
    makespan T is the planted bound; the schedule proves feasibility <= T."""
    rng = random.Random(seed * 2_000_003 + m)
    jobs = [[(rng.randint(1, m), rng.randint(1, 9)) for _ in range(ops_per_job)]
            for _ in range(n_jobs)]
    machine_free = [0] * (m + 1)
    job_end = [0] * n_jobs
    next_op = [0] * n_jobs
    starts = [[0] * ops_per_job for _ in range(n_jobs)]
    total = n_jobs * ops_per_job
    done = 0
    while done < total:
        # ready ops = next unscheduled op of each job; pick earliest possible start (tie: shortest)
        best = None
        for j in range(n_jobs):
            k = next_op[j]
            if k >= ops_per_job:
                continue
            mach, dur = jobs[j][k]
            est = max(job_end[j], machine_free[mach])
            key = (est, dur, j)
            if best is None or key < best[0]:
                best = (key, j, k, mach, dur, est)
        _, j, k, mach, dur, est = best
        starts[j][k] = est
        job_end[j] = est + dur
        machine_free[mach] = est + dur
        next_op[j] += 1
        done += 1
    T = max(job_end)
    lines = [f"{n_jobs} {m} {T}"]
    for job in jobs:
        lines.append(f"{len(job)} " + " ".join(f"{mac} {d}" for mac, d in job))
    return "\n".join(lines) + "\n", starts


def _parse(text):
    toks = text.split(); idx = 0
    j = int(toks[idx]); m = int(toks[idx+1]); T = int(toks[idx+2]); idx += 3
    jobs = []
    for _ in range(j):
        o = int(toks[idx]); idx += 1
        ops = [(int(toks[idx+2*i]), int(toks[idx+2*i+1])) for i in range(o)]; idx += 2*o
        jobs.append(ops)
    return j, m, T, jobs


def grade(input_text, output_text):
    """Witness-only: PASS iff the output is a schedule respecting job order + machine exclusivity and
    with makespan <= T."""
    j, m, T, jobs = _parse(input_text)
    toks = output_text.split()
    if not toks:
        return False, "empty output"
    if toks[0].upper() == "NO":
        return False, "reported NO but a schedule was planted"
    nums = toks[1:] if toks[0].upper() == "YES" else toks
    try:
        vals = [int(x) for x in nums]
    except ValueError:
        return False, "non-integer start time"
    total = sum(len(job) for job in jobs)
    if len(vals) != total:
        return False, f"expected {total} start times, got {len(vals)}"
    # slice back into per-job start lists (in the job/op order)
    starts = []; p = 0
    for job in jobs:
        starts.append(vals[p:p+len(job)]); p += len(job)
    intervals = {}  # machine -> list of (start,end)
    makespan = 0
    for ji, job in enumerate(jobs):
        prev_end = 0
        for k, (mach, dur) in enumerate(job):
            s = starts[ji][k]
            if s < 0:
                return False, f"job {ji+1} op {k+1}: negative start"
            if s < prev_end:
                return False, f"job {ji+1} op {k+1}: starts {s} before previous op ends {prev_end}"
            e = s + dur
            intervals.setdefault(mach, []).append((s, e))
            prev_end = e
            makespan = max(makespan, e)
    if makespan > T:
        return False, f"makespan {makespan} exceeds T={T}"
    for mach, iv in intervals.items():
        iv.sort()
        for a, b in zip(iv, iv[1:]):
            if a[1] > b[0]:
                return False, f"machine {mach}: overlap {a} and {b}"
    return True, f"valid schedule, makespan {makespan} <= {T}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gen", action="store_true"); ap.add_argument("--grade", metavar="F")
    ap.add_argument("--jobs", type=int, default=20); ap.add_argument("--m", type=int, default=5)
    ap.add_argument("--ops", type=int, default=8); ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    if a.gen:
        txt, _ = plant(a.jobs, a.m, a.ops, a.seed); sys.stdout.write(txt)
    elif a.grade:
        ok, msg = grade(open(a.grade).read(), sys.stdin.read())
        print("PASS" if ok else "FAIL", "--", msg); sys.exit(0 if ok else 1)
    else:
        ap.error("use --gen or --grade")


if __name__ == "__main__":
    main()
