import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    blocks = []
    for _ in range(j):
        p1 = int(next(it))
        p2 = int(next(it))
        blocks.append((p1, p2))
    
    # Sort by Johnson's rule: p1 < p2 first (by p1 ascending), then p1 >= p2 (by p2 descending)
    first_part = []
    second_part = []
    for p1, p2 in blocks:
        if p1 < p2:
            first_part.append((p1, p2))
        else:
            second_part.append((p1, p2))
    
    first_part.sort(key=lambda x: x[0])
    second_part.sort(key=lambda x: -x[1])
    
    ordered = first_part + second_part
    
    # Compute prefix sums of p1
    prefix_p1 = [0] * (j + 1)
    for i in range(j):
        prefix_p1[i + 1] = prefix_p1[i] + ordered[i][0]
    
    # Compute suffix sums of p2
    suffix_p2 = [0] * (j + 1)
    for i in range(j - 1, -1, -1):
        suffix_p2[i] = suffix_p2[i + 1] + ordered[i][1]
    
    # Find maximum crossover duration
    max_duration = 0
    for k in range(1, j + 1):
        duration = prefix_p1[k] + suffix_p2[k - 1]
        if duration > max_duration:
            max_duration = duration
    
    print(max_duration)

solve()