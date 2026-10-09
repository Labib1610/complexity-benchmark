import sys

def main():
    data = sys.stdin.buffer.read().split()
    j = int(data[0])
    jobs = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx+1])
        idx += 2
        jobs.append((p1, p2))
    
    group1 = []
    group2 = []
    for p1, p2 in jobs:
        if p1 <= p2:
            group1.append((p1, p2))
        else:
            group2.append((p1, p2))
    
    group1.sort(key=lambda x: x[0])
    group2.sort(key=lambda x: x[1], reverse=True)
    
    ordered = group1 + group2
    
    time_m1 = 0
    time_m2 = 0
    for p1, p2 in ordered:
        time_m1 += p1
        if time_m2 < time_m1:
            time_m2 = time_m1
        time_m2 += p2
    
    print(time_m2)

if __name__ == "__main__":
    main()