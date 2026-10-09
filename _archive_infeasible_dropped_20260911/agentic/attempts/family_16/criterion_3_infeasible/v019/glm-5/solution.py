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
    for i in range(1, j + 1):
        p1 = int(data[idx])
        p2 = int(data[idx + 1])
        idx += 2
        sum1 += p1
        sum2 += p2
        if job_violation == -1 and p1 + p2 > T:
            job_violation = i
    if job_violation != -1:
        print(f"JOB {job_violation}")
    elif sum1 > T:
        print("LOAD 1")
    else:
        print("LOAD 2")

if __name__ == "__main__":
    main()