import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(data[idx]); idx += 1
    T = int(data[idx]); idx += 1
    total1 = 0
    total2 = 0
    job_idx = -1
    for i in range(1, j + 1):
        p1 = int(data[idx]); idx += 1
        p2 = int(data[idx]); idx += 1
        total1 += p1
        total2 += p2
        if p1 + p2 > T and job_idx == -1:
            job_idx = i
    if job_idx != -1:
        sys.stdout.write(f"JOB {job_idx}\n")
    elif total1 > T:
        sys.stdout.write("LOAD 1\n")
    else:
        sys.stdout.write("LOAD 2\n")

main()