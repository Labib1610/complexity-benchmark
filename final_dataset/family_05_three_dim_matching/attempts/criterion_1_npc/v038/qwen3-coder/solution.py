from itertools import combinations
import sys

def read_input():
    k, t = map(int, sys.stdin.readline().split())
    triplets = []
    for _ in range(t):
        a, b, c = map(int, sys.stdin.readline().split())
        triplets.append((a, b, c))
    return k, t, triplets

def is_valid_selection(selection, k):
    # Check if all channels are unique
    primary_channels = [triplet[0] for triplet in selection]
    backup_channels = [triplet[1] for triplet in selection]
    diagnostic_channels = [triplet[2] for triplet in selection]
    
    if len(set(primary_channels)) != k or len(set(backup_channels)) != k or len(set(diagnostic_channels)) != k:
        return False
    
    # Check the checksum requirement
    total_sum = sum(sum(triplet) for triplet in selection)
    expected_sum = 3 * k * (k + 1) // 2
    
    return total_sum == expected_sum

def solve(k, t, triplets):
    # Try all combinations of k triplets
    for combination in combinations(triplets, k):
        if is_valid_selection(combination, k):
            return True, combination
    
    return False, []

def main():
    k, t, triplets = read_input()
    found, selected = solve(k, t, triplets)
    
    if found:
        print("YES")
        for triplet in selected:
            print(triplet[0], triplet[1], triplet[2])
    else:
        print("NO")

if __name__ == "__main__":
    main()