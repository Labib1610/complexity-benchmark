import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    vessels = []
    for _ in range(j):
        t1 = int(next(it))
        t2 = int(next(it))
        vessels.append((t1, t2))
    
    # Sort by t2 descending (Johnson's rule for this specific problem)
    vessels.sort(key=lambda x: -x[1])
    
    total_alpha = 0
    max_gap = 0
    
    for t1, t2 in vessels:
        total_alpha += t1
        # The gap is the time Beta waits for the previous Beta to finish
        # gap = total_alpha - (sum of previous t2s)
        # We track the maximum such gap
        gap = total_alpha - t2
        if gap > max_gap:
            max_gap = gap
    
    # The final completion time is total_alpha + max_gap + last_t2
    # But max_gap is defined as max(total_alpha_i - t2_i)
    # So total_alpha + max_gap = max(total_alpha_i + (total_alpha - total_alpha_i) - t2_i + total_alpha_i)
    #                        = max(total_alpha + total_alpha_i - t2_i)
    # The last Beta starts at max(total_alpha, max(total_alpha_i - t2_i) + total_alpha)
    # which equals total_alpha + max(0, max(total_alpha_i - t2_i))
    # But since max_gap can be negative, we need max(0, max_gap)
    # Actually, the formula total_alpha + max_gap + last_t2 works because:
    # If max_gap <= 0, then total_alpha + max_gap <= total_alpha, and the last Beta starts at total_alpha
    # If max_gap > 0, then total_alpha + max_gap > total_alpha, and the last Beta starts at total_alpha + max_gap
    
    last_t2 = vessels[-1][1]
    result = total_alpha + max_gap + last_t2
    
    # But we need to ensure result is at least total_alpha + last_t2
    # (when max_gap is negative, the formula still works correctly)
    
    print(result)

if __name__ == "__main__":
    solve()