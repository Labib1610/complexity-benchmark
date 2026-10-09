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
    job_answer = None
    for i in range(1, j + 1):
        p1 = int(data[idx]); p2 = int(data[idx + 1]); idx += 2
        load1 += p1
        load2 += p2
        if p1 + p2 > T and job_answer is None:
            job_answer = i
    if job_answer is not None:
        print(f"JOB {job_answer}")
    elif load1 > T:
        print("LOAD 1")
    else:
        print("LOAD 2")

if __name__ == "__main__":
    main()