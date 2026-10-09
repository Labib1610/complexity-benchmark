import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(input_data[idx]); idx += 1
    
    set1 = []  # p1 <= p2, sort by p1 ascending
    set2 = []  # p1 > p2, sort by p2 descending
    
    for _ in range(j):
        p1 = int(input_data[idx]); idx += 1
        p2 = int(input_data[idx]); idx += 1
        if p1 <= p2:
            set1.append((p1, p2))
        else:
            set2.append((p1, p2))
    
    set1.sort(key=lambda x: x[0])
    set2.sort(key=lambda x: -x[1])
    
    order = set1 + set2
    
    m1_time = 0
    m2_time = 0
    
    for p1, p2 in order:
        m1_time += p1
        if m1_time > m2_time:
            m2_time = m1_time + p2
        else:
            m2_time += p2
    
    print(m2_time)

solve()