import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))
    
    p1_list = []
    p2_list = []
    total_p1 = 0
    total_p2 = 0
    job_impossible = -1
    
    for i in range(j):
        p1 = int(next(it))
        p2 = int(next(it))
        p1_list.append(p1)
        p2_list.append(p2)
        total_p1 += p1
        total_p2 += p2
        if p1 + p2 > T:
            job_impossible = i + 1
    
    if job_impossible != -1:
        print(f"JOB {job_impossible}")
        return
    
    if total_p1 > T:
        print("LOAD 1")
        return
    
    if total_p2 > T:
        print("LOAD 2")
        return
    
    # Check if any single team violates JOB constraint
    for i in range(j):
        if p1_list[i] + p2_list[i] > T:
            print(f"JOB {i + 1}")
            return
    
    # Check LOAD 1: all primary vehicles must fit in Lane 1
    if total_p1 > T:
        print("LOAD 1")
        return
    
    # Check LOAD 2: all secondary vehicles must fit in Lane 2
    if total_p2 > T:
        print("LOAD 2")
        return
    
    # If we reach here, the problem guarantees one of the above conditions holds
    # This should not happen given problem constraints
    print("LOAD 1")

if __name__ == "__main__":
    solve()