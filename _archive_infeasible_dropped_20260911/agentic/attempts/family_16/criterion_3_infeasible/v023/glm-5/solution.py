import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    idx = 2
    sum1 = 0
    sum2 = 0
    job_found = -1
    for i in range(1, j + 1):
        p1 = int(data[idx])
        p2 = int(data[idx + 1])
        idx += 2
        if job_found == -1 and p1 + p2 > T:
            job_found = i
        sum1 += p1
        sum2 += p2
    if job_found != -1:
        sys.stdout.write(f"JOB {job_found}\n")
    elif sum1 > T:
        sys.stdout.write("LOAD 1\n")
    else:
        sys.stdout.write("LOAD 2\n")

if __name__ == "__main__":
    solve()