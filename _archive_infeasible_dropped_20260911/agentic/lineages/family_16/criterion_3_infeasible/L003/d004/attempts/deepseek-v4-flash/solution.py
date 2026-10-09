import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    p1 = []
    p2 = []
    idx = 2
    for _ in range(j):
        p1.append(int(data[idx]))
        p2.append(int(data[idx+1]))
        idx += 2

    # Check JOB certificates
    for i in range(j):
        if p1[i] + p2[i] > T:
            print(f"JOB {i+1}")
            return

    # Check LOAD certificates
    sum1 = sum(p1)
    sum2 = sum(p2)
    if sum1 > T:
        print("LOAD 1")
        return
    if sum2 > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()