import sys
from itertools import accumulate

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    packets = []
    index = 1
    for _ in range(j):
        p1 = int(data[index])
        p2 = int(data[index+1])
        packets.append((p1, p2))
        index += 2
    
    # Sort packets by p1 - p2
    packets.sort(key=lambda x: x[0] - x[1])
    
    # Compute prefix sums for p1
    p1_list = [p[0] for p in packets]
    prefix_p1 = [0] + list(accumulate(p1_list))
    
    # Compute suffix sums for p2
    p2_list = [p[1] for p in packets]
    suffix_p2 = list(accumulate(p2_list[::-1]))[::-1] + [0]
    
    # Calculate the maximum latency over all possible switch positions
    max_latency = 0
    for k in range(1, j+1):
        latency = prefix_p1[k] + suffix_p2[k-1]
        if latency > max_latency:
            max_latency = latency
    
    print(max_latency)

if __name__ == "__main__":
    main()