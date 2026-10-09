import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    orders = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx]); p2 = int(data[idx+1])
        idx += 2
        orders.append((p1, p2))
    
    # Johnson's rule: sort by min(p1, p2), with p1-first group before p2-first group
    orders.sort(key=lambda x: (0 if x[0] <= x[1] else 1, min(x[0], x[1])))
    
    prep_end = 0
    asm_end = 0
    for p1, p2 in orders:
        prep_end += p1
        if prep_end > asm_end:
            asm_end = prep_end + p2
        else:
            asm_end += p2
    
    print(asm_end)

solve()