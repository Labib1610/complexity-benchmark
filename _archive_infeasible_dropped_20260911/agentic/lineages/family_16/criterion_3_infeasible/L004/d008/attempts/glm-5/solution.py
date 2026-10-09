import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(data[idx]); idx += 1
    T = int(data[idx]); idx += 1
    
    sum1 = 0
    sum2 = 0
    job_ans = -1
    
    for i in range(1, j + 1):
        p1 = int(data[idx]); idx += 1
        p2 = int(data[idx]); idx += 1
        if p1 + p2 > T and job_ans == -1:
            job_ans = i
        sum1 += p1
        sum2 += p2
    
    if job_ans != -1:
        print(f"JOB {job_ans}")
        return
    
    if sum1 > T:
        print("LOAD 1")
        return
    
    if sum2 > T:
        print("LOAD 2")
        return
    
    # Should not reach here per problem guarantee
    print("LOAD 1")

main()