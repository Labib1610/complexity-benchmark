import sys
from itertools import combinations

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    paths = [tuple(map(int, input().split())) for _ in range(t)]
    
    if t == 0:
        print("NO")
        return
    
    target = k * (k + 1) // 2  # sum needed for each coordinate
    
    # Split paths into two halves
    mid = t // 2
    left_paths = paths[:mid]
    right_paths = paths[mid:]
    
    # Generate all possible selections from left half
    left_map = {}
    n_left = len(left_paths)
    for mask in range(1 << n_left):
        cnt = bin(mask).count('1')
        if cnt > k:
            continue
        sx = sy = sz = 0
        for i in range(n_left):
            if mask & (1 << i):
                x, y, z = left_paths[i]
                sx += x
                sy += y
                sz += z
        if sx <= target and sy <= target and sz <= target:
            left_map[(sx, sy, sz, cnt)] = mask
    
    # Generate all possible selections from right half
    right_map = {}
    n_right = len(right_paths)
    for mask in range(1 << n_right):
        cnt = bin(mask).count('1')
        if cnt > k:
            continue
        sx = sy = sz = 0
        for i in range(n_right):
            if mask & (1 << i):
                x, y, z = right_paths[i]
                sx += x
                sy += y
                sz += z
        if sx <= target and sy <= target and sz <= target:
            right_map[(sx, sy, sz, cnt)] = mask
    
    # Try to combine
    for (sx, sy, sz, cnt_l), mask_l in left_map.items():
        need_x = target - sx
        need_y = target - sy
        need_z = target - sz
        need_cnt = k - cnt_l
        if need_cnt < 0:
            continue
        key = (need_x, need_y, need_z, need_cnt)
        if key in right_map:
            mask_r = right_map[key]
            chosen = []
            for i in range(n_left):
                if mask_l & (1 << i):
                    chosen.append(left_paths[i])
            for i in range(n_right):
                if mask_r & (1 << i):
                    chosen.append(right_paths[i])
            print("YES")
            for p in chosen:
                print(*p)
            return
    
    print("NO")

if __name__ == "__main__":
    solve()