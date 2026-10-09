import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    idx = 2
    jobs = []
    for i in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx+1])
        idx += 2
        jobs.append((p1, p2))
        if p1 + p2 > T:
            print(f"JOB {i+1}")
            return

    sum1 = sum(p1 for p1, _ in jobs)
    sum2 = sum(p2 for _, p2 in jobs)

    if sum1 > T:
        print("LOAD 1")
    elif sum2 > T:
        print("LOAD 2")

if __name__ == "__main__":
    main()