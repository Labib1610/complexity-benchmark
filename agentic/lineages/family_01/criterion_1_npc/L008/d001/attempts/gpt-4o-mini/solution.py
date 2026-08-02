def can_color(n, edges):
    colors = [0] * (n + 1)

    def backtrack(task):
        if task > n:
            return True

        for color in range(1, 4):
            # Check if the current color can be used
            if all(colors[neighbor] != color for neighbor in edges[task]):
                colors[task] = color
                if backtrack(task + 1):
                    return True
                colors[task] = 0  # Backtrack

        return False

    if backtrack(1):
        return colors[1:]
    return None

import sys
from collections import defaultdict

input = sys.stdin.read
data = input().strip().splitlines()

n, m = map(int, data[0].split())
edges = defaultdict(list)

for i in range(1, m + 1):
    u, v = map(int, data[i].split())
    edges[u].append(v)
    edges[v].append(u)

result = can_color(n, edges)

if result is None:
    print("NO")
else:
    print("YES")
    print(' '.join(map(str, result)))