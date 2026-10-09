import sys
from itertools import accumulate

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    rituals = []
    index = 1
    for _ in range(j):
        p1 = int(data[index])
        p2 = int(data[index+1])
        rituals.append((p1, p2))
        index += 2
    
    # Sort by p1 increasing, then by p2 decreasing
    rituals.sort(key=lambda x: (x[0], -x[1]))
    
    # Compute prefix sums of inscription durations
    inscriptions = [r[0] for r in rituals]
    prefix_inscription = [0] + list(accumulate(inscriptions))
    
    # Compute suffix sums of channeling durations
    channelings = [r[1] for r in rituals]
    suffix_channeling = list(accumulate(channelings[::-1]))[::-1] + [0]
    
    # For each possible focal point k (0-based), compute the strain
    min_max_strain = float('inf')
    for k in range(j):
        strain = prefix_inscription[k+1] + suffix_channeling[k]
        if strain < min_max_strain:
            min_max_strain = strain
            
    print(min_max_strain)

if __name__ == "__main__":
    main()