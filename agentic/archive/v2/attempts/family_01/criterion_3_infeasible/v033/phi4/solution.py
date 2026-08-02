import sys

def find_incompatible_triplet(n, m, incompatible_pairs):
    # Create adjacency list for storing incompatible pairs
    adj_list = [set() for _ in range(n + 1)]
    
    for u, v in incompatible_pairs:
        adj_list[u].add(v)
        adj_list[v].add(u)

    # Iterate over all possible triplets (a, b, c) with a < b < c
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if b not in adj_list[a]:
                continue
            for c in range(b + 1, n + 1):
                if c in adj_list[a] and c in adj_list[b]:
                    return a, b, c

# Read input
input = sys.stdin.read
data = input().split()
n = int(data[0])
m = int(data[1])

incompatible_pairs = []
index = 2
for _ in range(m):
    u = int(data[index])
    v = int(data[index + 1])
    incompatible_pairs.append((u, v))
    index += 2

# Find and print the lexicographically smallest triplet
a, b, c = find_incompatible_triplet(n, m, incompatible_pairs)
print(a, b, c)