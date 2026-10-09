import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    p1s = []
    p2s = []
    idx = 2
    for i in range(1, j+1):
        p1 = int(data[idx]); p2 = int(data[idx+1])
        idx += 2
        p1s.append(p1)
        p2s.append(p2)
        if p1 + p2 > T:
            print(f"JOB {i}")
            return

    # Check LOAD 1
    arr = sorted(p1s)
    S = 0
    prev = 0
    for k, val in enumerate(arr, start=1):
        S += val
        if S + prev > 2 * T:
            print("LOAD 1")
            return
        prev = S

    # Check LOAD 2
    arr = sorted(p2s)
    S = 0
    prev = 0
    for k, val in enumerate(arr, start=1):
        S += val
        if S + prev > 2 * T:
            print("LOAD 2")
            return
        prev = S

if __name__ == "__main__":
    main()