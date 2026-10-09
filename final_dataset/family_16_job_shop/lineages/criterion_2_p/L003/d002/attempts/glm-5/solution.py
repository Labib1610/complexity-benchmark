import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    j = int(input_data[0])
    idx = 1
    group1 = []  # p1 <= p2, sort by p1 ascending
    group2 = []  # p1 > p2, sort by p2 descending
    
    for _ in range(j):
        p1 = int(input_data[idx])
        p2 = int(input_data[idx + 1])
        idx += 2
        if p1 <= p2:
            group1.append((p1, p2))
        else:
            group2.append((p1, p2))
    
    group1.sort(key=lambda x: x[0])
    group2.sort(key=lambda x: x[1], reverse=True)
    
    orders = group1 + group2
    
    m1_time = 0
    m2_time = 0
    
    for p1, p2 in orders:
        m1_time += p1
        if m1_time > m2_time:
            m2_time = m1_time + p2
        else:
            m2_time += p2
    
    print(m2_time)

solve()