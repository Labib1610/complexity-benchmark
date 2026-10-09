import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= (1 << (v - 1))
        adj[v] |= (1 << (u - 1))

    for i in range(1, n + 1):
        adj[i] |= (1 << (i - 1))

    if k == 1:
        print("YES")
        print(1)
        return

    half_n = n // 2
    left_size = half_n
    right_size = n - half_n

    left_mask = (1 << left_size) - 1
    right_mask = ((1 << n) - 1) ^ left_mask

    # Precompute conflict masks for right partition
    right_conflict_masks = []
    for i in range(left_size + 1, n + 1):
        conflict = 0
        adj_i = adj[i]
        for j in range(left_size + 1, n + 1):
            if (adj_i >> (j - 1)) & 1:
                conflict |= (1 << (j - left_size - 1))
        right_conflict_masks.append(conflict)

    # Compute all independent sets in right partition
    right_indep_sets = [0] * (right_size + 1)
    for mask in range(1 << right_size):
        if (mask & right_mask_for_check(mask, right_conflict_masks, right_size)) == 0:
            cnt = mask.bit_count()
            if cnt >= k:
                print("YES")
                res = []
                for j in range(right_size):
                    if (mask >> j) & 1:
                        res.append(left_size + 1 + j)
                print(*(res[:k]))
                return
            if right_indep_sets[cnt] == 0:
                right_indep_sets[mask.bit_count()] = mask

    # Iterate over independent sets in left partition
    for mask in range(1 << left_size):
        if (mask & left_mask_for_check(mask, adj, left_size)) == 0:
            cnt = mask.bit_count()
            if cnt >= k:
                print("YES")
                res = []
                for j in range(left_size):
                    if (mask >> j) & 1:
                        res.append(j + 1)
                print(*(res[:k]))
                return
            
            need = k - cnt
            if need <= right_size and right_indep_sets[need] != 0:
                # Check compatibility
                right_m = right_indep_sets[need]
                forbidden_right = 0
                for j in range(left_size):
                    if (mask >> j) & 1:
                        u = j + 1
                        adj_u = adj[u]
                        for r_idx in range(right_size):
                            v_global = left_size + 1 + r_idx
                            if (adj_u >> (v_global - 1)) & 1:
                                forbidden_right |= (1 << r_idx)
                
                if (right_m & forbidden_right) == 0:
                    print("YES")
                    res = []
                    for j in range(left_size):
                        if (mask >> j) & 1:
                            res.append(j + 1)
                    for r_idx in range(right_size):
                        if (right_m >> r_idx) & 1:
                            res.append(left_size + 1 + r_idx)
                    print(*res)
                    return

    print("NO")

def right_mask_for_check(mask, right_conflict_masks, right_size):
    # Returns the conflict mask for the given 'mask' within the right partition
    # Actually this function calculates the conflicts induced by 'mask' itself
    conflict = 0
    for i in range(right_size):
        if (mask >> i) & 1:
            conflict |= right_conflict_masks[i]
    return conflict

def left_mask_for_check(mask, adj, left_size):
    # Returns the conflict mask for the given 'mask' within the left partition
    conflict = 0
    for i in range(left_size):
        if (mask >> i) & 1:
            u = i + 1
            adj_u = adj[u]
            for j in range(left_size):
                if (adj_u >> j) & 1:
                    conflict |= (1 << j)
    return conflict

if __name__ == '__main__':
    solve()