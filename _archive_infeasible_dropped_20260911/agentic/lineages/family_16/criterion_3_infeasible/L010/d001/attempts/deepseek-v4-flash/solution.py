import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    idx = 2
    sum_p1 = 0
    sum_p2 = 0
    for i in range(1, j + 1):
        p1 = int(data[idx])
        p2 = int(data[idx + 1])
        idx += 2
        sum_p1 += p1
        sum_p2 += p2
        if p1 + p2 > T:
            print(f"JOB {i}")
            return
    if sum_p1 > T:
        print("LOAD 1")
    elif sum_p2 > T:
        print("LOAD 2")

if __name__ == "__main__":
    main()