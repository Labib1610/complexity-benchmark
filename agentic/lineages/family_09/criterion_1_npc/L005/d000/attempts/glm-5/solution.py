import sys
sys.setrecursionlimit(1000000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    adj = [0] * (n + 1)
    for i in range(1, n + 1):
        adj[i] = (1 << (n + 1)) - 1 - (1 << i)
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] &= ~(1 << v)
        adj[v] &= ~(1 << u)
    
    half = n // 2
    L = half
    R = n - half
    
    left_nodes = list(range(1, L + 1))
    right_nodes = list(range(L + 1, n + 1))
    
    left_masks = []
    for i in range(1, L + 1):
        mask = 0
        for j in range(1, L + 1):
            if adj[i] & (1 << j):
                mask |= (1 << (j - 1))
        left_masks.append(mask)
    
    right_masks = []
    for i in range(L + 1, n + 1):
        mask = 0
        for j in range(L + 1, n + 1):
            if adj[i] & (1 << j):
                mask |= (1 << (j - L - 1))
        right_masks.append(mask)
    
    best_left = {}
    for mask in range(1 << L):
        if mask == 0:
            continue
        lsb = mask & -mask
        idx = (lsb.bit_length() - 1)
        prev = mask ^ lsb
        if prev == 0:
            clique_mask = left_masks[idx]
        else:
            clique_mask = best_left[prev][0] & left_masks[idx]
        if clique_mask == mask:
            cnt = mask.bit_count()
            if cnt not in best_left or best_left[cnt][1] < mask:
                best_left[cnt] = (clique_mask, mask)
    
    best_right = {}
    for mask in range(1 << R):
        if mask == 0:
            continue
        lsb = mask & -mask
        idx = (lsb.bit_length() - 1)
        prev = mask ^ lsb
        if prev == 0:
            clique_mask = right_masks[idx]
        else:
            clique_mask = best_right[prev][0] & right_masks[idx]
        if clique_mask == mask:
            cnt = mask.bit_count()
            if cnt not in best_right or best_right[cnt][1] < mask:
                best_right[cnt] = (clique_mask, mask)
    
    right_compat = []
    for i in range(L + 1, n + 1):
        mask = 0
        for j in range(1, L + 1):
            if adj[i] & (1 << j):
                mask |= (1 << (j - 1))
        right_compat.append(mask)
    
    right_compat_mask = {}
    for cnt, (clique_mask, mask) in list(best_right.items()):
        compat = (1 << L) - 1
        bits = mask
        while bits:
            lsb = bits & -bits
            idx = (lsb.bit_length() - 1)
            compat &= right_compat[idx]
            bits ^= lsb
        right_compat_mask[mask] = compat
    
    for lc in range(min(k, L) + 1):
        if lc not in best_left:
            continue
        left_clique_mask, left_mask = best_left[lc]
        need = k - lc
        if need < 0 or need > R:
            continue
        if need == 0:
            result = []
            bits = left_mask
            while bits:
                lsb = bits & -bits
                idx = (lsb.bit_length() - 1)
                result.append(left_nodes[idx])
                bits ^= lsb
            print("YES")
            print(' '.join(map(str, result)))
            return
        if need not in best_right:
            continue
        for rc, (right_clique_mask, right_mask) in best_right.items():
            if rc != need:
                continue
            compat = right_compat_mask[right_mask]
            if (left_mask & compat) == left_mask:
                result = []
                bits = left_mask
                while bits:
                    lsb = bits & -bits
                    idx = (lsb.bit_length() - 1)
                    result.append(left_nodes[idx])
                    bits ^= lsb
                bits = right_mask
                while bits:
                    lsb = bits & -bits
                    idx = (lsb.bit_length() - 1)
                    result.append(right_nodes[idx])
                    bits ^= lsb
                print("YES")
                print(' '.join(map(str, result)))
                return
    
    print("NO")

if __name__ == "__main__":
    solve()