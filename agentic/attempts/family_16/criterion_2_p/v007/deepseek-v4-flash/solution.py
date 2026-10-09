import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    jobs = []
    idx = 1
    for _ in range(n):
        a = int(data[idx])
        b = int(data[idx+1])
        idx += 2
        jobs.append((a, b))
    
    # Simulate
    time_m1 = 0
    time_m2 = 0
    for a, b in jobs:
        time_m1 += a
        if time_m2 < time_m1:
            time_m2 = time_m1
        time_m2 += b
    
    print(time_m2)

if __name__ == "__main__":
    main()