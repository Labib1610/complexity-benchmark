import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    j = int(input_data[0])
    trains = []
    idx = 1
    for _ in range(j):
        s = int(input_data[idx]); c = int(input_data[idx+1])
        idx += 2
        trains.append((s, c))
    
    group1 = []  # s <= c, sort by s ascending
    group2 = []  # s > c, sort by c descending
    for s, c in trains:
        if s <= c:
            group1.append((s, c))
        else:
            group2.append((s, c))
    
    group1.sort(key=lambda x: x[0])
    group2.sort(key=lambda x: x[1], reverse=True)
    
    ordered = group1 + group2
    
    A = 0
    B = 0
    for s, c in ordered:
        A += s
        if A > B:
            B = A + c
        else:
            B = B + c
    
    print(B)

solve()