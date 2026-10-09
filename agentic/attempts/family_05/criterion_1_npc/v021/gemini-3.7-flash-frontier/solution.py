import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    k = int(input_data[0])
    t = int(input_data[1])
    
    points = []
    idx = 2
    for _ in range(t):
        x = int(input_data[idx]) - 1
        y = int(input_data[idx+1]) - 1
        z = int(input_data[idx+2]) - 1
        idx += 3
        points.append((x, y, z))
        
    # Group points by x, y, and z
    by_x = [[] for _ in range(k)]
    by_y = [[] for _ in range(k)]
    by_z = [[] for _ in range(k)]
    
    for i, (x, y, z) in enumerate(points):
        by_x[x].append(i)
        by_y[y].append(i)
        by_z[z].append(i)
        
    used_x = 0
    used_y = 0
    used_z = 0
    
    solution = []
    
    def search(count):
        nonlocal used_x, used_y, used_z
        if count == k:
            return True
        
        # Choose the constraint with the minimum number of valid choices (MRV)
        best_type = -1
        best_val = -1
        min_candidates = 999999
        best_list = []
        
        # Check unused x
        for x in range(k):
            if not (used_x & (1 << x)):
                candidates = []
                for p_idx in by_x[x]:
                    _, py, pz = points[p_idx]
                    if not (used_y & (1 << py)) and not (used_z & (1 << pz)):
                        candidates.append(p_idx)
                c_len = len(candidates)
                if c_len == 0:
                    return False
                if c_len < min_candidates:
                    min_candidates = c_len
                    best_list = candidates
                    if min_candidates == 1:
                        break
        
        if min_candidates > 1:
            # Check unused y
            for y in range(k):
                if not (used_y & (1 << y)):
                    candidates = []
                    for p_idx in by_y[y]:
                        px, _, pz = points[p_idx]
                        if not (used_x & (1 << px)) and not (used_z & (1 << pz)):
                            candidates.append(p_idx)
                    c_len = len(candidates)
                    if c_len == 0:
                        return False
                    if c_len < min_candidates:
                        min_candidates = c_len
                        best_list = candidates
                        if min_candidates == 1:
                            break
                            
        if min_candidates > 1:
            # Check unused z
            for z in range(k):
                if not (used_z & (1 << z)):
                    candidates = []
                    for p_idx in by_z[z]:
                        px, py, _ = points[p_idx]
                        if not (used_x & (1 << px)) and not (used_y & (1 << py)):
                            candidates.append(p_idx)
                    c_len = len(candidates)
                    if c_len == 0:
                        return False
                    if c_len < min_candidates:
                        min_candidates = c_len
                        best_list = candidates
                        if min_candidates == 1:
                            break
                            
        for p_idx in best_list:
            px, py, pz = points[p_idx]
            if (used_x & (1 << px)) or (used_y & (1 << py)) or (used_z & (1 << pz)):
                continue
            
            used_x |= (1 << px)
            used_y |= (1 << py)
            used_z |= (1 << pz)
            solution.append(p_idx)
            
            if search(count + 1):
                return True
                
            solution.pop()
            used_x &= ~(1 << px)
            used_y &= ~(1 << py)
            used_z &= ~(1 << pz)
            
        return False

    if search(0):
        print("YES")
        for p_idx in solution:
            x, y, z = points[p_idx]
            print(f"{x + 1} {y + 1} {z + 1}")
    else:
        print("NO")

if __name__ == '__main__':
    solve()