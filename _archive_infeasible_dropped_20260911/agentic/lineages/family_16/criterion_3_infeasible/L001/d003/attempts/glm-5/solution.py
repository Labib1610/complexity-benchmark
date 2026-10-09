import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    idx = 2
    sum1 = 0
    sum2 = 0
    job_violation = -1
    for i in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx + 1])
        idx += 2
        sum1 += p1
        sum2 += p2
        if job_violation == -1 and p1 + p2 > T:
            job_violation = i + 1
    if job_violation != -1:
        sys.stdout.write(f"JOB {job_violation}\n")
    elif sum1 > T:
        sys.stdout.write("LOAD 1\n")
    else:
        sys.stdout.write("LOAD 2\n")

if __name__ == "__main__":
    main()