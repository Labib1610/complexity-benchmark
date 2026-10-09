import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(data[idx]); idx += 1
    T = int(data[idx]); idx += 1
    
    total1 = 0
    total2 = 0
    job_idx = -1
    
    for i in range(j):
        p1 = int(data[idx]); idx += 1
        p2 = int(data[idx]); idx += 1
        total1 += p1
        total2 += p2
        if job_idx == -1 and p1 + p2 > T:
            job_idx = i + 1
    
    if job_idx != -1:
        print(f"JOB {job_idx}")
    elif total1 > T:
        print("LOAD 1")
    else:
        print("LOAD 2")

main()