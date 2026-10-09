import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    p1 = [0]*j
    p2 = [0]*j
    idx = 1
    for i in range(j):
        p1[i] = int(data[idx]); p2[i] = int(data[idx+1])
        idx += 2

    # Sort by p1 ascending; ties by p2 ascending.
    order = sorted(range(j), key=lambda i: (p1[i], p2[i]))
    # Process in reverse order: highest priority first.
    # This is equivalent to Johnson's rule for two-machine flow shop.
    radar_time = 0
    sample_time = 0
    for k in range(j-1, -1, -1):
        i = order[k]
        radar_time += p1[i]
        if sample_time < radar_time:
            sample_time = radar_time + p2[i]
        else:
            sample_time += p2[i]

    print(sample_time)

solve()