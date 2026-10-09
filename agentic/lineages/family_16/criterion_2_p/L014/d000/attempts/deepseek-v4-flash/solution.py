import sys

def solve():
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
        if p1 <= p2:
            first.append((p1, p2))
        else:
            second.append((p1, p2))
    
    first.sort(key=lambda x: x[0])
    second.sort(key=lambda x: -x[1])
    
    sequence = first + second
    
    oven_time = 0
    icing_time = 0
    for p1, p2 in sequence:
        oven_time += p1
        if icing_time < oven_time:
            icing_time = oven_time
        icing_time += p2
    
    print(icing_time)

if __name__ == "__main__":
    solve()