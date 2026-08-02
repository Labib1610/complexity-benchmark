import sys

# Reading inputs
input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])

# Creating adjacency list for incompatible pairs
incompatibility = [[] for _ in range(n + 1)]

index = 2
for i in range(m):
    u = int(data[index])
    v = int(data[index + 1])
    incompatibility[u].append(v)
    incompatibility[v].append(u)
    index += 2

# Sort the incompatible lists for each compound to ensure lexicographical order
for comp in range(1, n + 1):
    incompatibility[comp].sort()

# Function to find the smallest triplet (a, b, c) where all pairs are incompatible
def find_smallest_triplet():
    # We only need to check up to (n-2) for 'a' because we need at least two more numbers after it
    for a in range(1, n - 1):
        for b in incompatibility[a]:
            if b <= a:
                continue  # Ensure b > a
            for c in incompatibility[a]:
                if c <= b or c == a:
                    continue  # Ensure c > b and c != a
                if b in incompatibility[c]:  # Check if the pair (b, c) is also incompatible
                    return a, b, c

# Find and print the result
result = find_smallest_triplet()
print(" ".join(map(str, result)))