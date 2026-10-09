import sys
from functools import cmp_to_key

def compare(vessel1, vessel2):
    p1_1, p2_1 = vessel1
    p1_2, p2_2 = vessel2
    
    # Compare p1_1 - p2_2 with p1_2 - p2_1
    # If p1_1 - p2_2 < p1_2 - p2_1, then vessel1 should come before vessel2
    if p1_1 - p2_2 < p1_2 - p2_1:
        return -1
    elif p1_1 - p2_2 > p1_2 - p2_1:
        return 1
    else:
        return 0

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    vessels = []
    index = 1
    for _ in range(j):
        p1 = int(data[index])
        p2 = int(data[index+1])
        vessels.append((p1, p2))
        index += 2
    
    # Sort vessels using the custom comparator
    vessels.sort(key=cmp_to_key(compare))
    
    # Calculate F_j
    L = 0
    F = 0
    for p1, p2 in vessels:
        L += p1
        F = max(F, L) + p2
    
    print(F)

if __name__ == "__main__":
    main()