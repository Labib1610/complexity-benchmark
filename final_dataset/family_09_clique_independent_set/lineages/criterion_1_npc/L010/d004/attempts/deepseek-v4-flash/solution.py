import sys
from collections import defaultdict

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    # Split into two halves
    n1 = n // 2
    n2 = n - n1
    
    # Enumerate independent sets in first half
    # For each mask, check if it's independent
    size1 = 1 << n1
    indep1 = []
    for mask in range(size1):
        ok = True
        for i in range(n1):
            if mask & (1 << i):
                # Check if any neighbor in mask
                if adj[i] & mask:
                    ok = False
                    break
        if ok:
            indep1.append(mask)
    
    # For second half, we need to know which vertices in first half are adjacent
    # For each mask in second half, we can compute the forbidden mask in first half
    size2 = 1 << n2
    # Map from forbidden mask in first half -> list of (mask2, count)
    best = {}
    for mask2 in range(size2):
        ok = True
        forbidden = 0
        cnt = 0
        for j in range(n2):
            v = n1 + j
            if mask2 & (1 << j):
                cnt += 1
                # Check internal edges in second half
                for j2 in range(j+1, n2):
                    if mask2 & (1 << j2):
                        if adj[v] & (1 << (n1 + j2)):
                            ok = False
                            break
                if not ok:
                    break
                # Add neighbors in first half
                forbidden |= (adj[v] & ((1 << n1) - 1))
        if ok:
            # Store best (max count) for each forbidden mask
            if forbidden not in best or cnt > best[forbidden][0]:
                best[forbidden] = (cnt, mask2)
    
    # Now try to combine
    for mask1 in indep1:
        cnt1 = bin(mask1).count('1')
        if cnt1 > k:
            continue
        need = k - cnt1
        # For this mask1, we need a mask2 with count == need and forbidden & mask1 == 0
        # We can iterate over all forbidden masks that are disjoint with mask1
        # But we stored only max count per forbidden; we need exact count.
        # So better: store all (forbidden, cnt, mask2) and search.
        # Let's rebuild with all entries.
    
    # Rebuild with all entries
    all2 = []
    for mask2 in range(size2):
        ok = True
        forbidden = 0
        cnt = 0
        for j in range(n2):
            v = n1 + j
            if mask2 & (1 << j):
                cnt += 1
                for j2 in range(j+1, n2):
                    if mask2 & (1 << j2):
                        if adj[v] & (1 << (n1 + j2)):
                            ok = False
                            break
                if not ok:
                    break
                forbidden |= (adj[v] & ((1 << n1) - 1))
        if ok:
            all2.append((forbidden, cnt, mask2))
    
    # Group by forbidden mask
    from collections import defaultdict
    groups = defaultdict(list)
    for forb, cnt, mask2 in all2:
        groups[forb].append((cnt, mask2))
    
    # For each mask1, we need a group with forb & mask1 == 0 and cnt == need
    for mask1 in indep1:
        cnt1 = bin(mask1).count('1')
        if cnt1 > k:
            continue
        need = k - cnt1
        # Iterate over all forbidden masks that are disjoint with mask1
        # We can iterate over submasks of complement of mask1
        comp = ((1 << n1) - 1) ^ mask1
        sub = comp
        while True:
            if sub in groups:
                for cnt2, mask2 in groups[sub]:
                    if cnt2 == need:
                        # Found
                        ans = []
                        for i in range(n1):
                            if mask1 & (1 << i):
                                ans.append(i+1)
                        for j in range(n2):
                            if mask2 & (1 << j):
                                ans.append(n1 + j + 1)
                        print("YES")
                        print(" ".join(map(str, ans)))
                        return
            if sub == 0:
                break
            sub = (sub - 1) & comp
    
    print("NO")

if __name__ == "__main__":
    solve()