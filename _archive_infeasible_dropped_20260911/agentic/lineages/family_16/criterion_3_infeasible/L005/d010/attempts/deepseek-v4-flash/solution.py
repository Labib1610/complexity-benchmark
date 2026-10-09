import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))
    sum1 = 0
    sum2 = 0
    for i in range(1, j+1):
        p1 = int(next(it))
        p2 = int(next(it))
        if p1 + p2 > T:
            print(f"JOB {i}")
            return
        sum1 += p1
        sum2 += p2
    if sum1 > T:
        print("LOAD 1")
    elif sum2 > T:
        print("LOAD 2")
    # else: should not happen

if __name__ == "__main__":
    main()