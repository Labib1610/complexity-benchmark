import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    tasks = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx]); p2 = int(data[idx+1])
        idx += 2
        tasks.append((p1, p2))
    
    # Johnson's rule for two-machine flow shop
    tasks.sort(key=lambda x: min(x[0], x[1]))
    
    wash_end = 0
    bake_end = 0
    for p1, p2 in tasks:
        wash_end += p1
        if wash_end > bake_end:
            bake_end = wash_end + p2
        else:
            bake_end += p2
    
    print(bake_end)

solve()