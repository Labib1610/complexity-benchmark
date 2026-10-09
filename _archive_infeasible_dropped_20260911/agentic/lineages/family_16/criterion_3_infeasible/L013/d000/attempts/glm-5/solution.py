import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(data[idx]); idx += 1
    T = int(data[idx]); idx += 1
    
    total1 = 0
    total2 = 0
    job_found = -1
    
    for i in range(1, j + 1):
        p1 = int(data[idx]); idx += 1
        p2 = int(data[idx]); idx += 1
        total1 += p1
        total2 += p2
        if job_found == -1 and p1 + p2 > T:
            job_found = i
    
    if job_found != -1:
        print(f"JOB {job_found}")
    elif total1 > T:
        print("LOAD 1")
    else:
        print("LOAD 2")

main()