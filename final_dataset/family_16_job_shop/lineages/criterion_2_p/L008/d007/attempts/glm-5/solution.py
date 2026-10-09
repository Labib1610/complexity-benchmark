import sys

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(input_data[idx]); idx += 1
    
    group_a = []  # p1 <= p2
    group_b = []  # p1 > p2
    total_p1 = 0
    
    for _ in range(j):
        p1 = int(input_data[idx]); idx += 1
        p2 = int(input_data[idx]); idx += 1
        total_p1 += p1
        if p1 <= p2:
            group_a.append((p2, p1))
        else:
            group_b.append((p2, p1))
    
    group_a.sort()
    group_b.sort()
    
    excess = 0
    for p2, p1 in group_a:
        excess = max(excess - 2*p1, 0) + 2*p2
    for p2, p1 in group_b:
        excess = max(excess - 2*p1, 0) + 2*p2
    
    print(total_p1 + excess // 2)

main()