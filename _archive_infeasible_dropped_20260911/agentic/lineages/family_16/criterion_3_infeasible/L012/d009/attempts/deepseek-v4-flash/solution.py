import sys

def main():
    data = sys.stdin.buffer.read().split()
    j = int(data[0])
    T = int(data[1])
    
    sum_p1 = 0
    sum_p2 = 0
    idx = 2
    job_bottleneck = None
    
    for i in range(1, j + 1):
        p1 = int(data[idx]); p2 = int(data[idx+1])
        idx += 2
        sum_p1 += p1
        sum_p2 += p2
        if job_bottleneck is None and p1 + p2 > T:
            job_bottleneck = i
    
    if job_bottleneck is not None:
        sys.stdout.write(f"JOB {job_bottleneck}\n")
    elif sum_p1 > T:
        sys.stdout.write("LOAD 1\n")
    else:
        sys.stdout.write("LOAD 2\n")

if __name__ == "__main__":
    main()