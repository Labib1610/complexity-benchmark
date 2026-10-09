import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(input_data[idx]); idx += 1
    
    total_p1 = 0
    positive = []  # p2 > p1
    non_positive = []  # p2 <= p1
    
    for _ in range(j):
        p1 = int(input_data[idx]); idx += 1
        p2 = int(input_data[idx]); idx += 1
        total_p1 += p1
        if p2 > p1:
            positive.append((p1, p2))
        else:
            non_positive.append((p1, p2))
    
    # Sort positive by p1 ascending (so V stays above p1 once it exceeds)
    positive.sort(key=lambda x: x[0])
    # Sort non-positive by p1 ascending (minimize resets)
    non_positive.sort(key=lambda x: x[0])
    
    V = 0
    for p1, p2 in positive:
        if V > p1:
            V = V - p1 + p2
        else:
            V = p2
    
    for p1, p2 in non_positive:
        if V > p1:
            V = V - p1 + p2
        else:
            V = p2
    
    print(total_p1 + V)

solve()