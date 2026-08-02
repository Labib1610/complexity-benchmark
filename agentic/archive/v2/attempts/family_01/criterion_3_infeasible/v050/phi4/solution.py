import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])

edges = [tuple(map(int, data[i:i+2])) for i in range(2, len(data), 2)]

adjacency_list = [[] for _ in range(n + 1)]
for u, v in edges:
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)

# Sort the adjacency lists to ensure lexicographical order
for neighbors in adjacency_list:
    neighbors.sort()

def find_smallest_triplet():
    # Iterate over each possible triplet (a, b, c) with a < b < c
    for a in range(1, n + 1):
        for b in adjacency_list[a]:
            if b > a:  # ensure b > a
                for c in adjacency_list[b]:
                    if c > b and c in adjacency_list[a]:  # ensure c > b and a < b < c with cross-talk between all pairs
                        return a, b, c

result = find_smallest_triplet()
print(result[0], result[1], result[2])