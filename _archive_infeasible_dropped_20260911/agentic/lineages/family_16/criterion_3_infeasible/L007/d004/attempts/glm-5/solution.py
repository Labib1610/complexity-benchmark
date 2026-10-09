import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    
    idx = 2
    job_cert = -1
    load1 = 0
    load2 = 0
    
    for i in range(1, j + 1):
        p1 = int(data[idx])
        p2 = int(data[idx + 1])
        idx += 2
        
        if p1 + p2 > T and job_cert == -1:
            job_cert = i
        
        load1 += p1
        load2 += p2
    
    if job_cert != -1:
        sys.stdout.write(f"JOB {job_cert}\n")
    elif load1 > T:
        sys.stdout.write("LOAD 1\n")
    else:
        sys.stdout.write("LOAD 2\n")

solve()