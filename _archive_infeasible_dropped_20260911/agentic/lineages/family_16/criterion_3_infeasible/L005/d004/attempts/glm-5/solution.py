import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    idx = 2
    total1 = 0
    total2 = 0
    job_cert = -1
    for i in range(1, j + 1):
        p1 = int(data[idx])
        p2 = int(data[idx + 1])
        idx += 2
        total1 += p1
        total2 += p2
        if p1 + p2 > T and job_cert == -1:
            job_cert = i
    if job_cert != -1:
        print(f"JOB {job_cert}")
        return
    if total1 > T:
        print("LOAD 1")
        return
    if total2 > T:
        print("LOAD 2")
        return

solve()