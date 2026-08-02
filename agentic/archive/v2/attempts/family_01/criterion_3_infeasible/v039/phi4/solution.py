import sys

# Read input from stdin
input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])

# Initialize adjacency list for graph representation
adj_list = [[] for _ in range(n + 1)]

index = 2
for i in range(m):
    u = int(data[index])
    v = int(data[index + 1])
    adj_list[u].append(v)
    adj_list[v].append(u)
    index += 2

# Sort the adjacency lists to make searching easier and ensure lexicographical order
for neighbors in adj_list:
    neighbors.sort()

# Find the first triple (a, b, c) such that a < b < c and all pairs interfere with each other
for a in range(1, n + 1):
    for b in adj_list[a]:
        if b > a:  # Ensure b > a
            for c in adj_list[b]:
                if c > b and c in adj_list[a]:  # Ensure c > b and all pairs (a, b), (b, c), (a, c) interfere
                    print(a, b, c)
                    sys.exit()