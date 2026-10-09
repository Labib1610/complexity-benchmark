import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(data[idx]); idx += 1
    T = int(data[idx]); idx += 1
    
    total_p1 = 0
    total_p2 = 0
    job_fail = -1
    
    for i in range(j):
        p1 = int(data[idx]); idx += 1
        p2 = int(data[idx]); idx += 1
        if p1 + p2 > T and job_fail == -1:
            job_fail = i + 1
        total_p1 += p1
        total_p2 += p2
    
    if job_fail != -1:
        print(f"JOB {job_fail}")
    elif total_p1 > T:
        print("LOAD 1")
    else:
        print("LOAD 2")

main()