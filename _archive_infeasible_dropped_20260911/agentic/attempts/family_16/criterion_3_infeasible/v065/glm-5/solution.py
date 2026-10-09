import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    
    idx = 2
    total1 = 0
    total2 = 0
    job_error = -1
    
    for i in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx + 1])
        idx += 2
        total1 += p1
        total2 += p2
        if job_error == -1 and p1 + p2 > T:
            job_error = i + 1
    
    if job_error != -1:
        sys.stdout.write(f"JOB {job_error}")
    elif total1 > T:
        sys.stdout.write("LOAD 1")
    else:
        sys.stdout.write("LOAD 2")

if __name__ == "__main__":
    main()