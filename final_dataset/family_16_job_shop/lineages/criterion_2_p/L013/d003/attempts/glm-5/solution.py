import sys

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(input_data[idx]); idx += 1
    group1 = []  # p1 <= p2, sort by p1 asc
    group2 = []  # p1 > p2, sort by p2 desc
    for _ in range(j):
        p1 = int(input_data[idx]); idx += 1
        p2 = int(input_data[idx]); idx += 1
        if p1 <= p2:
            group1.append((p1, p2))
        else:
            group2.append((p1, p2))
    group1.sort(key=lambda x: x[0])  # p1 asc
    group2.sort(key=lambda x: -x[1])  # p2 desc
    order = group1 + group2
    # compute peak stress
    total_p2 = sum(p2 for p1, p2 in order)
    peak = 0
    p1_sum = 0
    p2_suffix = total_p2
    for p1, p2 in order:
        p1_sum += p1
        # stress at this position = p1_sum + p2_suffix (p2_suffix includes current p2)
        stress = p1_sum + p2_suffix
        if stress > peak:
            peak = stress
        p2_suffix -= p2
    print(peak)

main()