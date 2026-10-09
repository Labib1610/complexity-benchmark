import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    idx = 2
    job_idx = -1
    sum_p1 = 0
    sum_p2 = 0
    for i in range(1, j + 1):
        p1 = int(data[idx]); p2 = int(data[idx + 1]); idx += 2
        if job_idx == -1 and p1 + p2 > T:
            job_idx = i
        sum_p1 += p1
        sum_p2 += p2
    if job_idx != -1:
        sys.stdout.write(f"JOB {job_idx}\n")
        return
    if sum_p1 > T:
        sys.stdout.write("LOAD 1\n")
        return
    if sum_p2 > T:
        sys.stdout.write("LOAD 2\n")
        return

if __name__ == "__main__":
    solve()