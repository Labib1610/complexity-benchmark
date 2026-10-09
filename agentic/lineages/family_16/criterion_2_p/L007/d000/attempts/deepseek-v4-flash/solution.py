import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    jobs = []
    idx = 1
    for i in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx + 1])
        idx += 2
        jobs.append((p1, p2, i))
    
    # Johnson's rule
    A = []
    B = []
    for p1, p2, i in jobs:
        if p1 <= p2:
            A.append((p1, p2, i))
        else:
            B.append((p1, p2, i))
    
    A.sort(key=lambda x: x[0])  # sort by p1 ascending
    B.sort(key=lambda x: x[1], reverse=True)  # sort by p2 descending
    
    order = A + B
    
    # Compute makespan
    time1 = 0
    time2 = 0
    for p1, p2, _ in order:
        time1 += p1
        if time2 < time1:
            time2 = time1
        time2 += p2
    
    print(time2)

if __name__ == "__main__":
    main()