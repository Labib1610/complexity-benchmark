import sys
from itertools import accumulate

def main():
    j = int(sys.stdin.readline())
    manuscripts = []
    for _ in range(j):
        p1, p2 = map(int, sys.stdin.readline().split())
        manuscripts.append((p1, p2))
    
    # For each possible transition point k (1-indexed),
    # the reviewer's time is sum(p1[1..k]) + sum(p2[k..j])
    # We want to minimize the maximum of these values over all k
    
    # Compute prefix sums of p1
    p1_prefix = [0] + list(accumulate(m.p1 for m in manuscripts))
    
    # Compute suffix sums of p2
    p2_suffix = [0] * (j + 1)
    for i in range(j - 1, -1, -1):
        p2_suffix[i] = p2_suffix[i + 1] + manuscripts[i][1]
    
    # Find the minimum of the maximum times
    min_max_time = float('inf')
    for k in range(1, j + 1):
        # Transition at manuscript k (1-indexed)
        # Sum of p1 from 1 to k plus sum of p2 from k to j
        time = p1_prefix[k] + p2_suffix[k - 1]
        min_max_time = min(min_max_time, time)
    
    print(min_max_time)

if __name__ == "__main__":
    main()