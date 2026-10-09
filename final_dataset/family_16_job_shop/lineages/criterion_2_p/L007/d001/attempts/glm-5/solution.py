import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    manuscripts = []
    for _ in range(j):
        p1 = int(next(it))
        p2 = int(next(it))
        manuscripts.append((p1, p2))
    
    # Sort by Johnson's rule:
    # Group A: p1 <= p2, sort by p1 ascending
    # Group B: p1 > p2, sort by p2 descending
    # Concatenate A then B
    group_a = []
    group_b = []
    for p1, p2 in manuscripts:
        if p1 <= p2:
            group_a.append((p1, p2))
        else:
            group_b.append((p1, p2))
    
    group_a.sort(key=lambda x: x[0])
    group_b.sort(key=lambda x: x[1])
    
    order = group_a + group_b
    
    # Simulate the flow shop
    # t1: time when calligrapher finishes current job
    # t2: time when bookbinder finishes current job
    t1 = 0
    t2 = 0
    for p1, p2 in order:
        t1 += p1
        # Bookbinder starts at max(t2, t1) and takes p2
        if t1 > t2:
            t2 = t1 + p2
        else:
            t2 = t2 + p2
    
    print(t2)

if __name__ == "__main__":
    solve()