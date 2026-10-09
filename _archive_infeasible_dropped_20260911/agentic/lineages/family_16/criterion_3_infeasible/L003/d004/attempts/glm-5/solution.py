import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    
    # Check JOB certificate: for each entity, p1 + p2 > T
    idx = 2
    for i in range(1, j + 1):
        p1 = int(data[idx])
        p2 = int(data[idx + 1])
        idx += 2
        if p1 + p2 > T:
            sys.stdout.write(f"JOB {i}\n")
            return
    
    # Check LOAD certificate: sum of spans in a domain > T
    sum1 = 0
    sum2 = 0
    idx = 2
    for _ in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx + 1])
        idx += 2
        sum1 += p1
        sum2 += p2
    
    if sum1 > T:
        sys.stdout.write("LOAD 1\n")
    else:
        sys.stdout.write("LOAD 2\n")

solve()