import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(data[idx]); idx += 1
    T = int(data[idx]); idx += 1
    
    s1 = 0
    s2 = 0
    job_idx = -1
    
    for i in range(1, j + 1):
        p1 = int(data[idx]); idx += 1
        p2 = int(data[idx]); idx += 1
        if p1 + p2 > T and job_idx == -1:
            job_idx = i
        s1 += p1
        s2 += p2
    
    if job_idx != -1:
        print(f"JOB {job_idx}")
    elif s1 > T:
        print("LOAD 1")
    else:
        print("LOAD 2")

main()