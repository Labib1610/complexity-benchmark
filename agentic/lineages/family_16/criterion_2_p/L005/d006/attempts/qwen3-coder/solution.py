import sys
from itertools import accumulate

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    vessels = []
    idx = 1
    for _ in range(j):
        t1 = int(data[idx])
        t2 = int(data[idx+1])
        vessels.append((t1, t2))
        idx += 2
    
    # Sort vessels by t1 increasing and t2 decreasing
    # This is the optimal ordering to minimize the max chain duration
    vessels.sort(key=lambda x: (x[0], -x[1]))
    
    # Precompute prefix sums of t1
    prefix_t1 = [0] + list(accumulate(v[0] for v in vessels))
    
    # Precompute suffix sums of t2
    suffix_t2 = [0] * (j + 1)
    for i in range(j-1, -1, -1):
        suffix_t2[i] = suffix_t2[i+1] + vessels[i][1]
    
    # Find the minimum exposure rating over all possible pivot positions
    min_exposure = float('inf')
    for k in range(1, j+1):
        chain_duration = prefix_t1[k] + suffix_t2[k-1]
        if chain_duration < min_exposure:
            min_exposure = chain_duration
    
    print(min_exposure)

if __name__ == "__main__":
    main()