import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    idx = 2
    designs = []
    sum1 = 0
    sum2 = 0
    for i in range(1, j+1):
        p1 = int(data[idx]); p2 = int(data[idx+1])
        idx += 2
        designs.append((p1, p2))
        sum1 += p1
        sum2 += p2
        if p1 + p2 > T:
            print(f"JOB {i}")
            return
    # If no design spread, check track saturation
    if sum1 > T:
        print("LOAD 1")
        return
    if sum2 > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()