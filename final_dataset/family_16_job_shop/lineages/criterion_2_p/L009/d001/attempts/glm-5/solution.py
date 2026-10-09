import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    effects = []
    for _ in range(j):
        p1 = int(next(it))
        p2 = int(next(it))
        effects.append((p1, p2))
    
    # Sort by (p1 - p2) in descending order
    effects.sort(key=lambda x: x[0] - x[1], reverse=True)
    
    # Compute prefix sums of geometry times
    prefix_geo = [0] * (j + 1)
    for i in range(1, j + 1):
        prefix_geo[i] = prefix_geo[i-1] + effects[i-1][0]
    
    # Compute suffix sums of lighting times
    suffix_light = [0] * (j + 2)
    for i in range(j, 0, -1):
        suffix_light[i] = suffix_light[i+1] + effects[i-1][1]
    
    # Find maximum total time over all split points k
    max_time = 0
    for k in range(1, j + 1):
        total = prefix_geo[k] + suffix_light[k]
        if total > max_time:
            max_time = total
    
    print(max_time)

solve()