import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    tasks = []
    for _ in range(j):
        p1 = int(next(it))
        p2 = int(next(it))
        tasks.append((p1, p2))
    
    # Sort by p2 descending (Johnson's rule for this problem)
    tasks.sort(key=lambda x: -x[1])
    
    # Compute prefix sums of p1
    prefix_p1 = [0] * (j + 1)
    for i in range(j):
        prefix_p1[i + 1] = prefix_p1[i] + tasks[i][0]
    
    # Compute max of (prefix_p1[i] + p2[i])
    max_val = 0
    for i in range(j):
        val = prefix_p1[i + 1] + tasks[i][1]
        if val > max_val:
            max_val = val
    
    # Total time is sum of all p1 plus the "gap" (max_val - prefix_p1[j])
    total = prefix_p1[j] + max_val - prefix_p1[j]
    print(total)

solve()