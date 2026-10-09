import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    k = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    protocols_by_m = [[] for _ in range(k+1)]
    for _ in range(t):
        m = int(input_data[idx]); idx += 1
        c = int(input_data[idx]); idx += 1
        f = int(input_data[idx]); idx += 1
        protocols_by_m[m].append((c-1, f-1))  # 0-indexed
    
    # Split materials 1..k into two halves
    half = k // 2
    A_mats = list(range(1, half+1))
    B_mats = list(range(half+1, k+1))
    
    full_catalyst = (1 << k) - 1
    full_finish = (1 << k) - 1
    
    # For A: enumerate assignments, store dpA[S_catalyst] = list of (F_finish, assignment_tuple)
    # assignment_tuple: for each material in A_mats, which (c,f) chosen
    
    # To save memory, store dpA[S] = dict {F_finish: assignment}
    # But could be large. Let's store dpA[S] = first found (F_finish, assignment)
    # and dpB[S] = dict {F_finish: assignment}
    
    # Actually we need to match: A uses catalyst set S, B uses catalyst set ~S & full
    # A uses finish set F_A, B uses finish set ~F_A & full
    # So for each S, for each F_A in dpA[S], check if (~F_A & full) in dpB[~S & full]
    
    # Store dpA[S] as a set of F_A values (with one assignment stored per F_A)
    # Store dpB[S] as a set of F_B values (with one assignment stored per F_B)
    
    def enumerate_half(mats):
        # Returns dict: catalyst_mask -> dict {finish_mask -> assignment}
        # assignment is tuple of (c, f) for each material in mats
        result = defaultdict(dict)
        n = len(mats)
        if n == 0:
            result[0] = {0: ()}
            return result
        
        # DFS
        # stack: (i, catalyst_mask, finish_mask, assignment)
        # We want to collect for each (catalyst_mask, finish_mask) one assignment
        # But storing all could be too much. Let's just store one per finish_mask per catalyst_mask.
        
        # Use iterative or recursive DFS
        sys.setrecursionlimit(10000)
        
        def dfs(i, cmask, fmask, assign):
            if i == n:
                if fmask not in result[cmask]:
                    result[cmask][fmask] = tuple(assign)
                return
            m = mats[i]
            for (c, f) in protocols_by_m[m]:
                cb = 1 << c
                fb = 1 << f
                if cmask & cb: continue
                if fmask & fb: continue
                assign.append((c, f))
                dfs(i+1, cmask | cb, fmask | fb, assign)
                assign.pop()
        
        dfs(0, 0, 0, [])
        return result
    
    dpA = enumerate_half(A_mats)
    dpB = enumerate_half(B_mats)
    
    # Now try to match
    for cmask_A, finish_dict_A in dpA.items():
        cmask_B = full_catalyst & ~cmask_A
        if cmask_B not in dpB: continue
        finish_dict_B = dpB[cmask_B]
        for fmask_A, assign_A in finish_dict_A.items():
            fmask_B_needed = full_finish & ~fmask_A
            if fmask_B_needed in finish_dict_B:
                assign_B = finish_dict_B[fmask_B_needed]
                # Reconstruct
                print("YES")
                out = []
                for i, m in enumerate(A_mats):
                    c, f = assign_A[i]
                    out.append(f"{m} {c+1} {f+1}")
                for i, m in enumerate(B_mats):
                    c, f = assign_B[i]
                    out.append(f"{m} {c+1} {f+1}")
                print("\n".join(out))
                return
    
    print("NO")

solve()