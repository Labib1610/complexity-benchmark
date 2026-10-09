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
    
    # Johnson's rule
    left = []  # p1 <= p2, sort by p1 ascending
    right = [] # p1 > p2, sort by p2 descending
    for p1, p2 in jobs:
        if p1 <= p2:
            left.append((p1, p2))
        else:
            right.append((p1, p2))
    
    left.sort(key=lambda x: x[0])
    right.sort(key=lambda x: -x[1])
    
    order = left + right
    
    # Compute minimal max time
    scout_time = 0
    total_p2 = sum(p2 for _, p2 in order)
    max_time = 0
    for p1, p2 in order:
        scout_time += p1
        total_p2 -= p2
        max_time = max(max_time, scout_time + total_p2)
    
    print(max_time)

if __name__ == "__main__":
    main()