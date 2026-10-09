import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))
    
    # Check JOB condition: p1 + p2 > T
    for i in range(1, j + 1):
        p1 = int(next(it))
        p2 = int(next(it))
        if p1 + p2 > T:
            print(f"JOB {i}")
            return
    
    # Check LOAD condition: sum of p1 > T or sum of p2 > T
    # We already read all p1, p2 values above, but we need to track sums
    # Let's re-read the input to calculate sums (simpler logic)
    # Actually, we need to re-iterate. Let's restructure.
    pass

def main_correct():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))
    
    sum_p1 = 0
    sum_p2 = 0
    job_index = -1
    
    for i in range(1, j + 1):
        p1 = int(next(it))
        p2 = int(next(it))
        
        if job_index == -1 and p1 + p2 > T:
            job_index = i
        
        sum_p1 += p1
        sum_p2 += p2
    
    if job_index != -1:
        print(f"JOB {job_index}")
    elif sum_p1 > T:
        print("LOAD 1")
    else:
        print("LOAD 2")

if __name__ == "__main__":
    main_correct()