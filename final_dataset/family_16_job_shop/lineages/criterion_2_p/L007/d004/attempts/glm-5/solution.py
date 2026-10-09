import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    j = int(input_data[0])
    p1 = [0] * j
    p2 = [0] * j
    idx = 1
    for i in range(j):
        p1[i] = int(input_data[idx])
        p2[i] = int(input_data[idx + 1])
        idx += 2
    
    total_p1 = sum(p1)
    total_p2 = sum(p2)
    
    # Sort manuscripts by p1 - p2 in descending order
    manuscripts = sorted(zip(p1, p2), key=lambda x: x[0] - x[2], reverse=True)
    
    # Compute prefix sums of p1 and suffix sums of p2
    prefix_p1 = [0] * (j + 1)
    for i in range(j):
        prefix_p1[i + 1] = prefix_p1[i] + manuscripts[i][0]
    
    suffix_p2 = [0] * (j + 1)
    for i in range(j - 1, -1, -1):
        suffix_p2[i] = suffix_p2[i + 1] + manuscripts[i][1]
    
    # Compute the maximum inspection time for this arrangement
    max_time = 0
    for k in range(1, j + 1):
        current_time = prefix_p1[k] + suffix_p2[k - 1]
        if current_time > max_time:
            max_time = current_time
    
    print(max_time)

solve()