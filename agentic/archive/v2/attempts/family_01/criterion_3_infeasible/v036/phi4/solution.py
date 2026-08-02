import sys

def find_impossible_trio(n, m, incompatible_pairs):
    # Create a set for fast lookup of pairs
    pair_set = set()
    for u, v in incompatible_pairs:
        if u > v: 
            u, v = v, u
        pair_set.add((u, v))
    
    # Find the lexicographically smallest trio
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if (i, j) not in pair_set:
                continue
            for k in range(j + 1, n + 1):
                if (i, k) in pair_set and (j, k) in pair_set:
                    return i, j, k

# Read input
input_data = sys.stdin.read().strip().split()
n = int(input_data[0])
m = int(input_data[1])
incompatible_pairs = []
index = 2
for _ in range(m):
    u = int(input_data[index])
    v = int(input_data[index + 1])
    incompatible_pairs.append((u, v))
    index += 2

# Find and print the result
result = find_impossible_trio(n, m, incompatible_pairs)
print(" ".join(map(str, result)))