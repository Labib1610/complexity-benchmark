import sys
from functools import cmp_to_key

def compare_sectors(a, b):
    # a = (p1_a, p2_a), b = (p1_b, p2_b)
    # Compare p2_a + max(p1_b, p2_a) vs p2_b + max(p1_a, p2_b)
    val1 = a[1] + max(b[0], a[1])
    val2 = b[1] + max(a[0], b[1])
    return val1 - val2

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    sectors = []
    index = 1
    for _ in range(j):
        p1 = int(data[index])
        p2 = int(data[index+1])
        sectors.append((p1, p2))
        index += 2
    
    # Sort sectors using the custom comparator
    sectors.sort(key=cmp_to_key(compare_sectors))
    
    # Simulate the process
    radar_time = 0
    sampling_time = 0
    
    for p1, p2 in sectors:
        radar_time += p1
        sampling_time = max(sampling_time, radar_time) + p2
    
    print(sampling_time)

if __name__ == "__main__":
    main()