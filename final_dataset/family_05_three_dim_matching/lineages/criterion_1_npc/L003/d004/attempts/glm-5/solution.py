import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    k = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    by_z = defaultdict(list)
    for _ in range(t):
        x = int(input_data[idx]); idx += 1
        y = int(input_data[idx]); idx += 1
        z = int(input_data[idx]); idx += 1
        by_z[z].append((x, y))
    
    z_list = sorted(by_z.keys(), key=lambda z: len(by_z[z]))
    
    full_mask = (1 << (2 * k)) - 1
    parent = {}
    parent[0] = (-1, -1, -1)  # (prev_state, x, y)
    
    for z in z_list:
        new_parent = {}
        pairs = by_z[z]
        for state, _ in parent.items():
            for x, y in pairs:
                bx = 1 << (x - 1)
                by_ = 1 << (k + y - 1)
                if state & bx == 0 and state & by_ == 0:
                    new_state = state | bx | by_
                    if new_state not in new_parent:
                        new_parent[new_state] = (state, x, y)
        parent = new_parent
        if not parent:
            print("NO")
            return
    
    if full_mask not in parent:
        print("NO")
        return
    
    print("YES")
    result = []
    state = full_mask
    zi = len(z_list) - 1
    while state != 0:
        prev_state, x, y = parent[state]
        z = z_list[zi]
        result.append((x, y, z))
        state = prev_state
        zi -= 1
    
    for x, y, z in result:
        print(f"{x} {y} {z}")

solve()