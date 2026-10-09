import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    idx = 2
    # Check local contradiction: p1 + p2 > T
    for i in range(1, j + 1):
        p1 = int(data[idx]); p2 = int(data[idx + 1]); idx += 2
        if p1 + p2 > T:
            print(f"JOB {i}")
            return
    # Check global contradiction for c=1 and c=2
    # Sum of p values must exceed T
    sum1 = 0
    sum2 = 0
    idx = 2
    for i in range(j):
        p1 = int(data[idx]); p2 = int(data[idx + 1]); idx += 2
        sum1 += p1
        sum2 += p2
    if sum1 > T:
        print("LOAD 1")
    else:
        print("LOAD 2")

if __name__ == "__main__":
    main()