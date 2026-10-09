import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    durations = []
    idx = 2
    for _ in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx+1])
        idx += 2
        durations.append((p1, p2))
    
    # Check JOB certificates
    for i, (p1, p2) in enumerate(durations, start=1):
        if p1 + p2 > T:
            print(f"JOB {i}")
            return
    
    # Check LOAD certificates
    sum1 = sum(p1 for p1, _ in durations)
    sum2 = sum(p2 for _, p2 in durations)
    if sum1 > T:
        print("LOAD 1")
        return
    if sum2 > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()