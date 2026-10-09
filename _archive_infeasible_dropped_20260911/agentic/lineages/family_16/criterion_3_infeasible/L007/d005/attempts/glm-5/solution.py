import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    
    job_idx = -1
    load1 = False
    load2 = False
    
    idx = 2
    for i in range(1, j + 1):
        p1 = int(data[idx]); p2 = int(data[idx + 1])
        idx += 2
        
        if job_idx == -1 and p1 + p2 > T:
            job_idx = i
        
        if not load1 and p1 > T:
            load1 = True
        if not load2 and p2 > T:
            load2 = True
    
    if job_idx != -1:
        print(f"JOB {job_idx}")
        return
    
    if load1:
        print("LOAD 1")
        return
    
    if load2:
        print("LOAD 2")
        return
    
    print("LOAD 1")

if __name__ == "__main__":
    solve()