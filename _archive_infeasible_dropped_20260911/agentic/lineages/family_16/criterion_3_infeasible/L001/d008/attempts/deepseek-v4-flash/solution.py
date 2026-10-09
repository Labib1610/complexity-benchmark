import sys

def solve():
    input = sys.stdin.readline
    j, T = map(int, input().split())
    p1 = []
    p2 = []
    for _ in range(j):
        a, b = map(int, input().split())
        p1.append(a)
        p2.append(b)
    
    # Check local contradiction
    for i in range(j):
        if p1[i] + p2[i] > T:
            print(f"JOB {i+1}")
            return
    
    # Check global contradiction for c=1
    # Sort p1 ascending
    sorted_p1 = sorted(p1)
    # Minimal max V for j intervals: sum of smallest j-1 2^p + largest 2^p
    # Since 2^p can be huge, compare using log2 to avoid big ints
    # We need sum_{smallest j-1} 2^p + 2^{max_p} > 2^T
    # Equivalent to log2(sum) > T
    # We can compute sum of 2^p for smallest j-1, but j up to 2e5, p up to 1e6
    # Use log-sum-exp trick: compute in log domain
    import math
    # For c=1
    # Sort ascending
    s1 = sorted_p1
    # Take smallest j-1
    small = s1[:-1]
    max_p = s1[-1]
    # Compute log2(sum(2^p for small) + 2^max_p)
    # Use log-sum-exp
    if small:
        max_small = max(small)
        # sum_exp = sum(2^(p - max_small)) for p in small
        sum_exp = sum(2.0 ** (p - max_small) for p in small)
        log_sum_small = max_small + math.log2(sum_exp)
    else:
        log_sum_small = -float('inf')
    # Add 2^max_p
    # log2(2^max_p + 2^log_sum_small) = max(max_p, log_sum_small) + log2(1 + 2^{-|diff|})
    if log_sum_small == -float('inf'):
        log_total = max_p
    else:
        if max_p >= log_sum_small:
            log_total = max_p + math.log2(1 + 2 ** (log_sum_small - max_p))
        else:
            log_total = log_sum_small + math.log2(1 + 2 ** (max_p - log_sum_small))
    if log_total > T:
        print("LOAD 1")
        return
    
    # Check global contradiction for c=2
    s2 = sorted(p2)
    small = s2[:-1]
    max_p = s2[-1]
    if small:
        max_small = max(small)
        sum_exp = sum(2.0 ** (p - max_small) for p in small)
        log_sum_small = max_small + math.log2(sum_exp)
    else:
        log_sum_small = -float('inf')
    if log_sum_small == -float('inf'):
        log_total = max_p
    else:
        if max_p >= log_sum_small:
            log_total = max_p + math.log2(1 + 2 ** (log_sum_small - max_p))
        else:
            log_total = log_sum_small + math.log2(1 + 2 ** (max_p - log_sum_small))
    if log_total > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    solve()