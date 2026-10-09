import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(data[idx]); idx += 1
    
    group1 = []  # X <= Y, sort by X ascending
    group2 = []  # X > Y, sort by Y descending
    
    for _ in range(j):
        x = int(data[idx]); idx += 1
        y = int(data[idx]); idx += 1
        if x <= y:
            group1.append((x, y))
        else:
            group2.append((x, y))
    
    group1.sort(key=lambda t: t[0])
    group2.sort(key=lambda t: -t[1])
    
    order = group1 + group2
    
    total_x = 0
    total_y = 0
    for _, y in order:
        total_y += y
    
    best = 0
    for x, y in order:
        total_x += x
        total_y -= y
        val = total_x + total_y + y
        if val > best:
            best = val
    
    print(best)

main()