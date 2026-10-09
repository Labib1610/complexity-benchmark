import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    idx = 2
    sum_gpu = 0
    sum_cpu = 0
    for i in range(1, j + 1):
        p1 = int(data[idx])
        p2 = int(data[idx + 1])
        idx += 2
        if p1 + p2 > T:
            print(f"JOB {i}")
            return
        sum_gpu += p1
        sum_cpu += p2
    if sum_gpu > T:
        print("LOAD 1")
    elif sum_cpu > T:
        print("LOAD 2")

if __name__ == "__main__":
    main()