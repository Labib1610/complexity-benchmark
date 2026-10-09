import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    p1 = [0] * j
    p2 = [0] * j
    idx = 2
    for i in range(j):
        p1[i] = int(data[idx]); p2[i] = int(data[idx+1])
        idx += 2

    # Check JOB i: p1[i] + p2[i] > T
    job_ans = -1
    for i in range(j):
        if p1[i] + p2[i] > T:
            job_ans = i + 1
            break

    # Check LOAD 1: sum(p1) > T
    load1_ans = -1
    if sum(p1) > T:
        load1_ans = 1

    # Check LOAD 2: sum(p2) > T
    load2_ans = -1
    if sum(p2) > T:
        load2_ans = 2

    # Exactly one is guaranteed to hold
    if job_ans != -1:
        print(f"JOB {job_ans}")
    elif load1_ans != -1:
        print(f"LOAD {load1_ans}")
    else:
        print(f"LOAD {load2_ans}")

solve()