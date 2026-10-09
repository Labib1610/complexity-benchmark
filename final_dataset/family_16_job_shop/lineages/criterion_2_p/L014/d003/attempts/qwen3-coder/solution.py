import sys
from functools import cmp_to_key

def compare_packets(a, b):
    # a[0] is p1, a[1] is p2 for packet a
    # Sort by p1 ascending, then by p2 descending
    if a[0] != b[0]:
        return a[0] - b[0]
    else:
        return b[1] - a[1]

def main():
    j = int(sys.stdin.readline())
    packets = []
    
    for _ in range(j):
        p1, p2 = map(int, sys.stdin.readline().split())
        packets.append((p1, p2))
    
    # Sort packets according to the optimal strategy
    # Johnson's rule: sort by min(p1, p2) but more specifically:
    # Packets with p1 < p2 should go first, sorted by p1 ascending
    # Packets with p1 >= p2 should go later, sorted by p2 descending
    
    # We use the comparison function that sorts by p1 ascending, then by p2 descending
    packets.sort(key=cmp_to_key(compare_packets))
    
    # Calculate the total time
    tup = 0  # Time when uplink finishes for current packet
    tdown = 0  # Time when downlink finishes for current packet
    
    for p1, p2 in packets:
        tup += p1
        tdown = max(tup, tdown) + p2
    
    print(tdown)

if __name__ == "__main__":
    main()