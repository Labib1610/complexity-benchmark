import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    jobs = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx+1])
        idx += 2
        jobs.append((p1, p2))
    
    first = []
    second = []
    for p1, p2 in jobs:
        if p1 < p2:
            first.append((p1, p2))
        else:
            second.append((p1, p2))
    
    first.sort(key=lambda x: x[0])
    second.sort(key=lambda x: x[1], reverse=True)
    
    order = first + second
    
    time_a = 0
    time_b = 0
    for p1, p2 in order:
        time_a += p1
        if time_b < time_a:
            time_b = time_a
        time_b += p2
    
    print(time_b)

if __name__ == "__main__":
    main()