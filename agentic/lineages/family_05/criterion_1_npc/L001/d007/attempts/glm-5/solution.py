import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    models = []
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        g = int(next(it))
        models.append((a, b, g))
    
    # We need to select k models such that:
    # - All alpha values are distinct
    # - All beta values are distinct
    # - All gamma values are distinct
    # This is a 3D matching problem.
    
    # Since k <= 22, we can use meet-in-the-middle.
    # Split into two halves.
    
    if k == 0:
        print("YES")
        return
    
    if t < k:
        print("NO")
        return
    
    # For small k, try all subsets
    if k <= 11:
        from itertools import combinations
        for combo in combinations(range(t), k):
            a_set = set()
            b_set = set()
            g_set = set()
            valid = True
            for idx in combo:
                a, b, g = models[idx]
                if a in a_set or b in b_set or g in g_set:
                    valid = False
                    break
                a_set.add(a)
                b_set.add(b)
                g_set.add(g)
            if valid:
                print("YES")
                for idx in combo:
                    a, b, g = models[idx]
                    print(a, b, g)
                return
        print("NO")
        return
    
    # For larger k, use meet-in-the-middle
    # Split k into k1 and k2 where k1 + k2 = k
    # k <= 22, so one half is at most 11
    k1 = k // 2
    k2 = k - k1
    
    # Generate all valid subsets of size k1 from first half of models
    # and all valid subsets of size k2 from second half
    # Then check if they can be combined
    
    # To make this efficient, we need to be careful about which models go to which half
    # Let's split the models into two groups
    n1 = min(t, k * k)  # heuristic for first group size
    models1 = models[:n1]
    models2 = models[n1:]
    
    # Actually, let's just split models into two halves
    mid = t // 2
    models1 = models[:mid]
    models2 = models[mid:]
    
    # Generate all valid subsets of size k1 from models1
    left_subsets = []
    from itertools import combinations
    for combo in combinations(range(len(models1)), k1):
        a_set = set()
        b_set = set()
        g_set = set()
        valid = True
        for idx in combo:
            a, b, g = models1[idx]
            if a in a_set or b in b_set or g in g_set:
                valid = False
                break
            a_set.add(a)
            b_set.add(b)
            g_set.add(g)
        if valid:
            left_subsets.append((frozenset(a_set), frozenset(b_set), frozenset(g_set), combo))
    
    # Generate all valid subsets of size k2 from models2
    right_subsets = []
    for combo in combinations(range(len(models2)), k2):
        a_set = set()
        b_set = set()
        g_set = set()
        valid = True
        for idx in combo:
            a, b, g = models2[idx]
            if a in a_set or b in b_set or g in g_set:
                valid = False
                break
            a_set.add(a)
            b_set.add(b)
            g_set.add(g)
        if valid:
            right_subsets.append((frozenset(a_set), frozenset(b_set), frozenset(g_set), combo))
    
    # Check for compatible pairs
    # Build a dictionary for right subsets
    right_dict = {}
    for a_set, b_set, g_set, combo in right_subsets:
        key = (a_set, b_set, g_set)
        right_dict[key] = combo
    
    for la, lb, lg, lcombo in left_subsets:
        for ra, rb, rg, rcombo in right_subsets:
            if la.isdisjoint(ra) and lb.isdisjoint(rb) and lg.isdisjoint(rg):
                print("YES")
                for idx in lcombo:
                    a, b, g = models1[idx]
                    print(a, b, g)
                for idx in rcombo:
                    a, b, g = models2[idx]
                    print(a, b, g)
                return
    
    print("NO")

solve()