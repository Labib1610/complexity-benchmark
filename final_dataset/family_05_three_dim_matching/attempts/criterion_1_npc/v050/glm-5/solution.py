import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    k = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    # Group triples by x
    triples_by_x = defaultdict(list)
    for _ in range(t):
        x = int(input_data[idx]); idx += 1
        y = int(input_data[idx]); idx += 1
        z = int(input_data[idx]); idx += 1
        triples_by_x[x].append((y, z))
    
    full_mask = (1 << k) - 1
    
    # Split x's into two halves
    xs = list(range(1, k+1))
    mid = k // 2
    first_half = xs[:mid]
    second_half = xs[mid:]
    
    # For second half: enumerate all (y_mask, z_mask) and store with assignment
    # assignment: dict from x -> (y, z)
    second_results = {}  # (y_mask, z_mask) -> assignment dict
    
    def dfs_second(i, y_mask, z_mask, assignment):
        if i == len(second_half):
            second_results[(y_mask, z_mask)] = dict(assignment)
            return
        x = second_half[i]
        for (y, z) in triples_by_x[x]:
            yb = 1 << (y - 1)
            zb = 1 << (z - 1)
            if y_mask & yb or z_mask & zb:
                continue
            assignment[x] = (y, z)
            dfs_second(i + 1, y_mask | yb, z_mask | zb, assignment)
            del assignment[x]
    
    dfs_second(0, 0, 0, {})
    
    # For first half: enumerate and check complement
    first_assignment = {}
    found = [False]
    result = [None]
    
    def dfs_first(i, y_mask, z_mask, assignment):
        if found[0]:
            return
        if i == len(first_half):
            # Check if complement exists in second half
            need_y = full_mask ^ y_mask
            need_z = full_mask ^ z_mask
            key = (need_y, need_z)
            if key in second_results:
                found[0] = True
                result[0] = (dict(assignment), second_results[key])
            return
        x = first_half[i]
        for (y, z) in triples_by_x[x]:
            yb = 1 << (y - 1)
            zb = 1 << (z - 1)
            if y_mask & yb or z_mask & zb:
                continue
            assignment[x] = (y, z)
            dfs_first(i + 1, y_mask | yb, z_mask | zb, assignment)
            del assignment[x]
            if found[0]:
                return
    
    dfs_first(0, 0, 0, {})
    
    if found[0]:
        print("YES")
        a1, a2 = result[0]
        for x in range(1, k+1):
            if x in a1:
                y, z = a1[x]
            else:
                y, z = a2[x]
            print(f"{x} {y} {z}")
    else:
        print("NO")

solve()