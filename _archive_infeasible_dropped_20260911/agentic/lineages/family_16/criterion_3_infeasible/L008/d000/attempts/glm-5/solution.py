import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(data[idx]); idx += 1
    T = int(data[idx]); idx += 1
    
    sum1 = 0
    sum2 = 0
    job_idx = -1
    
    for i in range(1, j + 1):
        p1 = int(data[idx]); idx += 1
        p2 = int(data[idx]); idx += 1
        sum1 += p1
        sum2 += p2
        if job_idx == -1 and p1 + p2 > T:
            job_idx = i
    
    if job_idx != -1:
        sys.stdout.write(f"JOB {job_idx}\n")
    elif sum1 > T:
        sys.stdout.write("LOAD 1\n")
    else:
        sys.stdout.write("LOAD 2\n")

main()