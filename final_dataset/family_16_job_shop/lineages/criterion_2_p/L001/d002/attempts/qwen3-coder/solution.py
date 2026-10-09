import sys
from functools import cmp_to_key

def compare(x, y):
    # x = (p1, p2), y = (p1, p2)
    # We want to sort such that the maximum clearance time is minimized
    # The key insight is to sort by (p1 - p2)
    # If p1_x - p2_x < p1_y - p2_y, then x should come before y
    diff_x = x[0] - x[1]
    diff_y = y[0] - y[1]
    if diff_x < diff_y:
        return -1
    elif diff_x > diff_y:
        return 1
    else:
        return 0

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    dossiers = []
    index = 1
    for _ in range(j):
        p1 = int(data[index])
        p2 = int(data[index+1])
        dossiers.append((p1, p2))
        index += 2
    
    # Sort dossiers based on (p1 - p2) in ascending order
    dossiers.sort(key=cmp_to_key(compare))
    
    # Calculate the maximum clearance metric
    max_clearance = 0
    prefix_sum_p1 = 0
    suffix_sum_p2 = sum(dossier[1] for dossier in dossiers)
    
    for p1, p2 in dossiers:
        prefix_sum_p1 += p1
        clearance = prefix_sum_p1 + suffix_sum_p2
        max_clearance = max(max_clearance, clearance)
        suffix_sum_p2 -= p2
    
    print(max_clearance)

if __name__ == "__main__":
    main()