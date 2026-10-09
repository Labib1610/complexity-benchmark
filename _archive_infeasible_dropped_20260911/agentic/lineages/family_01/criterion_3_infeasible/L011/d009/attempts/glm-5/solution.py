import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    # For each sequence, store positions where it has a 1
    seq_positions = [[] for _ in range(n + 1)]
    
    for k in range(1, m + 1):
        u = int(next(it))
        v = int(next(it))
        seq_positions[u].append(k)
        seq_positions[v].append(k)
    
    # Sort positions for binary search
    for i in range(1, n + 1):
        seq_positions[i].sort()
    
    # Compute pairwise score F(i, j)
    def compute_score(i, j):
        pos_i = seq_positions[i]
        pos_j = seq_positions[j]
        len_i = len(pos_i)
        len_j = len(pos_j)
        
        # Count positions where both have 1 (intersection)
        # Using two-pointer merge
        count_both = 0
        p1, p2 = 0, 0
        while p1 < len_i and p2 < len_j:
            if pos_i[p1] == pos_j[p2]:
                count_both += 1
                p1 += 1
                p2 += 1
            elif pos_i[p1] < pos_j[p2]:
                p1 += 1
            else:
                p2 += 1
        
        # Score = 3 * count_both + 1 * (m - count_both) = m + 2 * count_both
        return m + 2 * count_both
    
    # For resonance: F(a,b) + F(b,c) + F(c,a) = 3m + 6
    # Let x = count_both(a,b), y = count_both(b,c), z = count_both(c,a)
    # (m + 2x) + (m + 2y) + (m + 2z) = 3m + 6
    # 3m + 2(x + y + z) = 3m + 6
    # x + y + z = 3
    # So we need three pairs with intersection counts summing to 3
    
    # Strategy: Check pairs with intersection >= 1
    # If intersection >= 3, check if there's a third sequence with intersection >= 0
    # If intersection = 2, need another pair with intersection >= 1
    # If intersection = 1, need another pair with intersection >= 2, or two pairs with intersection >= 1
    
    # Precompute pairs with intersection >= 1
    pairs_with_intersection = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # Quick check: if intersection is possible
            pos_i = seq_positions[i]
            pos_j = seq_positions[j]
            if pos_i and pos_j:  # Both have at least one 1
                # Check if they share any position
                p1, p2 = 0, 0
                count = 0
                len_i = len(pos_i)
                len_j = len(pos_j)
                while p1 < len_i and p2 < len_j:
                    if pos_i[p1] == pos_j[p2]:
                        count += 1
                        p1 += 1
                        p2 += 1
                        if count >= 1:
                            break
                    elif pos_i[p1] < pos_j[p2]:
                        p1 += 1
                    else:
                        p2 += 1
                if count >= 1:
                    pairs_with_intersection.append((i, j, count))
    
    # Sort pairs by count (descending) for efficiency
    pairs_with_intersection.sort(key=lambda x: -x[2])
    
    # For each pair with intersection >= 1, try to find a third sequence
    for a, b, count_ab in pairs_with_intersection:
        if count_ab >= 3:
            # Need count_bc + count_ca >= 0, which is always true
            # Find smallest c > b such that c != a and c != b
            for c in range(1, n + 1):
                if c != a and c != b:
                    # Verify the resonance condition
                    score_ab = compute_score(a, b)
                    score_bc = compute_score(b, c)
                    score_ca = compute_score(c, a)
                    if score_ab + score_bc + score_ca == 3 * m + 6:
                        result = sorted([a, b, c])
                        print(result[0], result[1], result[2])
                        return
        elif count_ab == 2:
            # Need count_bc + count_ca >= 1
            # Check pairs that include b or a
            for c in range(1, n + 1):
                if c != a and c != b:
                    # Quick check: does c share with b or a?
                    pos_c = seq_positions[c]
                    if not pos_c:
                        continue
                    # Check intersection with b
                    pos_b = seq_positions[b]
                    count_bc = 0
                    p1, p2 = 0, 0
                    len_b = len(pos_b)
                    len_c = len(pos_c)
                    while p1 < len_b and p2 < len_c:
                        if pos_b[p1] == pos_c[p2]:
                            count_bc += 1
                            p1 += 1
                            p2 += 1
                        elif pos_b[p1] < pos_c[p2]:
                            p1 += 1
                        else:
                            p2 += 1
                    
                    if count_bc >= 1:
                        # Check intersection with a
                        pos_a = seq_positions[a]
                        count_ca = 0
                        p1, p2 = 0, 0
                        len_a = len(pos_a)
                        while p1 < len_a and p2 < len_c:
                            if pos_a[p1] == pos_c[p2]:
                                count_ca += 1
                                p1 += 1
                                p2 += 1
                            elif pos_a[p1] < pos_c[p2]:
                                p1 += 1
                            else:
                                p2 += 1
                        
                        if count_ab + count_bc + count_ca >= 3:
                            score_ab = compute_score(a, b)
                            score_bc = compute_score(b, c)
                            score_ca = compute_score(c, a)
                            if score_ab + score_bc + score_ca == 3 * m + 6:
                                result = sorted([a, b, c])
                                print(result[0], result[1], result[2])
                                return
        else:  # count_ab == 1
            # Need count_bc + count_ca >= 2
            for c in range(1, n + 1):
                if c != a and c != b:
                    pos_c = seq_positions[c]
                    if not pos_c:
                        continue
                    
                    # Check intersection with b
                    pos_b = seq_positions[b]
                    count_bc = 0
                    p1, p2 = 0, 0
                    len_b = len(pos_b)
                    len_c = len(pos_c)
                    while p1 < len_b and p2 < len_c:
                        if pos_b[p1] == pos_c[p2]:
                            count_bc += 1
                            p1 += 1
                            p2 += 1
                        elif pos_b[p1] < pos_c[p2]:
                            p1 += 1
                        else:
                            p2 += 1
                    
                    # Check intersection with a
                    pos_a = seq_positions[a]
                    count_ca = 0
                    p1, p2 = 0, 0
                    len_a = len(pos_a)
                    while p1 < len_a and p2 < len_c:
                        if pos_a[p1] == pos_c[p2]:
                            count_ca += 1
                            p1 += 1
                            p2 += 1
                        elif pos_a[p1] < pos_c[p2]:
                            p1 += 1
                        else:
                            p2 += 1
                    
                    if count_ab + count_bc + count_ca >= 3:
                        score_ab = compute_score(a, b)
                        score_bc = compute_score(b, c)
                        score_ca = compute_score(c, a)
                        if score_ab + score_bc + score_ca == 3 * m + 6:
                            result = sorted([a, b, c])
                            print(result[0], result[1], result[2])
                            return

if __name__ == "__main__":
    solve()