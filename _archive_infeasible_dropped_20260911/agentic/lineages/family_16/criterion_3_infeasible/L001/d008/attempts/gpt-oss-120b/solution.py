import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))
    p1 = []
    p2 = []
    for _ in range(j):
        p1.append(int(next(it)))
        p2.append(int(next(it)))
    # check local contradictions
    for idx, (a, b) in enumerate(zip(p1, p2), 1):
        if a + b > T:
            print(f"JOB {idx}")
            return
    # check global contradictions
    sum1 = sum(p1)
    sum2 = sum(p2)
    if sum1 > T:
        print("LOAD 1")
    else:
        print("LOAD 2")

if __name__ == "__main__":
    main()