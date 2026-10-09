import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    assets = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx]); p2 = int(data[idx+1])
        idx += 2
        assets.append((p1, p2))
    
    # Johnson's rule for two-machine flow shop
    assets.sort(key=lambda x: (min(x[0], x[1]), x[0] - x[1]))
    
    group1 = [a for a in assets if a[0] <= a[1]]
    group2 = [a for a in assets if a[0] > a[1]]
    
    order = group1 + group2
    
    drafting_done = 0
    rendering_done = 0
    for p1, p2 in order:
        drafting_done += p1
        if rendering_done < drafting_done:
            rendering_done = drafting_done + p2
        else:
            rendering_done += p2
    
    print(rendering_done)

solve()