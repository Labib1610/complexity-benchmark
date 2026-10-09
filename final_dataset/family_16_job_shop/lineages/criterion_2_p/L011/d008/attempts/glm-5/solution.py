import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(input_data[idx]); idx += 1
    
    group_a = []  # p1 <= p2, sort by p1 ascending
    group_b = []  # p1 > p2, sort by p2 descending
    
    for _ in range(j):
        p1 = int(input_data[idx]); idx += 1
        p2 = int(input_data[idx]); idx += 1
        if p1 <= p2:
            group_a.append((p1, p2))
        else:
            group_b.append((p1, p2))
    
    group_a.sort(key=lambda x: x[0])
    group_b.sort(key=lambda x: x[1], reverse=True)
    
    order = group_a + group_b
    
    structural_end = 0
    cargo_end = 0
    
    for p1, p2 in order:
        structural_end += p1
        cargo_start = max(structural_end, cargo_end)
        cargo_end = cargo_start + p2
    
    print(cargo_end)

solve()