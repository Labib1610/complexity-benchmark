import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    ships = []
    idx = 1
    for _ in range(j):
        t1 = int(data[idx]); t2 = int(data[idx+1])
        idx += 2
        ships.append((t1, t2))
    
    # Johnson's rule for 2-machine flow shop
    group1 = []  # t1 <= t2, sort by t1 ascending
    group2 = []  # t1 > t2, sort by t2 descending
    for t1, t2 in ships:
        if t1 <= t2:
            group1.append((t1, t2))
        else:
            group2.append((t1, t2))
    
    group1.sort(key=lambda x: x[0])
    group2.sort(key=lambda x: x[1], reverse=True)
    
    order = group1 + group2
    
    time1 = 0
    time2 = 0
    for t1, t2 in order:
        time1 += t1
        if time2 < time1:
            time2 = time1 + t2
        else:
            time2 += t2
    
    print(time2)

solve()