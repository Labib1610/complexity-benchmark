import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    vessels = []
    idx = 1
    for _ in range(j):
        t1 = int(data[idx]); t2 = int(data[idx+1])
        idx += 2
        vessels.append((t1, t2))
    
    # Sort by Beta duration descending (tie-breaker doesn't matter)
    vessels.sort(key=lambda x: -x[1])
    
    total_alpha = 0
    max_completion = 0
    for t1, t2 in vessels:
        total_alpha += t1
        completion = total_alpha + t2
        if completion > max_completion:
            max_completion = completion
    
    print(max_completion)

solve()