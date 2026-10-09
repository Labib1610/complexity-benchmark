import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(data[idx]); idx += 1
    T = int(data[idx]); idx += 1
    
    sum1 = 0
    sum2 = 0
    job_fail = -1
    
    for i in range(j):
        p1 = int(data[idx]); idx += 1
        p2 = int(data[idx]); idx += 1
        sum1 += p1
        sum2 += p2
        if p1 + p2 > T and job_fail == -1:
            job_fail = i + 1
    
    if job_fail != -1:
        print(f"JOB {job_fail}")
    else:
        if sum1 > T:
            print("LOAD 1")
        else:
            print("LOAD 2")

main()