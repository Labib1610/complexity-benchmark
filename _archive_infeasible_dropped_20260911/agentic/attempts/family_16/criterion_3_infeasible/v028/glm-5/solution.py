import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))
    
    total_p1 = 0
    total_p2 = 0
    job_index = 0
    
    for i in range(1, j + 1):
        p1 = int(next(it))
        p2 = int(next(it))
        if p1 + p2 > T:
            print(f"JOB {i}")
            return
        total_p1 += p1
        total_p2 += p2
    
    if total_p1 > T:
        print("LOAD 1")
    elif total_p2 > T:
        print("LOAD 2")

if __name__ == "__main__":
    solve()