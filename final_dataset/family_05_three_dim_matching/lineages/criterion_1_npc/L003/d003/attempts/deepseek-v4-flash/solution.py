import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    k = int(next(it))
    t = int(next(it))
    
    # edges_by_left[x] = list of (y, z)
    edges_by_left = [[] for _ in range(k)]
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        edges_by_left[x].append((y, z))
    
    # Sort edges for each left for deterministic behavior
    for i in range(k):
        edges_by_left[i].sort()
    
    full_mask = (1 << k) - 1
    assignment = [None] * k
    
    # We'll do backtracking with bitmasks for right and keystone
    # and a mask for used lefts
    
    used_left_mask = 0
    used_right_mask = 0
    used_keystone_mask = 0
    
    # We'll store partial assignment
    
    # To speed up, we can reorder lefts by number of edges
    # But we need to map back
    
    # Compute number of options for each left given current masks
    def count_options(left):
        cnt = 0
        for y, z in edges_by_left[left]:
            if not (used_right_mask >> y) & 1 and not (used_keystone_mask >> z) & 1:
                cnt += 1
        return cnt
    
    sys.setrecursionlimit(1000000)
    
    def backtrack(step):
        nonlocal used_left_mask, used_right_mask, used_keystone_mask
        if step == k:
            return True
        # Find left with fewest options among unused
        best_left = -1
        best_cnt = 10**9
        for left in range(k):
            if not (used_left_mask >> left) & 1:
                cnt = count_options(left)
                if cnt == 0:
                    return False
                if cnt < best_cnt:
                    best_cnt = cnt
                    best_left = left
        if best_left == -1:
            return False
        # Try each option for best_left
        for y, z in edges_by_left[best_left]:
            if (used_right_mask >> y) & 1:
                continue
            if (used_keystone_mask >> z) & 1:
                continue
            # Place
            used_left_mask |= (1 << best_left)
            used_right_mask |= (1 << y)
            used_keystone_mask |= (1 << z)
            assignment[best_left] = (best_left, y, z)
            if backtrack(step + 1):
                return True
            # Undo
            used_left_mask ^= (1 << best_left)
            used_right_mask ^= (1 << y)
            used_keystone_mask ^= (1 << z)
            assignment[best_left] = None
        return False
    
    if backtrack(0):
        print("YES")
        for x, y, z in assignment:
            print(x+1, y+1, z+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()