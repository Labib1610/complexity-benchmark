import sys

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(input_data[idx]); idx += 1
    groupA = []  # p1 <= p2, sort by p1 ascending
    groupB = []  # p1 > p2, sort by p2 descending
    total_p2 = 0
    for _ in range(j):
        p1 = int(input_data[idx]); idx += 1
        p2 = int(input_data[idx]); idx += 1
        total_p2 += p2
        if p1 <= p2:
            groupA.append((p1, p2))
        else:
            groupB.append((p2, p1))  # store p2 first for sorting by p2 desc
    
    groupA.sort()  # sort by p1 ascending (then p2, doesn't matter)
    groupB.sort()  # sort by p2 ascending, then reverse
    groupB.reverse()  # now p2 descending
    
    max_val = 0
    buffer = 0  # this is prefix_p1 - prefix_p2 (running sum of p1 - p2)
    # Actually, let me track: running_p1_sum - running_p2_sum_before
    # f(k) = prefix_p1[k] - prefix_p2[k-1]
    # = (prefix_p1[k] - prefix_p2[k]) + p2_k
    # = running_diff + p2_k where running_diff = sum(p1-p2) so far including current
    
    running_diff = 0
    for p1, p2 in groupA:
        running_diff += p1 - p2
        val = running_diff + p2  # = prefix_p1 - prefix_p2_prev
        if val > max_val:
            max_val = val
    for p2, p1 in groupB:
        running_diff += p1 - p2
        val = running_diff + p2
        if val > max_val:
            max_val = val
    
    idle = max(0, max_val)
    print(idle + total_p2)

main()