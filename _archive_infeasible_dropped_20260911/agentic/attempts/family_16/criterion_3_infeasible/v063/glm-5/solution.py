import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))
    
    total1 = 0
    total2 = 0
    job_idx = -1
    
    for i in range(1, j + 1):
        p1 = int(next(it))
        p2 = int(next(it))
        total1 += p1
        total2 += p2
        if job_idx == -1 and p1 + p2 > T:
            job_idx = i
    
    if job_idx != -1:
        print(f"JOB {job_idx}")
    elif total1 > T:
        print("LOAD 1")
    else:
        print("LOAD 2")

if __name__ == "__main__":
    main()