import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    idx = 2
    load1 = 0
    load2 = 0
    job_impossible = -1
    for i in range(1, j + 1):
        p1 = int(data[idx])
        p2 = int(data[idx + 1])
        idx += 2
        load1 += p1
        load2 += p2
        if job_impossible == -1 and p1 + p2 > T:
            job_impossible = i
    if job_impossible != -1:
        sys.stdout.write(f"JOB {job_impossible}\n")
    elif load1 > T:
        sys.stdout.write("LOAD 1\n")
    else:
        sys.stdout.write("LOAD 2\n")

if __name__ == "__main__":
    main()