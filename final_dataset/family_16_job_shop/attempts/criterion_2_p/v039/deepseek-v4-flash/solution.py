import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    jobs = []
    idx = 1
    for _ in range(n):
        a = int(data[idx]); b = int(data[idx+1])
        idx += 2
        jobs.append((a, b))
    
    jobs.sort(key=lambda x: (-x[0], -x[1]))
    
    oven_time = 0
    icing_time = 0
    for a, b in jobs:
        oven_time += a
        if icing_time < oven_time:
            icing_time = oven_time
        icing_time += b
    
    print(icing_time)

if __name__ == "__main__":
    main()