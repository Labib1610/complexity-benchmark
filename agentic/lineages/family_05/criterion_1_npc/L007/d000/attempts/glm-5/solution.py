import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    k = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    options = [[] for _ in range(k + 1)]
    for _ in range(t):
        e = int(input_data[idx]); idx += 1
        s = int(input_data[idx]); idx += 1
        p = int(input_data[idx]); idx += 1
        options[e].append((s - 1, p - 1))
    
    # DP: state is (s_mask, p_mask), value is list of (s, p) choices to reconstruct
    # Process enzymes 1..k in order
    # current: dict mapping (s_mask, p_mask) -> parent info for reconstruction
    
    # Use dict: key = (s_mask, p_mask), value = (prev_s_mask, prev_p_mask, s, p)
    current = {(0, 0): None}
    
    for e in range(1, k + 1):
        next_level = {}
        for (sm, pm), parent_info in current.items():
            for (s, p) in options[e]:
                sb = 1 << s
                pb = 1 << p
                if sm & sb == 0 and pm & pb == 0:
                    nsm = sm | sb
                    npm = pm | pb
                    key = (nsm, npm)
                    if key not in next_level:
                        next_level[key] = (sm, pm, s, p)
        current = next_level
        if not current:
            print("NO")
            return
    
    full = (1 << k) - 1
    target = (full, full)
    
    if target not in current:
        print("NO")
        return
    
    # Reconstruct
    result = []
    # We need to trace back through all levels, but we only kept the last level
    # Need to re-run DP storing all levels
    
    # Re-run with all levels stored
    levels = [None] * (k + 1)
    levels[0] = {(0, 0): None}
    
    for e in range(1, k + 1):
        next_level = {}
        for (sm, pm), parent_info in levels[e - 1].items():
            for (s, p) in options[e]:
                sb = 1 << s
                pb = 1 << p
                if sm & sb == 0 and pm & pb == 0:
                    nsm = sm | sb
                    npm = pm | pb
                    key = (nsm, npm)
                    if key not in next_level:
                        next_level[key] = (sm, pm, s, p)
        levels[e] = next_level
        if not next_level:
            print("NO")
            return
    
    if target not in levels[k]:
        print("NO")
        return
    
    # Reconstruct path
    sm, pm = full, full
    for e in range(k, 0, -1):
        info = levels[e][(sm, pm)]
        psm, ppm, s, p = info
        result.append((e, s + 1, p + 1))
        sm, pm = psm, ppm
    
    result.reverse()
    print("YES")
    for e, s, p in result:
        print(f"{e} {s} {p}")

solve()