import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    k = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    cands = []
    for _ in range(t):
        x = int(input_data[idx]) - 1; idx += 1
        y = int(input_data[idx]) - 1; idx += 1
        z = int(input_data[idx]) - 1; idx += 1
        cands.append((x, y, z))
    
    if k == 0:
        print("YES")
        return
    
    if t < k:
        print("NO")
        return
    
    half = k // 2
    g1 = [c for c in cands if c[0] < half]
    g2 = [c for c in cands if c[0] >= half]
    
    def gen_subsets(group):
        n = len(group)
        results = []
        for mask in range(1 << n):
            ym = 0; zm = 0; cnt = 0; valid = True
            for i in range(n):
                if mask & (1 << i):
                    x, y, z = group[i]
                    if ym & (1 << y) or zm & (1 << z):
                        valid = False
                        break
                    ym |= (1 << y)
                    zm |= (1 << z)
                    cnt += 1
            if valid:
                results.append((cnt, ym, zm, mask))
        return results
    
    s1 = gen_subsets(g1)
    s2 = gen_subsets(g2)
    
    best2 = defaultdict(list)
    for cnt, ym, zm, mask in s2:
        key = (ym, zm)
        if len(best2[key]) < cnt:
            best2[key] = [mask]
    
    for cnt1, ym1, zm1, mask1 in s1:
        need = k - cnt1
        if need < 0 or need > len(g2):
            continue
        for (ym2, zm2), masks in best2.items():
            if len(masks) == 0:
                continue
            if (ym1 & ym2) == 0 and (zm1 & zm2) == 0:
                # Need to verify exact count = need
                # best2 stores by mask, need to check actual count
                mask2 = masks[0]
                cnt2 = bin(mask2).count('1')
                if cnt2 == need:
                    result = []
                    for i in range(len(g1)):
                        if mask1 & (1 << i):
                            result.append(g1[i])
                    for i in range(len(g2)):
                        if mask2 & (1 << i):
                            result.append(g2[i])
                    print("YES")
                    for x, y, z in result:
                        print(f"{x+1} {y+1} {z+1}")
                    return
    
    print("NO")

solve()