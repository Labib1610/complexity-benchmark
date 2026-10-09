import sys
from functools import cmp_to_key

def compare_cakes(a, b):
    # a = (oven_time, frosting_time, index)
    # b = (oven_time, frosting_time, index)
    # Sort by min(oven_time, frosting_time) descending
    # If equal, sort by oven_time descending
    min_a = min(a[0], a[1])
    min_b = min(b[0], b[1])
    if min_a != min_b:
        return min_b - min_a
    return b[0] - a[0]

def main():
    j = int(sys.stdin.readline())
    cakes = []
    
    for i in range(j):
        p1, p2 = map(int, sys.stdin.readline().split())
        cakes.append((p1, p2))
    
    # Create list with indices to maintain original order information if needed
    indexed_cakes = [(cakes[i][0], cakes[i][1], i) for i in range(j)]
    
    # Sort according to the rule: 
    # First by min(oven, frosting) descending
    # Then by oven time descending
    indexed_cakes.sort(key=cmp_to_key(compare_cakes))
    
    # Simulate the process
    oven_finish_time = 0
    frosting_finish_time = 0
    
    for oven_time, frosting_time, idx in indexed_cakes:
        # Cake finishes oven at this time
        oven_finish_time += oven_time
        # Frosting can start only when both:
        # 1. This cake finishes oven (oven_finish_time)
        # 2. Previous cake finishes frosting (frosting_finish_time)
        frosting_start_time = max(oven_finish_time, frosting_finish_time)
        frosting_finish_time = frosting_start_time + frosting_time
    
    print(frosting_finish_time)

if __name__ == "__main__":
    main()