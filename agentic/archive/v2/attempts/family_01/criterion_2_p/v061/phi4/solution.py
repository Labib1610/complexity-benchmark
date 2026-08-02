from sys import stdin
import operator

# Reading input using map and list comprehensions for efficiency
read = lambda: map(int, stdin.readline().split())
n, m = read()
links = [list(read()) for _ in range(m)]

# Initialize data structures to store degree counts and device connections
d1 = {}
d2 = {}

for i in range(1, n + 1):
    d1[i] = 0
    d2[i] = []

# Populate the adjacency list and degree count based on input links
for u, v in links:
    d1[u] += 1
    d1[v] += 1
    d2[u].append(v)
    d2[v].append(u)

# Sort devices by their degrees to help in lexicographically smallest assignment
sorted_devices = sorted(d1.items(), key=operator.itemgetter(1))

# Initialize the answer array with zeros (default segment assignments)
ans = [0] * n

# Assign segments starting from 1 and try to maintain the constraints
j = 1
for i in range(n):
    ans[sorted_devices[i][0] - 1] = j
    for neighbor in d2[sorted_devices[i][0]]:
        if ans[neighbor - 1] == j:
            j += 1
            ans[sorted_devices[i][0] - 1] = j

# Check for any conflicting assignments and determine the lexicographically smallest valid assignment
for u, v in links:
    if ans[u - 1] == ans[v - 1]:
        print('NO')
        exit(0)

print('YES')
if min(ans) > 1:
    ans = [segment - 1 for segment in ans]
else:
    ans = [1 if x != 0 else 2 for x in ans]

# Output the lexicographically smallest valid assignment
print(*ans)