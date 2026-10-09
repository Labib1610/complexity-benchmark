import sys

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(input_data[idx]); idx += 1
    group1 = []  # p1 <= p2, sort by p1 asc
    group2 = []  # p1 > p2, sort by p2 desc
    for i in range(j):
        p1 = int(input_data[idx]); idx += 1
        p2 = int(input_data[idx]); idx += 1
        if p1 <= p2:
            group1.append((p1, p2))
        else:
            group2.append((p1, p2))
    group1.sort(key=lambda x: x[0])
    group2.sort(key=lambda x: -x[1])
    order = group1 + group2
    total_p2 = sum(p2 for _, p2 in order)
    prefix_p1 = 0
    suffix_p2 = total_p2
    best = 0
    for p1, p2 in order:
        prefix_p1 += p1
        val = prefix_p1 + suffix_p2
        if val > best:
            best = val
        suffix_p2 -= p2
    print(best)

main()