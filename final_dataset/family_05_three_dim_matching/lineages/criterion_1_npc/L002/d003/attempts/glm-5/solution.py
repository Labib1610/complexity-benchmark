import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    k = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    if k == 0:
        print("YES")
        return
    
    pathways = []
    for _ in range(t):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        pathways.append((u, v, w))
    
    by_input = [[] for _ in range(k + 1)]
    for p in pathways:
        by_input[p[0]].append(p)
    
    for i in range(1, k + 1):
        if not by_input[i]:
            print("NO")
            return
    
    half = (k + 1) // 2
    A = list(range(1, half + 1))
    B = list(range(half + 1, k + 1))
    
    full_mask = (1 << k) - 1
    
    # Half A
    mapA = {}
    if A:
        states = {(0, 0): None}
        for inp in A:
            new_states = {}
            for (ov, ow), prev in states.items():
                for (u, v, w) in by_input[inp]:
                    bv = 1 << (v - 1)
                    bw = 1 << (w - 1)
                    if (ov & bv) or (ow & bw):
                        continue
                    nv = ov | bv
                    nw = ow | bw
                    key = (nv, nw)
                    if key not in new_states:
                        new_states[key] = (prev, (u, v, w))
            states = new_states
        for key, val in states.items():
            mapA[key] = val
    else:
        mapA[(0, 0)] = None
    
    # Half B
    found = False
    result = []
    
    if B:
        states = {(0, 0): None}
        for inp in B:
            if found:
                break
            new_states = {}
            for (ov, ow), prev in states.items():
                if found:
                    break
                for (u, v, w) in by_input[inp]:
                    bv = 1 << (v - 1)
                    bw = 1 << (w - 1)
                    if (ov & bv) or (ow & bw):
                        continue
                    nv = ov | bv
                    nw = ow | bw
                    key = (nv, nw)
                    if key in new_states:
                        continue
                    new_states[key] = (prev, (u, v, w))
                    comp_v = full_mask ^ nv
                    comp_w = full_mask ^ nw
                    comp_key = (comp_v, comp_w)
                    if comp_key in mapA:
                        found = True
                        cur = (prev, (u, v, w))
                        while cur is not None:
                            prev_ptr, triple = cur
                            result.append(triple)
                            cur = prev_ptr
                        curA = mapA[comp_key]
                        while curA is not None:
                            prev_ptr, triple = curA
                            result.append(triple)
                            curA = prev_ptr
                        break
            states = new_states
    else:
        if (0, 0) in mapA:
            found = True
            curA = mapA[(0, 0)]
            while curA is not None:
                prev_ptr, triple = curA
                result.append(triple)
                curA = prev_ptr
    
    if found:
        print("YES")
        for (u, v, w) in result:
            print(f"{u} {v} {w}")
    else:
        print("NO")

solve()