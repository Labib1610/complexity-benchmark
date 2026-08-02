import sys

def find_smallest_triple(n, m, links):
    # Create adjacency list
    adj = [[] for _ in range(n + 1)]
    for u, v in links:
        adj[u].append(v)
        adj[v].append(u)

    # Sort the adjacency lists to ensure lexicographical order
    for neighbors in adj:
        neighbors.sort()

    # Try every combination of three different servers
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if b in adj[a]:
                for c in range(b + 1, n + 1):
                    if c in adj[a] and c in adj[b]:
                        return (a, b, c)

# Read input
input = sys.stdin.read
data = input().split()
n = int(data[0])
m = int(data[1])

links = []
index = 2
for _ in range(m):
    u = int(data[index])
    v = int(data[index + 1])
    links.append((u, v))
    index += 2

# Find the smallest triple and print it
result = find_smallest_triple(n, m, links)
print(result[0], result[1], result[2])